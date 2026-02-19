"""Domain models for target Oracle WMS."""

from __future__ import annotations

from typing import Literal

from flext_core import FlextModels, FlextResult, FlextTypes as t
from pydantic import Field, SecretStr

from .constants import c


class FlextTargetOracleWmsModels(FlextModels):
    """Pydantic model namespace for target Oracle WMS objects."""

    class TargetOracleWms:
        """Target Oracle WMS model namespace."""

        class WmsAuthenticationConfig(FlextModels.ArbitraryTypesModel):
            """Authentication and endpoint settings."""

            base_url: str
            auth_method: Literal["oauth2", "basic", "api_key"] = "oauth2"
            username: str | None = None
            password: SecretStr | None = None
            api_key: SecretStr | None = None
            company_code: str = "DEFAULT"
            facility_code: str = "MAIN"

        class WmsTargetConfig(FlextModels.ArbitraryTypesModel):
            """Top-level target configuration model."""

            wms_auth: FlextTargetOracleWmsModels.TargetOracleWms.WmsAuthenticationConfig
            stream_maps: dict[str, dict[str, str]] = Field(default_factory=dict)
            batch_size: int = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE
            load_method: str = c.TargetOracleWms.LoadMethods.APPEND_ONLY
            validate_records: bool = True

            def validate_business_rules(self) -> FlextResult[bool]:
                """Validate basic config business rules."""
                if (
                    self.load_method
                    not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS
                ):
                    return FlextResult[bool].fail("Invalid load method")
                if self.batch_size <= 0:
                    return FlextResult[bool].fail("Batch size must be positive")
                return FlextResult[bool].ok(value=True)

        class WmsTargetResult(FlextModels.ArbitraryTypesModel):
            """Execution summary for the target pipeline."""

            total_records_processed: int = 0
            successful_records: int = 0
            failed_records: int = 0
            error_messages: list[str] = Field(default_factory=list)
            metrics: dict[str, t.GeneralValueType] = Field(default_factory=dict)

            @property
            def success_rate(self) -> float:
                """Calculate percentage of successful records."""
                if self.total_records_processed == 0:
                    return 0.0
                return (self.successful_records / self.total_records_processed) * 100.0


m = FlextTargetOracleWmsModels
m_target_oracle_wms = FlextTargetOracleWmsModels

__all__ = ["FlextTargetOracleWmsModels", "m", "m_target_oracle_wms"]
