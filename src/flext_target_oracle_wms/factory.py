"""Factory helpers for constructing Oracle WMS Singer targets."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping
from typing import ClassVar

from flext_core import FlextLogger, r, t

from .models import m
from .target_client import FlextTargetOracleWms

logger = FlextLogger(__name__)


class FlextTargetFactory:
    """Factory for creating configured target instances."""

    PRESETS: ClassVar[Mapping[str, t.ConfigurationMapping]] = {
        "development": {
            "batch_size": 100,
            "timeout": 30,
            "max_retries": 3,
            "verify_ssl": False,
            "enable_logging": True,
        },
        "production": {
            "batch_size": 1000,
            "timeout": 120,
            "max_retries": 10,
            "verify_ssl": True,
            "enable_logging": True,
        },
        "testing": {
            "batch_size": 10,
            "timeout": 15,
            "max_retries": 1,
            "verify_ssl": False,
            "enable_logging": False,
        },
    }

    @classmethod
    def create_from_config_dict(
        cls, config: t.ConfigurationMapping
    ) -> r[FlextTargetOracleWms]:
        """Create target from plain dictionary config via Pydantic validation."""
        known_keys = {"base_url", "username", "password", "environment", "preset"}
        additional = {k: v for k, v in config.items() if k not in known_keys}
        try:
            request = m.TargetOracleWms.TargetCreationRequest.model_validate({
                **config,
                "additional_config": additional or None,
            })
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as exc:
            return r[FlextTargetOracleWms].fail(str(exc))
        return cls.create_target(request)

    @classmethod
    def create_target(
        cls,
        request: m.TargetOracleWms.TargetCreationRequest,
    ) -> r[FlextTargetOracleWms]:
        """Create target instance from validated request."""
        config: MutableMapping[str, t.ContainerValue] = {
            "base_url": request.base_url,
            "username": request.username,
            "password": request.password,
            "environment": request.environment,
        }
        if request.preset is not None and request.preset in cls.PRESETS:
            config.update(cls.PRESETS[request.preset])
        if request.additional_config is not None:
            config.update(request.additional_config)
        logger.info("Created Oracle WMS target", environment=request.environment)
        return r[FlextTargetOracleWms].ok(FlextTargetOracleWms(config))


class FlextTargetMonitoringFactory:
    """Factory wrapper that currently reuses base creation behavior."""

    def __init__(self, monitor_name: str = "oracle_wms_target") -> None:
        """Store monitor metadata for external instrumentation."""
        self.monitor_name = monitor_name

    def create_monitored_target(
        self, request: m.TargetOracleWms.MonitoredTargetCreationRequest
    ) -> r[FlextTargetOracleWms]:
        """Create monitored target using base factory."""
        base_request = m.TargetOracleWms.TargetCreationRequest.model_validate({
            "base_url": request.base_url,
            "username": request.username,
            "password": request.password,
            "environment": request.environment,
            "preset": request.preset,
            "additional_config": request.additional_config,
        })
        return FlextTargetFactory.create_target(base_request)

    @staticmethod
    def create_oracle_wms_target(
        base_url: str,
        username: str,
        password: str,
        environment: str = "development",
        preset: str | None = None,
        **config: t.Scalar,
    ) -> r[FlextTargetOracleWms]:
        """Convenience method to create base target instance."""
        request = m.TargetOracleWms.TargetCreationRequest.model_validate({
            "base_url": base_url,
            "username": username,
            "password": password,
            "environment": environment,
            "preset": preset,
            "additional_config": config,
        })
        return FlextTargetFactory.create_target(request)

    @staticmethod
    def create_monitored_oracle_wms_target(
        request: m.TargetOracleWms.MonitoredTargetCreationRequest,
    ) -> r[FlextTargetOracleWms]:
        """Convenience method to create monitored target instance."""
        factory = FlextTargetMonitoringFactory(request.monitor_name)
        return factory.create_monitored_target(request)


# Module-level aliases for backward compatibility
def create_oracle_wms_target(
    base_url: str,
    username: str,
    password: str,
    environment: str = "development",
    preset: str | None = None,
    **config: t.Scalar,
) -> r[FlextTargetOracleWms]:
    """Convenience function to create base target instance."""
    return FlextTargetFactory.create_oracle_wms_target(
        base_url, username, password, environment, preset, **config
    )


def create_monitored_oracle_wms_target(
    request: m.TargetOracleWms.MonitoredTargetCreationRequest,
) -> r[FlextTargetOracleWms]:
    """Convenience function to create monitored target instance."""
    return FlextTargetFactory.create_monitored_oracle_wms_target(request)


__all__ = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
]
