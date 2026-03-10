"""Settings model for target Oracle WMS runtime."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, t


def create_settings(
    overrides: Mapping[str, t.ContainerValue] | None = None,
) -> FlextResult[FlextTargetOracleWmsSettings]:  # noqa: F821
    """Create settings instance with optional override values."""
    try:
        data: dict[str, t.ContainerValue] = dict(overrides) if overrides else {}
        settings = FlextTargetOracleWmsSettings.model_validate(data)  # noqa: F821
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ) as exc:
        return FlextResult[FlextTargetOracleWmsSettings].fail(  # noqa: F821
            f"Invalid settings overrides: {exc}"
        )
    validation = settings.validate_runtime()
    if validation.is_failure:
        return FlextResult[FlextTargetOracleWmsSettings].fail(  # noqa: F821
            validation.error or "Runtime validation failed"
        )
    return FlextResult[FlextTargetOracleWmsSettings].ok(settings)  # noqa: F821


__all__ = ["FlextTargetOracleWmsSettings", "create_settings"]  # noqa: F822
