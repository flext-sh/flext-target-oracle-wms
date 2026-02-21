"""Factory helpers for constructing Oracle WMS Singer targets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from flext_core import FlextLogger, r, t

from .target_client import SingerTargetOracleWMS

logger = FlextLogger(__name__)


@dataclass
class TargetCreationRequest:
    """Input object for target creation."""

    base_url: str
    username: str
    password: str
    environment: str = "development"
    preset: str | None = None
    additional_config: dict[str, t.GeneralValueType] | None = None


@dataclass
class MonitoredTargetCreationRequest(TargetCreationRequest):
    """Input object for monitored target creation."""

    monitor_name: str = "oracle_wms_target"


class FlextTargetFactory:
    """Factory for creating configured target instances."""

    PRESETS: ClassVar[dict[str, dict[str, t.GeneralValueType]]] = {
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
    def create_target(
        cls,
        request: TargetCreationRequest,
    ) -> r[SingerTargetOracleWMS]:
        """Create target instance from request object."""
        config: dict[str, t.GeneralValueType] = {
            "base_url": request.base_url,
            "username": request.username,
            "password": request.password,
            "environment": request.environment,
        }
        if request.preset is not None and request.preset in cls.PRESETS:
            config.update(cls.PRESETS[request.preset])
        if request.additional_config is not None:
            config.update(request.additional_config)
        logger.info(
            "Created Oracle WMS target", extra={"environment": request.environment}
        )
        return r[SingerTargetOracleWMS].ok(SingerTargetOracleWMS(config))

    @classmethod
    def create_from_config_dict(
        cls,
        config: dict[str, t.GeneralValueType],
    ) -> r[SingerTargetOracleWMS]:
        """Create target from plain dictionary config."""
        base_url = config.get("base_url")
        username = config.get("username")
        password = config.get("password")
        if not isinstance(base_url, str):
            return r[SingerTargetOracleWMS].fail("base_url must be a string")
        if not isinstance(username, str):
            return r[SingerTargetOracleWMS].fail("username must be a string")
        if not isinstance(password, str):
            return r[SingerTargetOracleWMS].fail("password must be a string")

        environment_value = config.get("environment", "development")
        if isinstance(environment_value, str):
            environment = environment_value
        else:
            environment = "development"

        preset_value = config.get("preset")
        preset = preset_value if isinstance(preset_value, str) else None

        additional = {
            key: value
            for key, value in config.items()
            if key not in {"base_url", "username", "password", "environment", "preset"}
        }
        request = TargetCreationRequest(
            base_url=base_url,
            username=username,
            password=password,
            environment=environment,
            preset=preset,
            additional_config=additional,
        )
        return cls.create_target(request)


class FlextTargetMonitoringFactory:
    """Factory wrapper that currently reuses base creation behavior."""

    def __init__(self, monitor_name: str = "oracle_wms_target") -> None:
        """Store monitor metadata for external instrumentation."""
        self.monitor_name = monitor_name

    def create_monitored_target(
        self,
        request: MonitoredTargetCreationRequest,
    ) -> r[SingerTargetOracleWMS]:
        """Create monitored target using base factory."""
        base_request = TargetCreationRequest(
            base_url=request.base_url,
            username=request.username,
            password=request.password,
            environment=request.environment,
            preset=request.preset,
            additional_config=request.additional_config,
        )
        return FlextTargetFactory.create_target(base_request)


def create_oracle_wms_target(
    base_url: str,
    username: str,
    password: str,
    environment: str = "development",
    preset: str | None = None,
    **config: t.GeneralValueType,
) -> r[SingerTargetOracleWMS]:
    """Convenience function to create base target instance."""
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
    request: MonitoredTargetCreationRequest,
) -> r[SingerTargetOracleWMS]:
    """Convenience function to create monitored target instance."""
    factory = FlextTargetMonitoringFactory(request.monitor_name)
    return factory.create_monitored_target(request)


__all__ = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "MonitoredTargetCreationRequest",
    "TargetCreationRequest",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
]
