"""Domain models for target Oracle WMS.

Inherits from the canonical Meltano models facade and m.
Defines local TargetOracleWms namespace for target-specific models.
"""

from __future__ import annotations

from collections.abc import (
    MutableMapping,
    MutableSequence,
)
from typing import Annotated, Literal

from flext_meltano import m as meltano_m, p, r, t, u
from flext_oracle_wms import m

from flext_target_oracle_wms.constants import c


class FlextTargetOracleWmsModels(meltano_m, m):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (overridden with Container support)
        m.OracleWms.*  — WMS entity/API types (from m)

    Local namespace:
        m.TargetOracleWms.* — target-specific settings, result, schema helpers
    """

    class TargetOracleWms:
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""

        class WmsAuthenticationConfig(meltano_m.ArbitraryTypesModel):
            """Authentication and endpoint settings."""

            base_url: Annotated[
                str, u.Field(description="Oracle WMS REST API base URL.")
            ]
            auth_method: Annotated[
                Literal["oauth2", "basic", "api_key"],
                u.Field(description="WMS authentication method."),
            ] = "oauth2"
            username: Annotated[
                str | None, u.Field(description="Optional authentication username.")
            ] = None
            password: Annotated[
                t.SecretStr | None,
                u.Field(description="Optional authentication password."),
            ] = None
            api_key: Annotated[
                t.SecretStr | None,
                u.Field(description="Optional API key for the selected auth method."),
            ] = None
            company_code: Annotated[str, u.Field(description="WMS company code.")] = (
                "DEFAULT"
            )
            facility_code: Annotated[str, u.Field(description="WMS facility code.")] = (
                "MAIN"
            )

        class WmsTargetConfig(meltano_m.ArbitraryTypesModel):
            """Top-level target configuration model."""

            wms_auth: Annotated[
                FlextTargetOracleWmsModels.TargetOracleWms.WmsAuthenticationConfig,
                u.Field(description="WMS authentication and endpoint settings."),
            ]
            stream_maps: Annotated[
                MutableMapping[str, t.StrMapping],
                u.Field(default_factory=dict, description="Singer stream map configurations."),
            ]
            batch_size: Annotated[
                t.BatchSize,
                u.Field(description="Number of records per batch write."),
            ] = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE
            load_method: Annotated[
                str,
                u.Field(description="Load strategy for writing records to WMS."),
            ] = c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY
            validate_records: Annotated[
                bool,
                u.Field(description="Whether to validate records before writing."),
            ] = True

            def validate_business_rules(self) -> p.Result[bool]:
                """Validate basic settings business rules."""
                if (
                    self.load_method
                    not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS
                ):
                    return r[bool].fail("Invalid load method")
                if self.batch_size <= 0:
                    return r[bool].fail("Batch size must be positive")
                return r[bool].ok(value=True)

            def validate_runtime(self) -> p.Result[bool]:
                """Validate runtime constraints before processing starts."""
                return self.validate_business_rules()

            @classmethod
            def create_config(
                cls,
                overrides: t.JsonMapping | None = None,
            ) -> p.Result[FlextTargetOracleWmsModels.TargetOracleWms.WmsTargetConfig]:
                """Create target settings instance with optional override values."""
                try:
                    data: t.JsonMapping = dict(overrides) if overrides else {}
                    settings = cls.model_validate(data)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
                    return r[
                        FlextTargetOracleWmsModels.TargetOracleWms.WmsTargetConfig
                    ].fail(
                        f"Invalid settings overrides: {exc}",
                    )
                validation = settings.validate_runtime()
                if validation.failure:
                    return r[
                        FlextTargetOracleWmsModels.TargetOracleWms.WmsTargetConfig
                    ].fail(
                        validation.error or "Runtime validation failed",
                    )
                return r[FlextTargetOracleWmsModels.TargetOracleWms.WmsTargetConfig].ok(
                    settings
                )

        class WmsTargetResult(meltano_m.ArbitraryTypesModel):
            """Execution summary for the target pipeline."""

            total_records_processed: Annotated[
                t.NonNegativeInt,
                u.Field(description="Total number of records attempted."),
            ] = 0
            successful_records: Annotated[
                t.NonNegativeInt,
                u.Field(description="Number of records successfully written."),
            ] = 0
            failed_records: Annotated[
                t.NonNegativeInt,
                u.Field(description="Number of records that failed to write."),
            ] = 0
            error_messages: Annotated[
                MutableSequence[str],
                u.Field(default_factory=list, description="List of error messages from failed records."),
            ]
            metrics: Annotated[
                MutableMapping[str, t.JsonValue],
                u.Field(default_factory=dict, description="Aggregate runtime metrics for this pipeline run."),
            ]

            @property
            def success_rate(self) -> float:
                """Calculate percentage of successful records."""
                if self.total_records_processed == 0:
                    return 0.0
                return (
                    float(self.successful_records) / float(self.total_records_processed)
                ) * 100.0

        class SingerFieldSchema(meltano_m.FlexibleModel):
            """Typed Singer field schema entry for target-side schema parsing."""

            type: Annotated[
                str, u.Field(description="JSON schema type descriptor for the field.")
            ] = "string"

        class SingerSchemaProperties(meltano_m.FlexibleModel):
            """Typed Singer schema properties block for target-side schema parsing."""

            properties: Annotated[
                MutableMapping[
                    str,
                    FlextTargetOracleWmsModels.TargetOracleWms.SingerFieldSchema,
                ],
                u.Field(default_factory=dict, description="Singer schema field property definitions."),
            ]

        class TargetCreationRequest(meltano_m.ArbitraryTypesModel):
            """Input object for target construction."""

            base_url: Annotated[
                str, u.Field(description="Oracle WMS REST API base URL.")
            ]
            username: Annotated[
                str, u.Field(description="Username used to authenticate against WMS.")
            ]
            password: Annotated[
                str, u.Field(description="Password used to authenticate against WMS.")
            ]
            environment: Annotated[
                str, u.Field(description="Target environment name.")
            ] = "development"
            preset: Annotated[
                str | None, u.Field(description="Optional preset profile name.")
            ] = None
            additional_config: Annotated[
                t.JsonMapping | None,
                u.Field(default=None, description="Additional environment overrides."),
            ]

        class MonitoredTargetCreationRequest(TargetCreationRequest):
            """Input object for monitored target creation."""

            monitor_name: Annotated[
                str, u.Field(description="Monitoring label for the created target.")
            ] = "oracle_wms_target"


m = FlextTargetOracleWmsModels

__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
