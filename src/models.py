"""Enhanced Oracle WMS Target models extending FlextModels.

Contains all Pydantic models for Oracle WMS target operations following
FLEXT standards with enhanced Pydantic 2.11 features and comprehensive validation.
"""

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path
from typing import Literal, Self

from pydantic import (
    ConfigDict,
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
    model_validator,
)

from flext_core import FlextConstants, FlextModels, FlextResult

# Re-export for convenience
__all__ = ["FlextTargetOracleWmsModels"]


class FlextTargetOracleWmsModels(FlextModels):
    """Enhanced Oracle WMS Target models extending FlextModels.

    Contains all Pydantic models for Oracle WMS target operations following
    FLEXT standards with enhanced Pydantic 2.11 features and comprehensive validation.
    """

    # Enhanced base models with Pydantic 2.11 features
    class _BaseTargetModel(FlextModels.ArbitraryTypesModel):
        """Base target model with enhanced Pydantic 2.11 configuration."""

        model_config = ConfigDict(
            # Enhanced Pydantic 2.11 features
            validate_assignment=True,
            use_enum_values=True,
            arbitrary_types_allowed=True,
            validate_return=True,
            ser_json_timedelta="iso8601",
            ser_json_bytes="base64",
            serialize_by_alias=True,
            populate_by_name=True,
            str_strip_whitespace=True,
            defer_build=False,
            coerce_numbers_to_str=False,
            validate_default=True,
            # Custom encoders for complex types
            json_encoders={
                Path: str,
                datetime: lambda dt: dt.isoformat(),
                Decimal: float,
            },
        )

    # Oracle WMS Target Record Models
    class TargetRecord(_BaseTargetModel):
        """Enhanced Oracle WMS target record model with comprehensive validation."""

        record_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Unique record identifier",
            min_length=1,
            max_length=255,
        )
        table_name: str = Field(
            description="Target table name",
            min_length=1,
            max_length=128,
        )
        schema_name: str = Field(
            description="Target schema name",
            min_length=1,
            max_length=128,
        )
        data: dict[str, object] = Field(
            description="Record data",
            min_length=1,
        )
        operation: Literal["INSERT", "UPDATE", "DELETE", "UPSERT"] = Field(
            default="INSERT",
            description="Database operation type",
        )
        timestamp: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Record timestamp",
        )
        batch_id: str | None = Field(
            default=None,
            description="Batch identifier",
        )
        sequence_number: int = Field(
            default=0,
            description="Sequence number within batch",
            ge=0,
        )
        metadata: dict[str, object] = Field(
            default_factory=dict,
            description="Record metadata",
        )

        @field_validator("table_name")
        @classmethod
        def validate_table_name(cls, v: str) -> str:
            """Validate table name format."""
            if not v.replace("_", "").replace("-", "").isalnum():
                msg = "Table name must contain only alphanumeric characters, underscores, and hyphens"
                raise ValueError(msg)
            return v.upper()

        @field_validator("schema_name")
        @classmethod
        def validate_schema_name(cls, v: str) -> str:
            """Validate schema name format."""
            if not v.replace("_", "").replace("-", "").isalnum():
                msg = "Schema name must contain only alphanumeric characters, underscores, and hyphens"
                raise ValueError(msg)
            return v.upper()

        @field_validator("data")
        @classmethod
        def validate_data(cls, v: dict[str, object]) -> dict[str, object]:
            """Validate record data."""
            if not v:
                msg = "Record data cannot be empty"
                raise ValueError(msg)

            # Check for dangerous keys
            dangerous_keys = {"DROP", "DELETE", "TRUNCATE", "ALTER", "CREATE"}
            for key in v:
                if any(dangerous in key.upper() for dangerous in dangerous_keys):
                    msg = f"Data key contains potentially dangerous SQL keywords: {key}"
                    raise ValueError(msg)

            return v

        @computed_field
        def full_table_name(self) -> str:
            """Get full table name with schema."""
            return f"{self.schema_name}.{self.table_name}"

        @computed_field
        def data_size_bytes(self) -> int:
            """Calculate data size in bytes."""
            try:
                serialized = json.dumps(self.data, default=str)
                return len(serialized.encode("utf-8"))
            except Exception:
                return 0

        @computed_field
        def is_insert_operation(self) -> bool:
            """Check if this is an insert operation."""
            return self.operation == "INSERT"

        @computed_field
        def is_update_operation(self) -> bool:
            """Check if this is an update operation."""
            return self.operation == "UPDATE"

        @computed_field
        def is_delete_operation(self) -> bool:
            """Check if this is a delete operation."""
            return self.operation == "DELETE"

        @computed_field
        def is_upsert_operation(self) -> bool:
            """Check if this is an upsert operation."""
            return self.operation == "UPSERT"

    class TargetBatch(_BaseTargetModel):
        """Enhanced Oracle WMS target batch model with comprehensive tracking."""

        batch_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Unique batch identifier",
            min_length=1,
            max_length=255,
        )
        records: list[FlextTargetOracleWmsModels.TargetRecord] = Field(
            description="Batch records",
            min_length=1,
        )
        batch_size: int = Field(
            description="Number of records in batch",
            ge=1,
        )
        table_name: str = Field(
            description="Target table name",
            min_length=1,
            max_length=128,
        )
        schema_name: str = Field(
            description="Target schema name",
            min_length=1,
            max_length=128,
        )
        load_method: str = Field(
            default="APPEND_ONLY",
            description="Data load method",
        )
        created_at: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Batch creation timestamp",
        )
        status: Literal["PENDING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED"] = (
            Field(
                default="PENDING",
                description="Batch processing status",
            )
        )
        error_message: str | None = Field(
            default=None,
            description="Error message if batch failed",
        )
        processing_started_at: datetime | None = None
        processing_completed_at: datetime | None = None
        records_processed: int = Field(default=0, ge=0)
        records_failed: int = Field(default=0, ge=0)

        @field_validator("batch_size")
        @classmethod
        def validate_batch_size(cls, v: int, info: ValidationInfo) -> int:
            """Validate batch size matches actual records count."""
            if "records" in info.data and v != len(info.data["records"]):
                msg = "Batch size must match actual records count"
                raise ValueError(msg)
            return v

        @field_validator("load_method")
        @classmethod
        def validate_load_method(cls, v: str) -> str:
            """Validate load method."""
            valid_methods = {
                "APPEND_ONLY",
                "UPSERT",
                "REPLACE",
                "MERGE",
                "TRUNCATE_INSERT",
            }
            if v.upper() not in valid_methods:
                msg = f"Invalid load_method: {v}. Valid methods: {valid_methods}"
                raise ValueError(msg)
            return v.upper()

        @model_validator(mode="after")
        def validate_batch_consistency(self) -> Self:
            """Validate batch consistency."""
            # Check that all records have the same table and schema
            if self.records:
                first_record = self.records[0]
                for record in self.records[1:]:
                    if record.table_name != first_record.table_name:
                        msg = "All records in batch must have the same table name"
                        raise ValueError(msg)
                    if record.schema_name != first_record.schema_name:
                        msg = "All records in batch must have the same schema name"
                        raise ValueError(msg)

            return self

        @computed_field
        def total_data_size_bytes(self) -> int:
            """Calculate total data size in bytes."""
            return sum(record.data_size_bytes for record in self.records)

        @computed_field
        def total_data_size_kb(self) -> float:
            """Calculate total data size in kilobytes."""
            return self.total_data_size_bytes / 1024.0

        @computed_field
        def processing_duration_seconds(self) -> float | None:
            """Calculate processing duration in seconds."""
            if self.processing_started_at and self.processing_completed_at:
                return (
                    self.processing_completed_at - self.processing_started_at
                ).total_seconds()
            return None

        @computed_field
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            total = self.records_processed + self.records_failed
            if total == 0:
                return 0.0
            return (self.records_processed / total) * 100.0

        @computed_field
        def is_completed(self) -> bool:
            """Check if batch is completed."""
            return self.status == "COMPLETED"

        @computed_field
        def is_failed(self) -> bool:
            """Check if batch failed."""
            return self.status == "FAILED"

        @computed_field
        def is_processing(self) -> bool:
            """Check if batch is currently processing."""
            return self.status == "PROCESSING"

        def start_processing(self) -> None:
            """Start batch processing."""
            self.status = "PROCESSING"
            self.processing_started_at = datetime.now(UTC)

        def complete_processing(
            self, records_processed: int = 0, records_failed: int = 0
        ) -> None:
            """Complete batch processing."""
            self.status = "COMPLETED"
            self.processing_completed_at = datetime.now(UTC)
            self.records_processed = records_processed
            self.records_failed = records_failed

        def fail_processing(self, error_message: str) -> None:
            """Fail batch processing."""
            self.status = "FAILED"
            self.processing_completed_at = datetime.now(UTC)
            self.error_message = error_message

        def cancel_processing(self) -> None:
            """Cancel batch processing."""
            self.status = "CANCELLED"
            self.processing_completed_at = datetime.now(UTC)

    # Oracle WMS Target Configuration Models
    class TargetConfig(_BaseTargetModel):
        """Enhanced Oracle WMS target configuration model."""

        config_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Configuration identifier",
        )
        name: str = Field(
            description="Configuration name",
            min_length=1,
            max_length=255,
        )
        description: str | None = Field(
            default=None,
            description="Configuration description",
            max_length=1000,
        )
        base_url: str = Field(
            description="Oracle WMS base URL",
            min_length=1,
            max_length=500,
        )
        username: str = Field(
            description="Oracle WMS username",
            min_length=1,
            max_length=128,
        )
        password: str = Field(
            description="Oracle WMS password",
            repr=False,  # Hide in string representation for security
            min_length=1,
            max_length=128,
        )
        environment: str = Field(
            default=FlextConstants.Defaults.ENVIRONMENT,
            description="Environment identifier",
            min_length=1,
            max_length=50,
        )
        batch_size: int = Field(
            default=FlextConstants.Performance.DEFAULT_BATCH_SIZE,
            description="Default batch size",
            gt=0,
            le=100000,
        )
        timeout: float = Field(
            default=FlextConstants.Network.DEFAULT_TIMEOUT,
            description="Request timeout in seconds",
            gt=0,
            le=3600,
        )
        max_retries: int = Field(
            default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
            description="Maximum retry attempts",
            ge=0,
            le=10,
        )
        verify_ssl: bool = Field(
            default=True,
            description="Verify SSL certificates",
        )
        enable_logging: bool = Field(
            default=True,
            description="Enable request/response logging",
        )
        created_at: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Configuration creation timestamp",
        )
        updated_at: datetime | None = None
        is_active: bool = Field(
            default=True,
            description="Whether configuration is active",
        )

        @field_validator("base_url")
        @classmethod
        def validate_base_url(cls, v: str) -> str:
            """Validate base URL format."""
            result = FlextModels.create_validated_http_url(v)
            if result.is_failure:
                raise ValueError(result.error)
            # Convert FlextModels.Url back to string for Pydantic
            return str(result.unwrap())

        @field_validator("environment")
        @classmethod
        def validate_environment(cls, v: str) -> str:
            """Validate environment."""
            # Iterate directly over enum members
            valid_environments = [
                e.value for e in FlextConstants.Environment.ConfigEnvironment
            ]
            if v.lower() not in [env.lower() for env in valid_environments]:
                msg = f"Invalid environment: {v}. Valid environments: {valid_environments}"
                raise ValueError(msg)
            return v.lower()

        @computed_field
        def connection_string(self) -> str:
            """Generate connection string."""
            return f"{self.username}@{self.base_url}"

        @computed_field
        def is_production(self) -> bool:
            """Check if running in production environment."""
            return self.environment.lower() == "production"

        @computed_field
        def is_development(self) -> bool:
            """Check if running in development environment."""
            return self.environment.lower() in {"development", "dev", "local"}

        def update_timestamp(self) -> None:
            """Update the updated_at timestamp."""
            self.updated_at = datetime.now(UTC)

        def validate_configuration(self) -> FlextResult[None]:
            """Validate configuration."""
            try:
                # Validate credentials
                if not self.username.strip():
                    return FlextResult[None].fail("Username cannot be empty")
                if not self.password.strip():
                    return FlextResult[None].fail("Password cannot be empty")

                # Validate production settings
                if self.is_production and not self.verify_ssl:
                    return FlextResult[None].fail(
                        "SSL verification must be enabled in production"
                    )

                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"Configuration validation failed: {e}")

    # Oracle WMS Target Operation Models
    class TargetOperation(_BaseTargetModel):
        """Enhanced Oracle WMS target operation model."""

        operation_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Operation identifier",
        )
        operation_type: Literal["LOAD", "SYNC", "VALIDATE", "CLEANUP"] = Field(
            description="Operation type",
        )
        config_id: str = Field(
            description="Configuration identifier",
        )
        table_name: str = Field(
            description="Target table name",
            min_length=1,
            max_length=128,
        )
        schema_name: str = Field(
            description="Target schema name",
            min_length=1,
            max_length=128,
        )
        status: Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"] = (
            Field(
                default="PENDING",
                description="Operation status",
            )
        )
        started_at: datetime | None = None
        completed_at: datetime | None = None
        records_processed: int = Field(default=0, ge=0)
        records_failed: int = Field(default=0, ge=0)
        error_message: str | None = None
        metadata: dict[str, object] = Field(
            default_factory=dict,
            description="Operation metadata",
        )

        @computed_field
        def duration_seconds(self) -> float | None:
            """Calculate operation duration in seconds."""
            if self.started_at and self.completed_at:
                return (self.completed_at - self.started_at).total_seconds()
            return None

        @computed_field
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            total = self.records_processed + self.records_failed
            if total == 0:
                return 0.0
            return (self.records_processed / total) * 100.0

        @computed_field
        def is_completed(self) -> bool:
            """Check if operation is completed."""
            return self.status == "COMPLETED"

        @computed_field
        def is_failed(self) -> bool:
            """Check if operation failed."""
            return self.status == "FAILED"

        @computed_field
        def is_running(self) -> bool:
            """Check if operation is running."""
            return self.status == "RUNNING"

        def start_operation(self) -> None:
            """Start operation."""
            self.status = "RUNNING"
            self.started_at = datetime.now(UTC)

        def complete_operation(
            self, records_processed: int = 0, records_failed: int = 0
        ) -> None:
            """Complete operation."""
            self.status = "COMPLETED"
            self.completed_at = datetime.now(UTC)
            self.records_processed = records_processed
            self.records_failed = records_failed

        def fail_operation(self, error_message: str) -> None:
            """Fail operation."""
            self.status = "FAILED"
            self.completed_at = datetime.now(UTC)
            self.error_message = error_message

        def cancel_operation(self) -> None:
            """Cancel operation."""
            self.status = "CANCELLED"
            self.completed_at = datetime.now(UTC)

    # Oracle WMS Target Metrics Models
    class TargetMetrics(_BaseTargetModel):
        """Enhanced Oracle WMS target metrics model."""

        metrics_id: str = Field(
            default_factory=lambda: str(uuid.uuid4()),
            description="Metrics identifier",
        )
        operation_id: str = Field(
            description="Operation identifier",
        )
        timestamp: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Metrics timestamp",
        )
        records_per_second: float = Field(
            default=0.0,
            description="Records processed per second",
            ge=0.0,
        )
        bytes_per_second: float = Field(
            default=0.0,
            description="Bytes processed per second",
            ge=0.0,
        )
        memory_usage_mb: float = Field(
            default=0.0,
            description="Memory usage in megabytes",
            ge=0.0,
        )
        cpu_usage_percent: float = Field(
            default=0.0,
            description="CPU usage percentage",
            ge=0.0,
            le=100.0,
        )
        connection_count: int = Field(
            default=0,
            description="Active connection count",
            ge=0,
        )
        error_count: int = Field(
            default=0,
            description="Error count",
            ge=0,
        )
        retry_count: int = Field(
            default=0,
            description="Retry count",
            ge=0,
        )

        @computed_field
        def throughput_mb_per_second(self) -> float:
            """Calculate throughput in MB per second."""
            return self.bytes_per_second / (1024 * 1024)

        @computed_field
        def error_rate(self) -> float:
            """Calculate error rate percentage."""
            total_operations = self.records_per_second + self.error_count
            if total_operations == 0:
                return 0.0
            return (self.error_count / total_operations) * 100.0

    # Factory methods for creating model instances
    @classmethod
    def create_target_record(
        cls,
        table_name: str,
        schema_name: str,
        data: dict[str, object],
        operation: str = "INSERT",
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleWmsModels.TargetRecord]:
        """Create target record with validation."""
        try:
            record = cls.TargetRecord(
                table_name=table_name,
                schema_name=schema_name,
                data=data,
                operation=operation,
                **kwargs,
            )
            return FlextResult[cls.TargetRecord].ok(record)
        except Exception as e:
            return FlextResult[cls.TargetRecord].fail(f"Record creation failed: {e}")

    @classmethod
    def create_target_batch(
        cls,
        table_name: str,
        schema_name: str,
        records: list[FlextTargetOracleWmsModels.TargetRecord],
        load_method: str = "APPEND_ONLY",
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleWmsModels.TargetBatch]:
        """Create target batch with validation."""
        try:
            batch = cls.TargetBatch(
                table_name=table_name,
                schema_name=schema_name,
                records=records,
                batch_size=len(records),
                load_method=load_method,
                **kwargs,
            )
            return FlextResult[cls.TargetBatch].ok(batch)
        except Exception as e:
            return FlextResult[cls.TargetBatch].fail(f"Batch creation failed: {e}")

    @classmethod
    def create_target_config(
        cls,
        name: str,
        base_url: str,
        username: str,
        password: str,
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleWmsModels.TargetConfig]:
        """Create target configuration with validation."""
        try:
            config = cls.TargetConfig(
                name=name,
                base_url=base_url,
                username=username,
                password=password,
                **kwargs,
            )

            # Validate configuration
            validation_result = config.validate_configuration()
            if validation_result.is_failure:
                return FlextResult[cls.TargetConfig].fail(
                    f"Configuration validation failed: {validation_result.error}"
                )

            return FlextResult[cls.TargetConfig].ok(config)
        except Exception as e:
            return FlextResult[cls.TargetConfig].fail(
                f"Configuration creation failed: {e}"
            )

    @classmethod
    def create_target_operation(
        cls,
        operation_type: str,
        config_id: str,
        table_name: str,
        schema_name: str,
        **kwargs: object,
    ) -> FlextResult[FlextTargetOracleWmsModels.TargetOperation]:
        """Create target operation with validation."""
        try:
            operation = cls.TargetOperation(
                operation_type=operation_type,
                config_id=config_id,
                table_name=table_name,
                schema_name=schema_name,
                **kwargs,
            )
            return FlextResult[cls.TargetOperation].ok(operation)
        except Exception as e:
            return FlextResult[cls.TargetOperation].fail(
                f"Operation creation failed: {e}"
            )
