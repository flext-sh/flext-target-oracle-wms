"""Dependency Injection container for Oracle WMS target using flext-core patterns."""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextResult, get_flext_container, get_logger

logger = get_logger(__name__)


class TargetOracleWMSContainer:
    """Dependency Injection container for Oracle WMS Target."""

    def __init__(self) -> None:
        """Initialize Oracle WMS Target DI container."""
        self._flext_container = get_flext_container()

    def register_service(self, name: str, service: Any) -> FlextResult[None]:
        """Register a service in the container."""
        try:
            self._flext_container.register_service(name, service)
            logger.debug(f"Registered Oracle WMS service: {name}")
            return FlextResult.ok(None)

        except Exception as e:
            logger.exception(f"Failed to register Oracle WMS service: {name}")
            return FlextResult.fail(f"Service registration failed: {e}")

    def get_service(self, name: str) -> FlextResult[Any]:
        """Get a service from the container."""
        try:
            service = self._flext_container.get_service(name)
            return FlextResult.ok(service)

        except Exception as e:
            logger.exception(f"Failed to get Oracle WMS service: {name}")
            return FlextResult.fail(f"Service retrieval failed: {e}")

    def has_service(self, name: str) -> bool:
        """Check if service exists in container."""
        return self._flext_container.has_service(name)

    def remove_service(self, name: str) -> FlextResult[None]:
        """Remove a service from the container."""
        try:
            self._flext_container.remove_service(name)
            logger.debug(f"Removed Oracle WMS service: {name}")
            return FlextResult.ok(None)

        except Exception as e:
            logger.exception(f"Failed to remove Oracle WMS service: {name}")
            return FlextResult.fail(f"Service removal failed: {e}")

    def clear_services(self) -> FlextResult[None]:
        """Clear all services from container."""
        try:
            self._flext_container.clear_services()
            logger.info("Cleared all Oracle WMS services")
            return FlextResult.ok(None)

        except Exception as e:
            logger.exception("Failed to clear Oracle WMS services")
            return FlextResult.fail(f"Service clearing failed: {e}")

    def get_service_names(self) -> list[str]:
        """Get all registered service names."""
        return self._flext_container.get_service_names()

    def configure_wms_services(self, config: dict[str, Any]) -> FlextResult[None]:
        """Configure standard WMS services."""
        try:
            # Import WMS components
            from flext_target_oracle_wms.connection import (
                OracleWMSConnection,
                OracleWMSConnectionConfig,
            )
            from flext_target_oracle_wms.patterns import (
                WMSDataTransformer,
                WMSSchemaMapper,
                WMSTableManager,
                WMSTypeConverter,
            )

            # Configure Oracle connection
            connection_config = OracleWMSConnectionConfig(
                host=config.get("host", "localhost"),
                port=config.get("port", 1521),
                service_name=config.get("service_name", "XE"),
                username=config.get("username", "oracle"),
                password=config.get("password", "oracle"),
                schema=config.get("default_target_schema", "WMS_TARGET"),
                max_connections=config.get("max_connections", 10),
                connection_timeout=config.get("connection_timeout", 30),
            )

            oracle_connection = OracleWMSConnection(connection_config)

            # Register core services
            self.register_service("oracle_connection", oracle_connection)
            self.register_service("type_converter", WMSTypeConverter())
            self.register_service("data_transformer", WMSDataTransformer())
            self.register_service("schema_mapper", WMSSchemaMapper())
            self.register_service("table_manager", WMSTableManager())

            logger.info("Oracle WMS services configured successfully")
            return FlextResult.ok(None)

        except Exception as e:
            logger.exception("Failed to configure Oracle WMS services")
            return FlextResult.fail(f"Service configuration failed: {e}")


def get_target_oracle_wms_container() -> FlextResult[TargetOracleWMSContainer]:
    """Get Oracle WMS Target DI container instance."""
    try:
        container = TargetOracleWMSContainer()
        return FlextResult.ok(container)

    except Exception as e:
        logger.exception("Failed to create Oracle WMS Target container")
        return FlextResult.fail(f"Container creation failed: {e}")
