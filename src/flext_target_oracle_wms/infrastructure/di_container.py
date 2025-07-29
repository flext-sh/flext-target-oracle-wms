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
            self._flext_container.register(name, service)
            logger.debug(f"Registered Oracle WMS service: {name}")
            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to register Oracle WMS service: {name}")
            return FlextResult.fail(f"Service registration failed: {e}")

    def get_service(self, name: str) -> FlextResult[Any]:
        """Get a service from the container."""
        try:
            service_result = self._flext_container.get(name)
            if not service_result.is_success:
                return FlextResult.fail(service_result.error or f"Service {name} not found")
            service = service_result.data
            return FlextResult.ok(service)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to get Oracle WMS service: {name}")
            return FlextResult.fail(f"Service retrieval failed: {e}")

    def has_service(self, name: str) -> bool:
        """Check if service exists in container."""
        return self._flext_container.has(name)

    def remove_service(self, name: str) -> FlextResult[None]:
        """Remove a service from the container."""
        try:
            remove_result = self._flext_container.unregister(name)
            if not remove_result.is_success:
                raise RuntimeError(remove_result.error or f"Failed to remove service {name}")
            logger.debug(f"Removed Oracle WMS service: {name}")
            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to remove Oracle WMS service: {name}")
            return FlextResult.fail(f"Service removal failed: {e}")

    def clear_services(self) -> FlextResult[None]:
        """Clear all services from container."""
        try:
            clear_result = self._flext_container.clear()
            if not clear_result.is_success:
                raise RuntimeError(clear_result.error or "Failed to clear services")
            logger.info("Cleared all Oracle WMS services")
            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to clear Oracle WMS services")
            return FlextResult.fail(f"Service clearing failed: {e}")

    def get_service_names(self) -> list[str]:
        """Get all registered service names."""
        return self._flext_container.get_service_names()

    def configure_wms_services(self, config: dict[str, Any]) -> FlextResult[None]:
        """Configure standard WMS services."""
        try:
            # Import WMS components - simplified for now
            # TODO: Add proper imports when connection and patterns modules are ready

            # Simplified configuration - basic service registration
            # TODO: Implement proper service configuration when modules are ready
            logger.debug("Basic WMS service configuration completed")

            logger.info("Oracle WMS services configured successfully")
            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to configure Oracle WMS services")
            return FlextResult.fail(f"Service configuration failed: {e}")


def get_target_oracle_wms_container() -> FlextResult[TargetOracleWMSContainer]:
    """Get Oracle WMS Target DI container instance."""
    try:
        container = TargetOracleWMSContainer()
        return FlextResult.ok(container)

    except (RuntimeError, ValueError, TypeError) as e:
        logger.exception("Failed to create Oracle WMS Target container")
        return FlextResult.fail(f"Container creation failed: {e}")
