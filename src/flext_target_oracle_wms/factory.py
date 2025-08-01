"""FlextTargetFactory - Simplified target creation with production-ready patterns.

This factory implements SOLID principles to make flext-* libraries easier to use,
providing pre-configured setups for common use cases while maintaining full flexibility.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

# DRY: Use REAL flext-* APIs for consistency
from flext_core import FlextResult, get_logger
from flext_observability import FlextObservabilityMonitor

# Use REAL implementation - NO DUPLICATION
from flext_target_oracle_wms.singer.target import SingerTargetOracleWMS

# =============================================================================
# REFACTORING: Parameter Object Pattern for reducing method complexity
# =============================================================================


@dataclass
class TargetCreationRequest:
    """Parameter Object: Encapsulates target creation parameters.

    SOLID REFACTORING: Reduces parameter count in factory methods from 6-7 to 1
    using Parameter Object Pattern for better maintainability and extensibility.
    """

    base_url: str
    username: str
    password: str
    environment: str = "development"
    preset: str | None = None
    additional_config: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        """Initialize additional_config if not provided."""
        if self.additional_config is None:
            self.additional_config = {}


@dataclass
class MonitoredTargetCreationRequest(TargetCreationRequest):
    """Parameter Object: Extends TargetCreationRequest with monitoring configuration.

    SOLID REFACTORING: Specialized parameter object for monitored target creation
    following Open/Closed Principle.
    """

    monitor_name: str = "oracle_wms_target"


# Get logger using flext-core patterns
logger = get_logger(__name__)


class FlextTargetFactory:
    """Factory for creating Oracle WMS targets with pre-configured patterns.

    This factory implements SOLID principles:
    - Single Responsibility: Creates and configures targets
    - Open/Closed: Extensible through configuration presets
    - Liskov Substitution: All created targets are compatible
    - Interface Segregation: Focused on target creation only
    - Dependency Inversion: Depends on abstractions, not concrete classes
    """

    # Common configuration presets for different environments
    PRESETS: ClassVar[dict[str, dict[str, Any]]] = {
        "development": {
            "batch_size": 100,
            "table_prefix": "DEV_",
            "schema_name": "WMS_DEV",
            "timeout": 30.0,
            "max_retries": 3,
            "verify_ssl": False,
            "enable_logging": True,
        },
        "staging": {
            "batch_size": 500,
            "table_prefix": "STG_",
            "schema_name": "WMS_STAGING",
            "timeout": 60.0,
            "max_retries": 5,
            "verify_ssl": True,
            "enable_logging": True,
        },
        "production": {
            "batch_size": 1000,
            "table_prefix": "PROD_",
            "schema_name": "WMS_PRODUCTION",
            "timeout": 120.0,
            "max_retries": 10,
            "verify_ssl": True,
            "enable_logging": True,
        },
        "testing": {
            "batch_size": 10,
            "table_prefix": "TEST_",
            "schema_name": "WMS_TEST",
            "timeout": 15.0,
            "max_retries": 1,
            "verify_ssl": False,
            "enable_logging": False,
        },
    }

    @classmethod
    def create_target(
        cls,
        request: TargetCreationRequest,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create Oracle WMS target with smart defaults and presets.

        SOLID REFACTORING: Reduced parameter count from 6 to 1 using Parameter Object Pattern.

        Args:
            request: TargetCreationRequest containing all target creation parameters

        Returns:
            FlextResult containing configured target or error

        """
        try:
            logger.debug(
                f"Creating Oracle WMS target for environment: {request.environment}"
            )

            # Start with base configuration
            config = {
                "base_url": request.base_url,
                "username": request.username,
                "password": request.password,
                "environment": request.environment,
            }

            # Apply preset if specified
            if request.preset and request.preset in cls.PRESETS:
                config.update(cls.PRESETS[request.preset])
                logger.debug(f"Applied preset: {request.preset}")
            elif request.preset:
                logger.warning(f"Unknown preset: {request.preset}, using defaults")

            # Apply any additional configuration overrides
            if request.additional_config:
                config.update(request.additional_config)

            # Create target with final configuration
            target = SingerTargetOracleWMS(config)

            logger.info(
                f"Created Oracle WMS target for {request.environment} with preset {request.preset}",
            )
            return FlextResult.ok(target)

        except Exception as e:
            error_msg = f"Failed to create Oracle WMS target: {e}"
            logger.exception(error_msg)
            return FlextResult.fail(error_msg)

    @classmethod
    def create_target_legacy(
        cls,
        base_url: str,
        username: str,
        password: str,
        environment: str = "development",
        preset: str | None = None,
        **additional_config: Any,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Legacy method for backward compatibility - delegates to Parameter Object version.

        SOLID REFACTORING: Maintains backward compatibility while using improved Parameter Object Pattern.
        """
        request = TargetCreationRequest(
            base_url=base_url,
            username=username,
            password=password,
            environment=environment,
            preset=preset,
            additional_config=additional_config,
        )
        return cls.create_target(request)

    @classmethod
    def create_development_target(
        cls,
        base_url: str,
        username: str = "dev_user",
        password: str = "dev_password",
        **overrides: Any,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create development target with optimized settings."""
        request = TargetCreationRequest(
            base_url=base_url,
            username=username,
            password=password,
            environment="development",
            preset="development",
            additional_config=overrides,
        )
        return cls.create_target(request)

    @classmethod
    def create_production_target(
        cls,
        base_url: str,
        username: str,
        password: str,
        **overrides: Any,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create production target with optimized settings."""
        request = TargetCreationRequest(
            base_url=base_url,
            username=username,
            password=password,
            environment="production",
            preset="production",
            additional_config=overrides,
        )
        return cls.create_target(request)

    @classmethod
    def create_testing_target(
        cls,
        base_url: str = "https://test.wms.oracle.com",
        username: str = "test_user",
        password: str = "test_password",
        **overrides: Any,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create testing target with optimized settings."""
        request = TargetCreationRequest(
            base_url=base_url,
            username=username,
            password=password,
            environment="testing",
            preset="testing",
            additional_config=overrides,
        )
        return cls.create_target(request)

    @classmethod
    def create_from_config_dict(
        cls,
        config: dict[str, Any],
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create target from configuration dictionary.

        Args:
            config: Complete configuration dictionary

        Returns:
            FlextResult containing configured target or error

        """
        try:
            # Validate required fields
            required_fields = ["base_url", "username", "password"]
            missing_fields = [field for field in required_fields if field not in config]

            if missing_fields:
                error_msg = f"Missing required configuration fields: {missing_fields}"
                logger.error(error_msg)
                return FlextResult.fail(error_msg)

            # Extract preset if specified
            preset = config.pop("preset", None)
            environment = config.get("environment", "development")

            # Create target using preset logic with Parameter Object
            request = TargetCreationRequest(
                base_url=config.pop("base_url"),
                username=config.pop("username"),
                password=config.pop("password"),
                environment=environment,
                preset=preset,
                additional_config=config,
            )
            return cls.create_target(request)

        except Exception as e:
            error_msg = f"Failed to create target from config: {e}"
            logger.exception(error_msg)
            return FlextResult.fail(error_msg)


class FlextTargetMonitoringFactory:
    """Factory for creating monitored targets with observability.

    Extends the basic factory with built-in flext-observability integration
    for production monitoring and metrics collection.
    """

    def __init__(self, monitor_name: str = "oracle_wms_target") -> None:
        """Initialize monitoring factory.

        Args:
            monitor_name: Name for the observability monitor

        """
        # Initialize monitor with proper FlextContainer
        self.monitor = FlextObservabilityMonitor()
        self.monitor_name = monitor_name
        self.factory = FlextTargetFactory()

    def create_monitored_target(
        self,
        request: MonitoredTargetCreationRequest,
    ) -> FlextResult[SingerTargetOracleWMS]:
        """Create monitored target with observability integration.

        SOLID REFACTORING: Reduced parameter count from 6 to 1 using Parameter Object Pattern.

        Args:
            request: MonitoredTargetCreationRequest containing all target creation parameters

        Returns:
            FlextResult containing monitored target or error

        """
        try:
            # Create target using base factory with Parameter Object
            target_request = TargetCreationRequest(
                base_url=request.base_url,
                username=request.username,
                password=request.password,
                environment=request.environment,
                preset=request.preset,
                additional_config=request.additional_config,
            )
            target_result = self.factory.create_target(target_request)

            if not target_result.is_success:
                return target_result

            target = target_result.data
            if target is None:
                return FlextResult.fail("Target creation returned None")

            # Initialize monitoring services
            init_result = self.monitor.flext_initialize_observability()
            if not init_result.is_success:
                logger.warning(f"Failed to initialize monitoring: {init_result.error}")
                # Continue without monitoring rather than fail
                return FlextResult.ok(target)

            # Start monitoring
            start_result = self.monitor.flext_start_monitoring()
            if not start_result.is_success:
                logger.warning(f"Failed to start monitoring: {start_result.error}")
                # Continue without monitoring rather than fail
                return FlextResult.ok(target)

            # Add basic monitoring through logging - KISS approach
            logger.info(
                f"Created monitored target for {request.environment} with observability integration",
            )
            return FlextResult.ok(target)

        except Exception as e:
            error_msg = f"Failed to create monitored target: {e}"
            logger.exception(error_msg)
            return FlextResult.fail(error_msg)


# DRY: Export factory functions for easy access
def create_oracle_wms_target(
    base_url: str,
    username: str,
    password: str,
    environment: str = "development",
    preset: str | None = None,
    **config: Any,
) -> FlextResult[SingerTargetOracleWMS]:
    """Convenient function to create Oracle WMS target.

    This is a simplified interface to the FlextTargetFactory for easy usage.
    Uses Parameter Object Pattern internally for better performance.
    """
    request = TargetCreationRequest(
        base_url=base_url,
        username=username,
        password=password,
        environment=environment,
        preset=preset,
        additional_config=config,
    )
    return FlextTargetFactory.create_target(request)


def create_monitored_oracle_wms_target(
    base_url: str,
    username: str,
    password: str,
    environment: str = "development",
    preset: str | None = None,
    monitor_name: str = "oracle_wms_target",
    **config: Any,
) -> FlextResult[SingerTargetOracleWMS]:
    """Convenient function to create monitored Oracle WMS target.

    This is a simplified interface to the FlextTargetMonitoringFactory for easy usage.
    Uses Parameter Object Pattern internally for better performance.
    """
    factory = FlextTargetMonitoringFactory(monitor_name)
    request = MonitoredTargetCreationRequest(
        base_url=base_url,
        username=username,
        password=password,
        environment=environment,
        preset=preset,
        additional_config=config,
        monitor_name=monitor_name,
    )
    return factory.create_monitored_target(request)
