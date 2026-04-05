"""Settings model for target Oracle WMS runtime."""

from __future__ import annotations

from flext_core import r
from flext_target_oracle_wms import c, m, t


class FlextTargetOracleWmsSettings(m.TargetOracleWms.WmsTargetConfig):
    """Validated settings model used by target runtime and factory helpers."""

    def validate_runtime(self) -> r[bool]:
        """Validate runtime constraints before processing starts."""
        return self.validate_business_rules()

    @classmethod
    def create_settings(
        cls,
        overrides: t.ContainerValueMapping | None = None,
    ) -> r[FlextTargetOracleWmsSettings]:
        """Create settings instance with optional override values."""
        try:
            data: t.ContainerValueMapping = dict(overrides) if overrides else {}
            settings = FlextTargetOracleWmsSettings.model_validate(data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[FlextTargetOracleWmsSettings].fail(
                f"Invalid settings overrides: {exc}",
            )
        validation = settings.validate_runtime()
        if validation.is_failure:
            return r[FlextTargetOracleWmsSettings].fail(
                validation.error or "Runtime validation failed",
            )
        return r[FlextTargetOracleWmsSettings].ok(settings)


__all__ = ["FlextTargetOracleWmsSettings"]
