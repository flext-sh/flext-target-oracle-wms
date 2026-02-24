"""Settings model for target Oracle WMS runtime."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextResult, FlextSettings, t
from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .constants import c


class FlextTargetOracleWmsSettings(FlextSettings):
    """Runtime settings for Singer target Oracle WMS."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_",
        case_sensitive=False,
        extra="ignore",
    )

    base_url: str = Field(default="https://invalid.wms.ocs.oraclecloud.com")
    username: str = Field(default="oracle")
    password: str = Field(default="oracle")
    environment: str = Field(default="development")
    timeout: int = Field(default=c.TargetOracleWms.OracleWms.DEFAULT_TIMEOUT)
    max_retries: int = Field(default=c.TargetOracleWms.OracleWms.DEFAULT_MAX_RETRIES)
    verify_ssl: bool = Field(default=True)
    enable_logging: bool = Field(default=True)
    batch_size: int = Field(default=c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE)
    load_method: str = Field(default=c.TargetOracleWms.LoadMethods.APPEND_ONLY)

    def validate_runtime(self) -> FlextResult[bool]:
        """Validate core runtime invariants."""
        if self.load_method not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS:
            return FlextResult[bool].fail("Invalid load_method")
        if self.batch_size <= 0:
            return FlextResult[bool].fail("batch_size must be positive")
        return FlextResult[bool].ok(value=True)

    def to_target_config(self) -> Mapping[str, t.GeneralValueType]:
        """Export settings as target configuration dictionary."""
        return {
            "base_url": self.base_url,
            "username": self.username,
            "password": self.password,
            "environment": self.environment,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "verify_ssl": self.verify_ssl,
            "enable_logging": self.enable_logging,
            "batch_size": self.batch_size,
            "load_method": self.load_method,
        }


def create_settings(
    overrides: dict[str, t.GeneralValueType] | None = None,
) -> FlextResult[FlextTargetOracleWmsSettings]:
    """Create settings instance with optional override values."""
    try:
        settings = FlextTargetOracleWmsSettings(**(overrides or {}))
    except Exception as exc:
        return FlextResult[FlextTargetOracleWmsSettings].fail(
            f"Invalid settings overrides: {exc}",
        )

    validation = settings.validate_runtime()
    if validation.is_failure:
        return FlextResult[FlextTargetOracleWmsSettings].fail(
            validation.error or "Runtime validation failed",
        )
    return FlextResult[FlextTargetOracleWmsSettings].ok(settings)


__all__ = ["FlextTargetOracleWmsSettings", "create_settings"]
