"""Domain models for target Oracle WMS.

Inherits from FlextMeltanoModels (m.Meltano.*) and FlextOracleWmsModels (m.OracleWms.*).
Defines local TargetOracleWms namespace for target-specific models.
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextModels, r, t
from flext_meltano.models import FlextMeltanoModels
from flext_oracle_wms.wms_models import FlextOracleWmsModels
from pydantic import ConfigDict, Field, SecretStr

from .constants import c


class FlextTargetOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (from FlextMeltanoModels)
        m.OracleWms.*  — WMS entity/API types (from FlextOracleWmsModels)

    Local namespace:
        m.TargetOracleWms.* — target-specific config, result, schema helpers
    """

    class TargetOracleWms:
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""

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

            def validate_business_rules(self) -> r[bool]:
                """Validate basic config business rules."""
                if (
                    self.load_method
                    not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS
                ):
                    return r[bool].fail("Invalid load method")
                if self.batch_size <= 0:
                    return r[bool].fail("Batch size must be positive")
                return r[bool].ok(value=True)

        class WmsTargetResult(FlextModels.ArbitraryTypesModel):
            """Execution summary for the target pipeline."""

            total_records_processed: int = 0
            successful_records: int = 0
            failed_records: int = 0
            error_messages: list[str] = Field(default_factory=list)
            metrics: dict[str, t.JsonValue] = Field(default_factory=dict)

            @property
            def success_rate(self) -> float:
                """Calculate percentage of successful records."""
                if self.total_records_processed == 0:
                    return 0.0
                return (self.successful_records / self.total_records_processed) * 100.0

        class SingerFieldSchema(FlextModels.ArbitraryTypesModel):
            """Typed Singer field schema entry for target-side schema parsing."""

            model_config = ConfigDict(extra="ignore")

            type: str = "string"

        class SingerSchemaProperties(FlextModels.ArbitraryTypesModel):
            """Typed Singer schema properties block for target-side schema parsing."""

            model_config = ConfigDict(extra="ignore")

            properties: dict[
                str,
                FlextTargetOracleWmsModels.TargetOracleWms.SingerFieldSchema,
            ] = Field(default_factory=dict)


m = FlextTargetOracleWmsModels

__all__ = ["FlextTargetOracleWmsModels", "m"]
