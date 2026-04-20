"""Domain models for target Oracle WMS.

Inherits from FlextMeltanoModels (m.Meltano.*) and FlextOracleWmsModels (m.OracleWms.*).
Defines local TargetOracleWms namespace for target-specific models.
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)
from typing import Annotated, ClassVar, Literal

from flext_meltano import FlextMeltanoModels, m, p, r, t, u
from flext_oracle_wms import FlextOracleWmsModels
from flext_target_oracle_wms import c


class FlextTargetOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (overridden with ContainerValue support)
        m.OracleWms.*  — WMS entity/API types (from FlextOracleWmsModels)

    Local namespace:
        m.TargetOracleWms.* — target-specific settings, result, schema helpers
    """

    class TargetOracleWms:
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""

        class WmsAuthenticationConfig(FlextMeltanoModels.ArbitraryTypesModel):
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

        class WmsTargetConfig(FlextMeltanoModels.ArbitraryTypesModel):
            """Top-level target configuration model."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            wms_auth: FlextTargetOracleWmsModels.TargetOracleWms.WmsAuthenticationConfig
            stream_maps: Mapping[str, t.StrMapping] = u.Field(default_factory=dict)
            batch_size: t.BatchSize = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE
            load_method: str = c.TargetOracleWms.LoadMethods.APPEND_ONLY
            validate_records: bool = True

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

        class WmsTargetResult(FlextMeltanoModels.ArbitraryTypesModel):
            """Execution summary for the target pipeline."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            total_records_processed: t.NonNegativeInt = 0
            successful_records: t.NonNegativeInt = 0
            failed_records: t.NonNegativeInt = 0
            error_messages: t.StrSequence = u.Field(default_factory=list)
            metrics: t.ConfigurationMapping = u.Field(default_factory=dict)

            @property
            def success_rate(self) -> float:
                """Calculate percentage of successful records."""
                if self.total_records_processed == 0:
                    return 0.0
                return (self.successful_records / self.total_records_processed) * 100.0

        class SingerFieldSchema(FlextMeltanoModels.ArbitraryTypesModel):
            """Typed Singer field schema entry for target-side schema parsing."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")

            type: Annotated[
                str, u.Field(description="JSON schema type descriptor for the field.")
            ] = "string"

        class SingerSchemaProperties(FlextMeltanoModels.ArbitraryTypesModel):
            """Typed Singer schema properties block for target-side schema parsing."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(extra="ignore")

            properties: Mapping[
                str,
                FlextTargetOracleWmsModels.TargetOracleWms.SingerFieldSchema,
            ] = u.Field(default_factory=dict)

        class TargetCreationRequest(FlextMeltanoModels.ArbitraryTypesModel):
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
                t.ConfigurationMapping | None,
                u.Field(default=None, description="Additional environment overrides."),
            ]

        class MonitoredTargetCreationRequest(TargetCreationRequest):
            """Input object for monitored target creation."""

            monitor_name: Annotated[
                str, u.Field(description="Monitoring label for the created target.")
            ] = "oracle_wms_target"

        class SingerSchemaMessage(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer SCHEMA message with ContainerValue schema support."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                populate_by_name=True,
            )

            type: Annotated[
                Literal["SCHEMA"], u.Field(description="Singer message discriminator")
            ] = "SCHEMA"
            stream: Annotated[
                t.NonEmptyStr,
                u.Field(description="Singer stream name"),
            ]
            schema_definition: Annotated[
                t.ContainerValueMapping,
                u.Field(
                    alias="schema",
                    serialization_alias="schema",
                    validation_alias="schema",
                    description="Singer JSON schema payload",
                ),
            ]
            key_properties: Annotated[
                t.StrSequence,
                u.Field(
                    description="Singer stream key properties",
                ),
            ] = u.Field(default_factory=list)
            bookmark_properties: Annotated[
                t.StrSequence,
                u.Field(
                    description="Singer bookmark columns for incremental replication",
                ),
            ] = u.Field(default_factory=list)

        class SingerRecordMessage(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer RECORD message with ContainerValue record support."""

            type: Annotated[
                Literal["RECORD"], u.Field(description="Singer message discriminator")
            ] = "RECORD"
            stream: Annotated[
                str,
                u.Field(description="Singer stream name"),
            ]
            record: Annotated[
                t.ContainerValueMapping,
                u.Field(description="Singer record payload"),
            ]
            time_extracted: Annotated[
                str | None,
                u.Field(
                    description="ISO 8601 timestamp when the record was extracted",
                ),
            ] = None
            version: Annotated[
                int | None,
                u.Field(
                    description="Stream version for activate_version protocol",
                ),
            ] = None

        class SingerCatalogEntry(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer catalog entry with ContainerValue schema support."""

            _flext_enforcement_exempt: ClassVar[bool] = True

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                populate_by_name=True,
            )

            tap_stream_id: Annotated[
                str,
                u.Field(description="Tap stream identifier"),
            ]
            stream: Annotated[
                str,
                u.Field(description="Singer stream name"),
            ]
            schema_definition: Annotated[
                t.ContainerValueMapping,
                u.Field(
                    alias="schema",
                    serialization_alias="schema",
                    validation_alias="schema",
                    description="Singer stream schema payload",
                ),
            ]
            key_properties: Annotated[
                t.StrSequence,
                u.Field(
                    description="Singer stream key properties",
                ),
            ] = u.Field(default_factory=list)
            table_name: str | None = None


m = FlextTargetOracleWmsModels

__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
