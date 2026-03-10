"""Settings model for target Oracle WMS runtime."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t

from .models import m


class FlextTargetOracleWmsSettings(m.TargetOracleWms.WmsTargetConfig):
    """Validated settings model used by target runtime and factory helpers."""

    def validate_runtime(self) -> FlextResult[bool]:
        """Validate runtime constraints before processing starts."""
        return self.validate_business_rules()


def create_settings(
    overrides: Mapping[str, t.ContainerValue] | None = None,
) -> FlextResult[FlextTargetOracleWmsSettings]:
    """Create settings instance with optional override values."""
    try:
        data: dict[str, t.ContainerValue] = dict(overrides) if overrides else {}
        settings = FlextTargetOracleWmsSettings.model_validate(data)
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ) as exc:
        return FlextResult[FlextTargetOracleWmsSettings].fail(
            f"Invalid settings overrides: {exc}"
        )
    validation = settings.validate_runtime()
    if validation.is_failure:
        return FlextResult[FlextTargetOracleWmsSettings].fail(
            validation.error or "Runtime validation failed"
        )
    return FlextResult[FlextTargetOracleWmsSettings].ok(settings)


__all__ = ["FlextTargetOracleWmsSettings", "create_settings"]
