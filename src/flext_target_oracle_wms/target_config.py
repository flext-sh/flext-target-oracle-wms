"""Settings model for target Oracle WMS runtime."""

from __future__ import annotations

from flext_core import r
from flext_target_oracle_wms import c, m, t


class FlextTargetOracleWmsTargetConfig(m.TargetOracleWms.WmsTargetConfig):
    """Validated target settings used by target runtime and factory helpers."""

    def validate_runtime(self) -> r[bool]:
        """Validate runtime constraints before processing starts."""
        return self.validate_business_rules()

    @classmethod
    def create_config(
        cls,
        overrides: t.ContainerValueMapping | None = None,
    ) -> r[FlextTargetOracleWmsTargetConfig]:
        """Create target settings instance with optional override values."""
        try:
            data: t.ContainerValueMapping = dict(overrides) if overrides else {}
            settings = cls.model_validate(data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[FlextTargetOracleWmsTargetConfig].fail(
                f"Invalid settings overrides: {exc}",
            )
        validation = settings.validate_runtime()
        if validation.failure:
            return r[FlextTargetOracleWmsTargetConfig].fail(
                validation.error or "Runtime validation failed",
            )
        return r[FlextTargetOracleWmsTargetConfig].ok(settings)


__all__: list[str] = ["FlextTargetOracleWmsTargetConfig"]
