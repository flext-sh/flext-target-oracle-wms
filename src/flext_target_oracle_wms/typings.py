"""FLEXT Target Oracle WMS Types - Domain-specific Singer Oracle WMS target type definitions.

This module provides Singer Oracle WMS target-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes as t

# =============================================================================
# TARGET ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle WMS target operations
# =============================================================================


# Singer Oracle WMS target domain TypeVars
class FlextTargetOracleWmsTypes(t):
    """Singer Oracle WMS target-specific type definitions extending t.

    Domain-specific type system for Singer Oracle WMS target operations.
    Contains ONLY complex Oracle WMS target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TARGET TYPES - Complex Singer target protocol types
    # =========================================================================

    class SingerTarget:
        """Singer target protocol complex types."""

        type TargetConfiguration = dict[
            str, str | int | bool | dict[str, t.GeneralValueType]
        ]
        type StreamConfiguration = dict[
            str,
            str | bool | dict[str, t.JsonValue],
        ]
        type MessageProcessing = dict[str, str | list[dict[str, t.JsonValue]]]
        type RecordHandling = dict[str, str | dict[str, t.JsonValue] | bool]
        type StateManagement = dict[str, str | dict[str, t.JsonValue]]
        type BatchProcessing = dict[str, str | int | dict[str, t.JsonValue]]

    # =========================================================================
    # ORACLE WMS WAREHOUSE TYPES - Complex warehouse management types
    # =========================================================================

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = dict[
            str, str | int | bool | dict[str, t.GeneralValueType]
        ]
        type FacilityDefinition = dict[
            str,
            str | list[str] | dict[str, t.JsonValue],
        ]
        type LocationManagement = dict[str, str | dict[str, t.JsonValue]]
        type ZoneConfiguration = dict[str, str | dict[str, t.GeneralValueType]]
        type WarehouseMetadata = dict[str, str | dict[str, t.JsonValue]]
        type LayoutDefinition = dict[str, str | bool | dict[str, t.GeneralValueType]]

    # =========================================================================
    # WMS INVENTORY TYPES - Complex inventory management types
    # =========================================================================

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = dict[
            str, str | int | bool | dict[str, t.GeneralValueType]
        ]
        type ItemMasterData = dict[str, str | dict[str, t.JsonValue]]
        type StockLevelTracking = dict[str, int | float | dict[str, t.GeneralValueType]]
        type AllocationManagement = dict[str, int | str | dict[str, t.GeneralValueType]]
        type InventoryMetrics = dict[str, int | float | dict[str, t.JsonValue]]
        type CycleCountData = dict[str, str | int | dict[str, t.GeneralValueType]]

    # =========================================================================
    # WMS ORDER MANAGEMENT TYPES - Complex order processing types
    # =========================================================================

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = dict[str, str | int | dict[str, t.GeneralValueType]]
        type OrderProcessing = dict[str, str | bool | dict[str, t.JsonValue]]
        type FulfillmentWorkflow = dict[str, str | int | dict[str, t.GeneralValueType]]
        type PickingInstructions = dict[str, str | dict[str, t.JsonValue]]
        type ShippingConfiguration = dict[
            str, bool | str | dict[str, t.GeneralValueType]
        ]
        type OrderTracking = dict[str, str | int | dict[str, t.GeneralValueType]]

    # =========================================================================
    # WMS LABOR MANAGEMENT TYPES - Complex workforce management types
    # =========================================================================

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = dict[str, str | bool | dict[str, t.GeneralValueType]]
        type WorkforceManagement = dict[
            str,
            int | float | dict[str, t.JsonValue],
        ]
        type TaskAssignment = dict[str, str | dict[str, t.JsonValue]]
        type ProductivityMetrics = dict[
            str, float | int | dict[str, t.GeneralValueType]
        ]
        type PerformanceTracking = dict[
            str,
            int | float | dict[str, t.JsonValue],
        ]
        type WorkforceScheduling = dict[str, str | int | dict[str, t.GeneralValueType]]

    # =========================================================================
    # WMS TRANSPORTATION TYPES - Complex transportation management types
    # =========================================================================

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = dict[
            str, str | int | bool | dict[str, t.GeneralValueType]
        ]
        type CarrierManagement = dict[str, str | dict[str, t.JsonValue]]
        type ShipmentTracking = dict[str, str | dict[str, t.JsonValue]]
        type DeliveryScheduling = dict[str, str | bool | dict[str, t.GeneralValueType]]
        type TransportMetrics = dict[str, int | float | dict[str, t.JsonValue]]
        type RouteOptimization = dict[
            str, str | list[str] | dict[str, t.GeneralValueType]
        ]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | dict[str, t.GeneralValueType]
        ]
        type FieldMapping = dict[str, str | list[str] | dict[str, t.GeneralValueType]]
        type DataValidation = dict[str, str | dict[str, t.JsonValue]]
        type TypeConversion = dict[str, bool | str | dict[str, t.GeneralValueType]]
        type FilteringRules = dict[str, str | dict[str, t.JsonValue]]
        type TransformationResult = dict[str, dict[str, t.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, t.GeneralValueType]
        ]
        type StreamMetadata = dict[str, str | dict[str, t.JsonValue]]
        type StreamRecord = dict[str, t.JsonValue | dict[str, t.GeneralValueType]]
        type StreamState = dict[str, str | int | dict[str, t.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, t.GeneralValueType]]
        type StreamSchema = dict[str, str | dict[str, t.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, t.GeneralValueType]
        ]
        type ErrorRecovery = dict[str, str | bool | dict[str, t.GeneralValueType]]
        type ErrorReporting = dict[str, str | int | dict[str, t.JsonValue]]
        type ErrorClassification = dict[str, str | int | dict[str, t.GeneralValueType]]
        type ErrorMetrics = dict[str, int | float | dict[str, t.JsonValue]]
        type ErrorTracking = list[dict[str, str | int | dict[str, t.JsonValue]]]

    # =========================================================================
    # SINGER TARGET ORACLE WMS PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """Singer Target Oracle WMS-specific project types.

        Adds Singer target Oracle WMS-specific project types.
        Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        # Singer target Oracle WMS-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # Singer target Oracle WMS-specific types
            "singer-target",
            "wms-loader",
            "warehouse-loader",
            "singer-target-oracle-wms",
            "target-oracle-wms",
            "wms-connector",
            "warehouse-connector",
            "singer-protocol",
            "wms-integration",
            "oracle-wms",
            "warehouse-management",
            "singer-stream",
            "etl-target",
            "data-pipeline",
            "wms-sink",
            "singer-integration",
        ]

        # Error type literal - references ErrorType StrEnum from constants
        type ErrorTypeLiteral = Literal[
            "WMS_CONNECTION",
            "WMS_AUTHENTICATION",
            "WMS_BUSINESS_RULE",
            "WMS_VALIDATION",
            "SINGER_PROTOCOL",
            "DATA_TRANSFORMATION",
            "PERFORMANCE",
            "CONFIGURATION",
        ]

        # Singer target Oracle WMS-specific project configurations
        type SingerTargetOracleWmsProjectConfig = dict[str, t.GeneralValueType]
        type WmsLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | dict[str, t.GeneralValueType]
        ]
        type TargetOracleWmsPipelineConfig = dict[str, t.GeneralValueType]

    class TargetOracleWms:
        """Target Oracle WMS types namespace for cross-project access.

        Provides organized access to all Target Oracle WMS types for other FLEXT projects.
        Usage: Other projects can reference `t.TargetOracleWms.OracleWmsWarehouse.*`, `t.TargetOracleWms.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_target_oracle_wms.typings import t
            config: t.TargetOracleWms.Project.SingerTargetOracleWmsProjectConfig = ...
            warehouse: t.TargetOracleWms.OracleWmsWarehouse.FacilityDefinition = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


# Module-level alias for simplified usage
# Note: 't' is imported from flext_core above for internal use
# This alias provides the extended type system for external consumers
TargetOracleWmsTypes = FlextTargetOracleWmsTypes

# Namespace composition via class inheritance
# TargetOracleWms namespace provides access to nested classes through inheritance
# Access patterns:
# - TargetOracleWmsTypes.TargetOracleWms.* for Target Oracle WMS-specific types
# - TargetOracleWmsTypes.Project.* for project types
# - TargetOracleWmsTypes.Core.* for core types (inherited from parent)

# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle WMS target TypeVars and types
# =============================================================================

__all__ = [
    "FlextTargetOracleWmsTypes",
    "TargetOracleWmsTypes",
]
