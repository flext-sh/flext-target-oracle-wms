"""FLEXT Target Oracle WMS Types - Domain-specific Singer Oracle WMS target type definitions.

This module provides Singer Oracle WMS target-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# TARGET ORACLE WMS-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle WMS target operations
# =============================================================================


# Singer Oracle WMS target domain TypeVars
class FlextTargetOracleWmsTypes(FlextTypes):
    """Singer Oracle WMS target-specific type definitions extending FlextTypes.

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
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue]
        ]
        type MessageProcessing = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type RecordHandling = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]
        type StateManagement = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type BatchProcessing = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE WMS WAREHOUSE TYPES - Complex warehouse management types
    # =========================================================================

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type FacilityDefinition = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type LocationManagement = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ZoneConfiguration = dict[str, str | FlextTypes.Dict]
        type WarehouseMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type LayoutDefinition = dict[str, str | bool | FlextTypes.Dict]

    # =========================================================================
    # WMS INVENTORY TYPES - Complex inventory management types
    # =========================================================================

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ItemMasterData = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StockLevelTracking = dict[
            str, int | float | dict[str, FlextTypes.ConfigValue]
        ]
        type AllocationManagement = dict[str, int | str | FlextTypes.Dict]
        type InventoryMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]
        type CycleCountData = dict[str, str | int | FlextTypes.Dict]

    # =========================================================================
    # WMS ORDER MANAGEMENT TYPES - Complex order processing types
    # =========================================================================

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = dict[
            str, str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type OrderProcessing = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type FulfillmentWorkflow = dict[str, str | int | FlextTypes.Dict]
        type PickingInstructions = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ShippingConfiguration = dict[
            str, bool | str | dict[str, FlextTypes.ConfigValue]
        ]
        type OrderTracking = dict[str, str | int | FlextTypes.Dict]

    # =========================================================================
    # WMS LABOR MANAGEMENT TYPES - Complex workforce management types
    # =========================================================================

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type WorkforceManagement = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type TaskAssignment = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ProductivityMetrics = dict[str, float | int | FlextTypes.Dict]
        type PerformanceTracking = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type WorkforceScheduling = dict[str, str | int | FlextTypes.Dict]

    # =========================================================================
    # WMS TRANSPORTATION TYPES - Complex transportation management types
    # =========================================================================

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type CarrierManagement = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ShipmentTracking = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DeliveryScheduling = dict[str, str | bool | FlextTypes.Dict]
        type TransportMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]
        type RouteOptimization = dict[
            str, str | FlextTypes.StringList | FlextTypes.Dict
        ]

    # =========================================================================
    # DATA TRANSFORMATION TYPES - Complex data transformation types
    # =========================================================================

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type FieldMapping = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type DataValidation = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TypeConversion = dict[str, bool | str | FlextTypes.Dict]
        type FilteringRules = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type TransformationResult = dict[str, dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextTypes.ConfigValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamRecord = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type StreamState = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamBookmark = dict[str, str | int | FlextTypes.Dict]
        type StreamSchema = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type ErrorRecovery = dict[str, str | bool | FlextTypes.Dict]
        type ErrorReporting = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type ErrorClassification = dict[str, str | int | FlextTypes.Dict]
        type ErrorMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]

    # =========================================================================
    # SINGER TARGET ORACLE WMS PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """Singer Target Oracle WMS-specific project types extending FlextTypes.Project.

        Adds Singer target Oracle WMS-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        # Singer target Oracle WMS-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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

        # Singer target Oracle WMS-specific project configurations
        type SingerTargetOracleWmsProjectConfig = dict[
            str, FlextTypes.ConfigValue | object
        ]
        type WmsLoaderConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type SingerProtocolConfig = dict[str, bool | str | FlextTypes.Dict]
        type TargetOracleWmsPipelineConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle WMS target TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextTargetOracleWmsTypes",
]
