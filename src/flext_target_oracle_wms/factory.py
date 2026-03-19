"""Factory helpers for constructing Oracle WMS Singer targets."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, ClassVar

from flext_core import FlextLogger, FlextModels, r
from pydantic import Field

from flext_target_oracle_wms import t

from .target_client import SingerTargetOracleWMS

logger = FlextLogger(__name__)


class TargetCreationRequest(FlextModels.ArbitraryTypesModel):
    """Input object for target construction."""

    base_url: str
    username: str
    password: str
    environment: str = "development"
    preset: str | None = None
    additional_config: Annotated[Mapping[str, t.Scalar] | None, Field(default=None)]


class MonitoredTargetCreationRequest(TargetCreationRequest):
    """Input object for monitored target creation."""

    monitor_name: str = "oracle_wms_target"


class FlextTargetFactory:
    """Factory for creating configured target instances."""

    PRESETS: ClassVar[dict[str, dict[str, t.Scalar]]] = {
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
        cls, config: Mapping[str, t.Scalar]
    ) -> r[SingerTargetOracleWMS]:
        """Create target from plain dictionary config via Pydantic validation."""
        known_keys = {"base_url", "username", "password", "environment", "preset"}
        additional = {k: v for k, v in config.items() if k not in known_keys}
        try:
            request = TargetCreationRequest.model_validate({
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
            return r[SingerTargetOracleWMS].fail(str(exc))
        return cls.create_target(request)

    @classmethod
    def create_target(
        cls,
        request: TargetCreationRequest,
    ) -> r[SingerTargetOracleWMS]:
        """Create target instance from request object."""
        config: dict[str, t.ContainerValue] = {
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
        return r[SingerTargetOracleWMS].ok(SingerTargetOracleWMS(config))


class FlextTargetMonitoringFactory:
    """Factory wrapper that currently reuses base creation behavior."""

    def __init__(self, monitor_name: str = "oracle_wms_target") -> None:
        """Store monitor metadata for external instrumentation."""
        self.monitor_name = monitor_name

    def create_monitored_target(
        self, request: MonitoredTargetCreationRequest
    ) -> r[SingerTargetOracleWMS]:
        """Create monitored target using base factory."""
        base_request = TargetCreationRequest.model_validate({
            "base_url": request.base_url,
            "username": request.username,
            "password": request.password,
            "environment": request.environment,
            "preset": request.preset,
            "additional_config": request.additional_config,
        })
        return FlextTargetFactory.create_target(base_request)


def create_oracle_wms_target(
    base_url: str,
    username: str,
    password: str,
    environment: str = "development",
    preset: str | None = None,
    **config: t.Scalar,
) -> r[SingerTargetOracleWMS]:
    """Convenience function to create base target instance."""
    request = TargetCreationRequest.model_validate({
        "base_url": base_url,
        "username": username,
        "password": password,
        "environment": environment,
        "preset": preset,
        "additional_config": config,
    })
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
