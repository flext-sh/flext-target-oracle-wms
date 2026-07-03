"""Factory helpers for constructing Oracle WMS Singer targets."""

from __future__ import annotations

from typing import ClassVar

from flext_core import r
from flext_target_oracle_wms import c, m, p, t, u

from ._constants import factory


class FlextTargetFactory:
    """Factory for creating configured target instances."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    PRESETS: ClassVar[t.MappingKV[str, t.JsonMapping]] = factory.PRESETS

    @classmethod
    def create_from_config_dict(
        cls,
        settings: t.JsonMapping,
    ) -> p.Result[u.TargetOracleWms.Target]:
        """Create target from plain dictionary settings via Pydantic validation."""
        known_keys = {"base_url", "username", "password", "environment", "preset"}
        additional = {k: v for k, v in settings.items() if k not in known_keys}
        try:
            request = m.TargetOracleWms.TargetCreationRequest.model_validate({
                **settings,
                "additional_config": additional or None,
            })
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[u.TargetOracleWms.Target].fail(str(exc))
        return cls.create_target(request)

    @classmethod
    def create_target(
        cls,
        request: m.TargetOracleWms.TargetCreationRequest,
    ) -> p.Result[u.TargetOracleWms.Target]:
        """Create target instance from validated request."""
        settings: t.MutableJsonMapping = {
            "base_url": request.base_url,
            "username": request.username,
            "password": request.password,
            "environment": request.environment,
        }
        if request.preset is not None and request.preset in factory.PRESETS:
            settings.update(factory.PRESETS[request.preset])
        if request.additional_config is not None:
            settings.update(request.additional_config)
        cls.logger.info("Created Oracle WMS target", environment=request.environment)
        return r[u.TargetOracleWms.Target].ok(u.TargetOracleWms.Target(settings))


class FlextTargetMonitoringFactory:
    """Factory wrapper that currently reuses base creation behavior."""

    def __init__(self, monitor_name: str = "oracle_wms_target") -> None:
        """Store monitor metadata for external instrumentation."""
        self.monitor_name = monitor_name

    def create_monitored_target(
        self,
        request: m.TargetOracleWms.MonitoredTargetCreationRequest,
    ) -> p.Result[u.TargetOracleWms.Target]:
        """Create monitored target using base factory."""
        base_request = m.TargetOracleWms.TargetCreationRequest.model_validate(
            request.model_dump(exclude={"monitor_name"}),
        )
        return FlextTargetFactory.create_target(base_request)

    @staticmethod
    def create_oracle_wms_target(
        **kwargs: t.JsonValue,
    ) -> p.Result[u.TargetOracleWms.Target]:
        """Convenience method to create base target instance."""
        request = m.TargetOracleWms.TargetCreationRequest.model_validate(kwargs)
        return FlextTargetFactory.create_target(request)

    @staticmethod
    def create_monitored_oracle_wms_target(
        request: m.TargetOracleWms.MonitoredTargetCreationRequest,
    ) -> p.Result[u.TargetOracleWms.Target]:
        """Convenience method to create monitored target instance."""
        factory = FlextTargetMonitoringFactory(request.monitor_name)
        return factory.create_monitored_target(request)


__all__: list[str] = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
]
