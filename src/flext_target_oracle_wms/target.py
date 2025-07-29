"""Target Oracle WMS implementation using Singer SDK and flext-core patterns."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

import sqlalchemy as sa

# Import from flext-core for foundational patterns
from flext_core import FlextError as FlextServiceError, FlextResult

# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano.singer import FlextMeltanoTarget as Target

# Import from new modular architecture
from flext_target_oracle_wms.application import OracleWMSTargetOrchestrator
from flext_target_oracle_wms.config import TargetOracleWMSConfig
from flext_target_oracle_wms.infrastructure import get_target_oracle_wms_container
from flext_target_oracle_wms.sinks import OracleWMSSink

if TYPE_CHECKING:
    from collections.abc import Sequence

try:
    import oracledb
except ImportError:
    oracledb = None


class TargetOracleWMS(Target):
    """FLEXT Target Oracle WMS - Singer target for Oracle WMS data loading."""

    name = "target-oracle-wms"
    config_class = TargetOracleWMSConfig
    default_sink_class = OracleWMSSink

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        *,
        parse_env_config: bool = False,
        validate_config: bool = True,
    ) -> None:
        """Initialize the target."""
        # Handle nested oracle_config structure from Meltano
        if config and "oracle_config" in config:
            oracle_config = config.pop("oracle_config")
            # Map username to user for compatibility
            if "username" in oracle_config:
                oracle_config["user"] = oracle_config.pop("username")
            # Convert port to int if it's a string
            if "port" in oracle_config and isinstance(oracle_config["port"], str):
                try:
                    oracle_config["port"] = int(oracle_config["port"])
                except ValueError:
                    oracle_config["port"] = 1521
            config.update(oracle_config)

        super().__init__(
            config=config,
            parse_env_config=parse_env_config,
            validate_config=validate_config,
        )

        # Initialize Oracle connection pool
        self._engine: sa.Engine | None = None
        self._connection_pool: oracledb.ConnectionPool | None = None

        # Initialize orchestrator with new modular architecture
        self._orchestrator: OracleWMSTargetOrchestrator | None = None
        self._container = None

    @property
    def engine(self) -> sa.Engine:
        """Get or create SQLAlchemy engine with Oracle connection."""
        if self._engine is None:
            connection_string = self._build_connection_string()

            self._engine = sa.create_engine(
                connection_string,
                pool_size=self.config.max_connections,
                max_overflow=10,
                pool_timeout=self.config.connection_timeout,
                pool_recycle=3600,  # Recycle connections after 1 hour
                echo=self.logger.isEnabledFor(10),  # Echo SQL if debug logging
            )

        return self._engine

    def build_connection_string(self) -> str:
        """Build Oracle connection string from config."""
        return self._build_connection_string()

    def _build_connection_string(self) -> str:
        """Build Oracle connection string from config."""
        host = self.config.host
        port = self.config.port
        service_name = self.config.service_name
        username = self.config.username
        password = self.config.password

        # Oracle connection string format
        return f"oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}"

    def get_sink(
        self,
        stream_name: str,
        *,
        record: dict[Any, Any] | None = None,
        schema: dict[Any, Any] | None = None,
        key_properties: Sequence[str] | None = None,
    ) -> OracleWMSSink:
        """Get a sink for the given stream."""
        return self.default_sink_class(
            target=self,
            stream_name=stream_name,
            schema=schema,
            key_properties=list(key_properties) if key_properties else None,
        )

    def validate_connection(self) -> FlextResult[bool]:
        """Validate Oracle WMS connection."""
        try:
            with self.engine.connect() as conn:
                # Test basic connection
                result = conn.execute(sa.text("SELECT 1 FROM DUAL"))
                result.fetchone()

                self.logger.info("Oracle WMS connection validated successfully")
                return FlextResult.ok(True)

        except (RuntimeError, ValueError, TypeError) as e:
            error_msg = f"Oracle WMS connection validation failed: {e}"
            self.logger.exception(error_msg)
            return FlextResult.fail(error_msg)

    @property
    def orchestrator(self) -> OracleWMSTargetOrchestrator:
        """Get or create orchestrator."""
        if self._orchestrator is None:
            self._orchestrator = OracleWMSTargetOrchestrator(dict(self.config))
        return self._orchestrator

    def setup(self) -> None:
        """Setup the Oracle WMS target."""
        super().setup()

        # Validate connection on setup
        validation_result = self.validate_connection()
        if not validation_result.is_success:
            msg = f"Target setup failed: {validation_result.error}"
            raise FlextServiceError(msg)

        # Initialize orchestrator and container
        init_result = self.orchestrator.initialize()
        if not init_result.is_success:
            msg = f"Orchestrator initialization failed: {init_result.error}"
            raise FlextServiceError(msg)

        # Initialize DI container
        container_result = get_target_oracle_wms_container()
        if container_result.is_success:
            self._container = container_result.data
            config_result = self._container.configure_wms_services(dict(self.config))
            if not config_result.is_success:
                self.logger.warning(
                    f"Container configuration failed: {config_result.error}",
                )

        self.logger.info(f"Oracle WMS target setup completed for {self.config.host}")

    def teardown(self) -> None:
        """Teardown the Oracle WMS target."""
        # Cleanup orchestrator
        if self._orchestrator:
            cleanup_result = self._orchestrator.cleanup()
            if not cleanup_result.is_success:
                self.logger.warning(
                    f"Orchestrator cleanup failed: {cleanup_result.error}",
                )
            self._orchestrator = None

        # Cleanup container
        if self._container:
            clear_result = self._container.clear_services()
            if not clear_result.is_success:
                self.logger.warning(f"Container cleanup failed: {clear_result.error}")
            self._container = None

        if self._engine:
            self._engine.dispose()
            self._engine = None

        if self._connection_pool:
            self._connection_pool.close()
            self._connection_pool = None

        super().teardown()
        self.logger.info("Oracle WMS target teardown completed")


def main() -> None:
    """CLI entry point for target-oracle-wms."""
    # from flext_meltano import target_test_runner  # Not available

    # Basic CLI support
    if len(sys.argv) > 1 and sys.argv[1] == "--help":

        sys.stdout.write("Usage: target-oracle-wms [--help] [--config CONFIG_FILE]\n")
        sys.stdout.write("\nOracle WMS target for Singer\n")
        sys.stdout.write("\nOptions:\n")
        sys.stdout.write("  --help              Show this help message\n")
        sys.stdout.write("  --config FILE       Configuration file path\n")
        return

    # Run the target
    target = TargetOracleWMS()
    # target_test_runner(target)  # Not available - use Singer SDK directly
    target.cli()


if __name__ == "__main__":
    main()
