"""FLEXT Target Oracle WMS Types - Domain-specific Singer Oracle WMS target type definitions.

This module provides Singer Oracle WMS target-specific type definitions extending FlextMeltanoTypes.
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

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """Singer Oracle WMS target-specific type definitions extending FlextMeltanoTypes.

    Domain-specific type system for Singer Oracle WMS target operations.
    Contains ONLY complex Oracle WMS target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetOracleWms:
        """Singer target protocol complex types."""

        type TargetConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type StreamConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type MessageProcessing = dict[
            str, str | list[Mapping[str, FlextMeltanoTypes.object]]
        ]
        type RecordHandling = dict[
            str, str | Mapping[str, FlextMeltanoTypes.object] | bool
        ]
        type StateManagement = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type BatchProcessing = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.object]
        ]

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type FacilityDefinition = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.object]
        ]
        type LocationManagement = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type ZoneConfiguration = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type WarehouseMetadata = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type LayoutDefinition = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type ItemMasterData = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type StockLevelTracking = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.object]
        ]
        type AllocationManagement = dict[
            str, int | str | Mapping[str, FlextMeltanoTypes.object]
        ]
        type InventoryMetrics = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.object]
        ]
        type CycleCountData = dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type OrderProcessing = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type FulfillmentWorkflow = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type PickingInstructions = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type ShippingConfiguration = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.object]
        ]
        type OrderTracking = dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type WorkforceManagement = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.object]
        ]
        type TaskAssignment = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type ProductivityMetrics = dict[
            str, float | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type PerformanceTracking = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.object]
        ]
        type WorkforceScheduling = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.object]
        ]

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type CarrierManagement = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type ShipmentTracking = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type DeliveryScheduling = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type TransportMetrics = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.object]
        ]
        type RouteOptimization = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.object]
        ]

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.object]
        ]
        type FieldMapping = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.object]
        ]
        type DataValidation = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type TypeConversion = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.object]
        ]
        type FilteringRules = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type TransformationResult = dict[str, dict[str, FlextMeltanoTypes.object]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type StreamMetadata = dict[str, str | Mapping[str, FlextMeltanoTypes.object]]
        type StreamRecord = dict[
            str,
            FlextMeltanoTypes.object | Mapping[str, FlextMeltanoTypes.object],
        ]
        type StreamState = dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]
        type StreamBookmark = dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]
        type StreamSchema = dict[str, str | Mapping[str, FlextMeltanoTypes.object] | bool]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type ErrorRecovery = dict[str, str | bool | Mapping[str, FlextMeltanoTypes.object]]
        type ErrorReporting = dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]
        type ErrorClassification = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.object]
        ]
        type ErrorMetrics = dict[str, int | float | Mapping[str, FlextMeltanoTypes.object]]
        type ErrorTracking = list[
            dict[str, str | int | Mapping[str, FlextMeltanoTypes.object]]
        ]

    class Project:
        """Singer Target Oracle WMS-specific project types.

        Adds Singer target Oracle WMS-specific project types.
        Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
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
        type SingerTargetOracleWmsProjectConfig = dict[str, FlextMeltanoTypes.object]
        type WmsLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.object]
        ]
        type TargetOracleWmsPipelineConfig = dict[str, FlextMeltanoTypes.object]


t = FlextTargetOracleWmsTypes
__all__ = ["FlextTargetOracleWmsTypes", "t"]
