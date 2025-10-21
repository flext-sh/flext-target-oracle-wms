"""FlextTargetOracleWmsModels - Oracle WMS target models extending flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import Literal

from flext_core import FlextModels, FlextResult
from pydantic import Field, SecretStr

from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants

# Oracle WMS constants
oauth2 = "oauth2"
basic = "basic"
WMS_CONNECTION = "WMS_CONNECTION"
WMS_AUTHENTICATION = "WMS_AUTHENTICATION"
WMS_BUSINESS_RULE = "WMS_BUSINESS_RULE"
WMS_VALIDATION = "WMS_VALIDATION"
SINGER_PROTOCOL = "SINGER_PROTOCOL"
DATA_TRANSFORMATION = "DATA_TRANSFORMATION"
PERFORMANCE = "PERFORMANCE"
CONFIGURATION = "CONFIGURATION"


class FlextTargetOracleWmsModels(FlextModels):
    """Oracle WMS target models extending flext-core FlextModels.

    Provides complete models for Oracle Warehouse Management System data loading,
    Singer protocol compliance, WMS business rule validation, and target operations
    following standardized patterns.
    """

    class WmsAuthenticationConfig(FlextModels.BaseConfig):
        """Oracle WMS authentication configuration with complete auth support."""

        base_url: str = Field(..., description="Oracle WMS base URL")
        auth_method: Literal[oauth2, basic, api_key] = Field(
            default="oauth2", description="Authentication method"
        )

        # OAuth2 configuration
        oauth_client_id: str | None = Field(None, description="OAuth2 client ID")
        oauth_client_secret: SecretStr | None = Field(
            None, description="OAuth2 client secret"
        )
        oauth_token_url: str | None = Field(None, description="OAuth2 token endpoint")
        oauth_scope: str | None = Field(None, description="OAuth2 scope")

        # Basic auth configuration
        username: str | None = Field(None, description="Basic auth username")
        password: SecretStr | None = Field(None, description="Basic auth password")

        # API key configuration
        api_key: SecretStr | None = Field(
            None, description="API key for authentication"
        )
        api_key_header: str = Field(
            default="X-API-Key", description="API key header name"
        )

        # WMS-specific configuration
        company_code: str = Field(..., description="WMS company code")
        facility_code: str = Field(..., description="WMS facility code")

        # Connection settings
        connection_timeout: int = Field(
            default=120, ge=30, le=600, description="Connection timeout seconds"
        )
        request_timeout: int = Field(
            default=300, ge=60, le=1800, description="Request timeout seconds"
        )
        max_retries: int = Field(
            default=5, ge=1, le=10, description="Maximum retry attempts"
        )
        retry_delay: int = Field(
            default=2, ge=1, le=30, description="Retry delay seconds"
        )

    class WmsInventoryItem(FlextModels.Entity):
        """Oracle WMS inventory item model with business validation."""

        item_id: str = Field(
            ..., description="WMS item identifier", min_length=1, max_length=50
        )
        item_description: str = Field(
            ..., description="Item description", max_length=255
        )
        unit_of_measure: str = Field(..., description="Unit of measure", max_length=10)
        item_type: str = Field(..., description="Item type", max_length=20)
        abc_class: str | None = Field(
            None, description="ABC classification", max_length=1
        )

        # Physical attributes
        weight: float | None = Field(None, ge=0, description="Item weight")
        volume: float | None = Field(None, ge=0, description="Item volume")
        length: float | None = Field(None, ge=0, description="Item length")
        width: float | None = Field(None, ge=0, description="Item width")
        height: float | None = Field(None, ge=0, description="Item height")

        # Status and flags
        active_flag: bool = Field(default=True, description="Item active status")
        lot_controlled_flag: bool = Field(
            default=False, description="Lot control enabled"
        )
        serial_controlled_flag: bool = Field(
            default=False, description="Serial control enabled"
        )

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate WMS inventory item business rules."""
            try:
                errors = []

                # Validate item ID format
                if not self.item_id.replace("-", "").replace("_", "").isalnum():
                    errors.append(
                        "Item ID must be alphanumeric with optional hyphens/underscores"
                    )

                # Validate unit of measure
                valid_uoms = ["EA", "LB", "KG", "OZ", "LT", "GL", "FT", "M", "IN", "CM"]
                if self.unit_of_measure not in valid_uoms:
                    errors.append(
                        f"Unit of measure must be one of: {', '.join(valid_uoms)}"
                    )

                # Validate ABC class
                if self.abc_class and self.abc_class not in {"A", "B", "C"}:
                    errors.append("ABC class must be A, B, or C")

                # Validate physical dimensions consistency
                dimensions = [self.length, self.width, self.height]
                if any(d is not None for d in dimensions) and not all(
                    d is not None for d in dimensions
                ):
                    errors.append(
                        "All dimensions (length, width, height) must be provided together"
                    )

                if errors:
                    return FlextResult[None].fail("; ".join(errors))
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(
                    f"WMS inventory item validation failed: {e}"
                )

    class WmsInventoryLocation(FlextModels.Entity):
        """Oracle WMS inventory location model with warehouse validation."""

        location_id: str = Field(
            ..., description="WMS location identifier", min_length=1, max_length=50
        )
        location_type: str = Field(..., description="Location type", max_length=20)
        zone_id: str | None = Field(None, description="Zone identifier", max_length=20)
        aisle: str | None = Field(None, description="Aisle identifier", max_length=10)
        bay: str | None = Field(None, description="Bay identifier", max_length=10)
        level: str | None = Field(None, description="Level identifier", max_length=10)
        position: str | None = Field(
            None, description="Position identifier", max_length=10
        )

        # Capacity and constraints
        max_volume: float | None = Field(
            None, ge=0, description="Maximum volume capacity"
        )
        max_weight: float | None = Field(
            None, ge=0, description="Maximum weight capacity"
        )
        max_units: int | None = Field(None, ge=0, description="Maximum unit capacity")

        # Status and flags
        active_flag: bool = Field(default=True, description="Location active status")
        pickable_flag: bool = Field(
            default=True, description="Location pickable status"
        )
        receivable_flag: bool = Field(
            default=True, description="Location receivable status"
        )

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate WMS inventory location business rules."""
            try:
                errors = []

                # Validate location ID format (typically hierarchical)
                if "-" in self.location_id:
                    parts = self.location_id.split("-")
                    if (
                        len(parts)
                        < FlextTargetOracleWmsConstants.OracleWms.MIN_LOCATION_PARTS
                    ):
                        errors.append(
                            "Location ID with hyphens must have at least 2 parts"
                        )

                # Validate location type
                valid_types = [
                    "PICK",
                    "RESERVE",
                    "STAGING",
                    "SHIPPING",
                    "RECEIVING",
                    "BULK",
                    "DAMAGE",
                ]
                if self.location_type not in valid_types:
                    errors.append(
                        f"Location type must be one of: {', '.join(valid_types)}"
                    )

                # Validate capacity constraints
                if self.max_volume is not None and self.max_volume <= 0:
                    errors.append("Maximum volume must be positive")

                if self.max_weight is not None and self.max_weight <= 0:
                    errors.append("Maximum weight must be positive")

                if errors:
                    return FlextResult[None].fail("; ".join(errors))
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(
                    f"WMS inventory location validation failed: {e}"
                )

    class WmsInventoryTransaction(FlextModels.Entity):
        """Oracle WMS inventory transaction model with audit trail."""

        transaction_id: str = Field(
            ..., description="Transaction identifier", min_length=1, max_length=50
        )
        transaction_type: str = Field(
            ..., description="Transaction type", max_length=20
        )
        item_id: str = Field(..., description="Item identifier", max_length=50)
        location_id: str = Field(..., description="Location identifier", max_length=50)

        # Quantity and lot information
        quantity: float = Field(..., description="Transaction quantity")
        unit_of_measure: str = Field(..., description="Unit of measure", max_length=10)
        lot_number: str | None = Field(None, description="Lot number", max_length=50)
        serial_number: str | None = Field(
            None, description="Serial number", max_length=50
        )

        # Reference information
        reference_type: str | None = Field(
            None, description="Reference document type", max_length=20
        )
        reference_number: str | None = Field(
            None, description="Reference document number", max_length=50
        )
        reason_code: str | None = Field(
            None, description="Transaction reason code", max_length=20
        )

        # Audit information
        transaction_date: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Transaction timestamp",
        )
        user_id: str | None = Field(
            None, description="User performing transaction", max_length=50
        )

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate WMS inventory transaction business rules."""
            try:
                errors = []

                # Validate transaction type
                valid_types = [
                    "RECEIPT",
                    "SHIPMENT",
                    "ADJUSTMENT",
                    "MOVE",
                    "PICK",
                    "PUTAWAY",
                    "CYCLE_COUNT",
                    "TRANSFER",
                    "RETURN",
                    "DAMAGE",
                    "SCRAP",
                ]
                if self.transaction_type not in valid_types:
                    errors.append(
                        f"Transaction type must be one of: {', '.join(valid_types)}"
                    )

                # Validate quantity based on transaction type
                if (
                    self.transaction_type in {"SHIPMENT", "PICK", "SCRAP"}
                    and self.quantity >= 0
                ):
                    errors.append(
                        f"Transaction type {self.transaction_type} must have negative quantity"
                    )
                elif (
                    self.transaction_type in {"RECEIPT", "PUTAWAY", "RETURN"}
                    and self.quantity <= 0
                ):
                    errors.append(
                        f"Transaction type {self.transaction_type} must have positive quantity"
                    )

                # Validate lot/serial requirements
                lot_required_types = ["RECEIPT", "SHIPMENT", "PICK"]
                if self.transaction_type in lot_required_types and not self.lot_number:
                    errors.append(
                        f"Lot number required for transaction type {self.transaction_type}"
                    )

                if errors:
                    return FlextResult[None].fail("; ".join(errors))
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(
                    f"WMS inventory transaction validation failed: {e}"
                )

    class WmsShipment(FlextModels.Entity):
        """Oracle WMS shipment model with carrier and tracking."""

        shipment_id: str = Field(
            ..., description="Shipment identifier", min_length=1, max_length=50
        )
        order_number: str = Field(
            ..., description="Order number reference", max_length=50
        )
        carrier_code: str = Field(..., description="Carrier code", max_length=20)
        service_level: str = Field(..., description="Service level", max_length=20)

        # Tracking information
        tracking_number: str | None = Field(
            None, description="Carrier tracking number", max_length=50
        )
        pro_number: str | None = Field(None, description="PRO number", max_length=50)

        # Dates and timing
        ship_date: datetime | None = Field(None, description="Actual ship date")
        delivery_date: datetime | None = Field(
            None, description="Scheduled delivery date"
        )
        requested_ship_date: datetime | None = Field(
            None, description="Requested ship date"
        )

        # Address information
        ship_to_name: str = Field(..., description="Ship-to name", max_length=100)
        ship_to_address1: str = Field(
            ..., description="Ship-to address line 1", max_length=100
        )
        ship_to_address2: str | None = Field(
            None, description="Ship-to address line 2", max_length=100
        )
        ship_to_city: str = Field(..., description="Ship-to city", max_length=50)
        ship_to_state: str = Field(..., description="Ship-to state", max_length=10)
        ship_to_postal_code: str = Field(
            ..., description="Ship-to postal code", max_length=20
        )
        ship_to_country: str = Field(
            default="US", description="Ship-to country", max_length=5
        )

        # Status and flags
        status: str = Field(
            default="OPEN", description="Shipment status", max_length=20
        )

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate WMS shipment business rules."""
            try:
                errors = []

                # Validate carrier code
                valid_carriers = [
                    "UPS",
                    "FEDEX",
                    "USPS",
                    "DHL",
                    "LTL",
                    "TRUCK",
                    "PICKUP",
                ]
                if self.carrier_code not in valid_carriers:
                    errors.append(
                        f"Carrier code must be one of: {', '.join(valid_carriers)}"
                    )

                # Validate service level
                valid_services = [
                    "GROUND",
                    "2DAY",
                    "OVERNIGHT",
                    "3DAY",
                    "STANDARD",
                    "EXPRESS",
                ]
                if self.service_level not in valid_services:
                    errors.append(
                        f"Service level must be one of: {', '.join(valid_services)}"
                    )

                # Validate status
                valid_statuses = [
                    "OPEN",
                    "PICKED",
                    "PACKED",
                    "SHIPPED",
                    "DELIVERED",
                    "CANCELLED",
                ]
                if self.status not in valid_statuses:
                    errors.append(f"Status must be one of: {', '.join(valid_statuses)}")

                # Validate date logic
                if (
                    self.ship_date
                    and self.requested_ship_date
                    and self.ship_date < self.requested_ship_date
                ):
                    errors.append("Ship date cannot be before requested ship date")

                # Validate postal code format (basic US format)
                if self.ship_to_country == "US" and not re.match(
                    r"^\d{5}(-\d{4})?$", self.ship_to_postal_code
                ):
                    errors.append(
                        "US postal code must be in format 12345 or 12345-6789"
                    )

                if errors:
                    return FlextResult[None].fail("; ".join(errors))
                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(f"WMS shipment validation failed: {e}")

    class WmsTargetConfig(FlextModels.BaseConfig):
        """Oracle WMS target configuration for Singer protocol."""

        # WMS connection configuration
        wms_auth: FlextTargetOracleWmsModels.WmsAuthenticationConfig = Field(
            ..., description="WMS authentication configuration"
        )

        # Singer target configuration
        stream_maps: dict[str, dict[str, str]] = Field(
            default_factory=dict, description="Stream to WMS entity mappings"
        )

        # Performance configuration
        batch_size: int = Field(
            default=1000, ge=1, le=10000, description="Batch size for processing"
        )
        parallel_degree: int = Field(
            default=4, ge=1, le=16, description="Parallel processing degree"
        )
        enable_bulk_binding: bool = Field(
            default=True, description="Enable bulk database operations"
        )

        # Validation configuration
        validate_records: bool = Field(
            default=True, description="Enable record validation"
        )
        validate_item_codes: bool = Field(
            default=True, description="Validate item codes against WMS"
        )
        validate_location_codes: bool = Field(
            default=True, description="Validate location codes against WMS"
        )
        enable_business_rule_validation: bool = Field(
            default=True, description="Enable WMS business rule validation"
        )

        # Logging and monitoring
        enable_performance_logging: bool = Field(
            default=False, description="Enable performance logging"
        )
        enable_audit_logging: bool = Field(
            default=True, description="Enable audit logging"
        )

    class WmsTargetResult(FlextModels.Entity):
        """Oracle WMS target operation result with complete metrics."""

        # Processing summary
        total_records_processed: int = Field(
            default=0, ge=0, description="Total records processed"
        )
        successful_records: int = Field(
            default=0, ge=0, description="Successfully processed records"
        )
        failed_records: int = Field(default=0, ge=0, description="Failed records")

        # Performance metrics
        processing_duration_ms: float = Field(
            default=0.0, ge=0.0, description="Total processing time"
        )
        average_processing_time_ms: float = Field(
            default=0.0, ge=0.0, description="Average per-record time"
        )
        records_per_second: float = Field(
            default=0.0, ge=0.0, description="Processing throughput"
        )

        # Error tracking
        error_messages: list[str] = Field(
            default_factory=list, description="Error messages"
        )
        warning_messages: list[str] = Field(
            default_factory=list, description="Warning messages"
        )

        # WMS-specific results
        wms_operations_executed: dict[str, int] = Field(
            default_factory=dict, description="WMS operations executed by type"
        )
        business_rule_violations: list[str] = Field(
            default_factory=list, description="Business rule violations"
        )

        def validate_business_rules(self) -> FlextResult[None]:
            """Validate WMS target result business rules."""
            try:
                # Validate record counts
                if (
                    self.successful_records + self.failed_records
                    != self.total_records_processed
                ):
                    return FlextResult[None].fail(
                        "Sum of successful and failed records must equal total processed"
                    )

                # Validate performance metrics
                if self.total_records_processed > 0 and self.processing_duration_ms > 0:
                    expected_avg = (
                        self.processing_duration_ms / self.total_records_processed
                    )
                    if (
                        abs(self.average_processing_time_ms - expected_avg)
                        > FlextTargetOracleWmsConstants.OracleWms.PROCESSING_TIME_TOLERANCE
                    ):
                        return FlextResult[None].fail(
                            "Average processing time inconsistent with total duration"
                        )

                return FlextResult[None].ok(None)
            except Exception as e:
                return FlextResult[None].fail(
                    f"WMS target result validation failed: {e}"
                )

        @property
        def success_rate(self) -> float:
            """Calculate success rate percentage."""
            if self.total_records_processed == 0:
                return 0.0
            return (self.successful_records / self.total_records_processed) * 100.0

        @property
        def failure_rate(self) -> float:
            """Calculate failure rate percentage."""
            if self.total_records_processed == 0:
                return 0.0
            return (self.failed_records / self.total_records_processed) * 100.0

    class WmsErrorContext(FlextModels.BaseModel):
        """Error context for WMS target error handling."""

        error_type: Literal[
            WMS_CONNECTION,
            WMS_AUTHENTICATION,
            WMS_BUSINESS_RULE,
            WMS_VALIDATION,
            SINGER_PROTOCOL,
            DATA_TRANSFORMATION,
            PERFORMANCE,
            CONFIGURATION,
        ] = Field(..., description="Error category")

        # Context information
        wms_entity: str | None = Field(None, description="WMS entity causing error")
        record_id: str | None = Field(
            None, description="Record identifier causing error"
        )
        stream_name: str | None = Field(None, description="Singer stream name")
        operation_type: str | None = Field(None, description="WMS operation type")

        # WMS-specific context
        wms_error_code: str | None = Field(None, description="WMS-specific error code")
        business_rule_violated: str | None = Field(
            None, description="Business rule violated"
        )
        validation_failures: list[str] = Field(
            default_factory=list, description="Validation failure details"
        )

        # Recovery information
        is_retryable: bool = Field(
            default=False, description="Whether error is retryable"
        )
        suggested_action: str | None = Field(
            None, description="Suggested recovery action"
        )
        max_retry_attempts: int | None = Field(
            None, description="Maximum retry attempts"
        )


__all__ = [
    "FlextTargetOracleWmsModels",
]
