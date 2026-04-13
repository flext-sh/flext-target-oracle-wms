"""Domain models for target Oracle WMS.

Inherits from FlextMeltanoModels (m.Meltano.*) and FlextOracleWmsModels (m.OracleWms.*).
Defines local TargetOracleWms namespace for target-specific models.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Annotated, ClassVar, Literal

from pydantic import ConfigDict, Field, SecretStr

from flext_core import p, r
from flext_meltano import FlextMeltanoModels
from flext_oracle_wms import FlextOracleWmsModels
from flext_target_oracle_wms import c, t


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

            base_url: str
            auth_method: Literal["oauth2", "basic", "api_key"] = "oauth2"
            username: str | None = None
            password: SecretStr | None = None
            api_key: SecretStr | None = None
            company_code: str = "DEFAULT"
            facility_code: str = "MAIN"

        class WmsTargetConfig(FlextMeltanoModels.ArbitraryTypesModel):
            """Top-level target configuration model."""

            wms_auth: FlextTargetOracleWmsModels.TargetOracleWms.WmsAuthenticationConfig
            stream_maps: Mapping[str, t.StrMapping] = Field(default_factory=dict)
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

            total_records_processed: t.NonNegativeInt = 0
            successful_records: t.NonNegativeInt = 0
            failed_records: t.NonNegativeInt = 0
            error_messages: t.StrSequence = Field(default_factory=list)
            metrics: t.ConfigurationMapping = Field(default_factory=dict)

            @property
            def success_rate(self) -> float:
                """Calculate percentage of successful records."""
                if self.total_records_processed == 0:
                    return 0.0
                return (self.successful_records / self.total_records_processed) * 100.0

        class SingerFieldSchema(FlextMeltanoModels.ArbitraryTypesModel):
            """Typed Singer field schema entry for target-side schema parsing."""

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

            type: str = "string"

        class SingerSchemaProperties(FlextMeltanoModels.ArbitraryTypesModel):
            """Typed Singer schema properties block for target-side schema parsing."""

            model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

            properties: Mapping[
                str,
                FlextTargetOracleWmsModels.TargetOracleWms.SingerFieldSchema,
            ] = Field(default_factory=dict)

        class TargetCreationRequest(FlextMeltanoModels.ArbitraryTypesModel):
            """Input object for target construction."""

            base_url: str
            username: str
            password: str
            environment: str = "development"
            preset: str | None = None
            additional_config: Annotated[
                t.ConfigurationMapping | None,
                Field(default=None),
            ]

        class MonitoredTargetCreationRequest(TargetCreationRequest):
            """Input object for monitored target creation."""

            monitor_name: str = "oracle_wms_target"

        class SingerSchemaMessage(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer SCHEMA message with ContainerValue schema support."""

            model_config: ClassVar[ConfigDict] = ConfigDict(
                populate_by_name=True,
            )

            type: Annotated[
                Literal["SCHEMA"],
                Field(default="SCHEMA", description="Singer message discriminator"),
            ]
            stream: Annotated[
                t.NonEmptyStr,
                Field(description="Singer stream name"),
            ]
            schema_definition: Annotated[
                t.ContainerValueMapping,
                Field(
                    alias="schema",
                    serialization_alias="schema",
                    validation_alias="schema",
                    description="Singer JSON schema payload",
                ),
            ]
            key_properties: Annotated[
                t.StrSequence,
                Field(
                    description="Singer stream key properties",
                ),
            ] = Field(default_factory=list)
            bookmark_properties: Annotated[
                t.StrSequence,
                Field(
                    description="Singer bookmark columns for incremental replication",
                ),
            ] = Field(default_factory=list)

        class SingerRecordMessage(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer RECORD message with ContainerValue record support."""

            type: Annotated[
                Literal["RECORD"],
                Field(default="RECORD", description="Singer message discriminator"),
            ]
            stream: Annotated[
                str,
                Field(description="Singer stream name"),
            ]
            record: Annotated[
                t.ContainerValueMapping,
                Field(description="Singer record payload"),
            ]
            time_extracted: Annotated[
                str | None,
                Field(
                    default=None,
                    description="ISO 8601 timestamp when the record was extracted",
                ),
            ]
            version: Annotated[
                int | None,
                Field(
                    default=None,
                    description="Stream version for activate_version protocol",
                ),
            ]

        class SingerCatalogEntry(FlextMeltanoModels.ArbitraryTypesModel):
            """Singer catalog entry with ContainerValue schema support."""

            model_config: ClassVar[ConfigDict] = ConfigDict(
                populate_by_name=True,
            )

            tap_stream_id: Annotated[
                str,
                Field(description="Tap stream identifier"),
            ]
            stream: Annotated[
                str,
                Field(description="Singer stream name"),
            ]
            schema_definition: Annotated[
                t.ContainerValueMapping,
                Field(
                    alias="schema",
                    serialization_alias="schema",
                    validation_alias="schema",
                    description="Singer stream schema payload",
                ),
            ]
            key_properties: Annotated[
                t.StrSequence,
                Field(
                    description="Singer stream key properties",
                ),
            ] = Field(default_factory=list)
            table_name: str | None = None


m = FlextTargetOracleWmsModels

__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
