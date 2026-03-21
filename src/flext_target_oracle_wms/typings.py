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

from collections.abc import Mapping

from flext_core.constants import c
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
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type StreamConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type MessageProcessing = dict[
            str, str | list[Mapping[str, FlextMeltanoTypes.Container]]
        ]
        type RecordHandling = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container] | bool
        ]
        type StateManagement = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type BatchProcessing = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type FacilityDefinition = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type LocationManagement = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ZoneConfiguration = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type WarehouseMetadata = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type LayoutDefinition = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ItemMasterData = dict[str, str | Mapping[str, FlextMeltanoTypes.Container]]
        type StockLevelTracking = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type AllocationManagement = dict[
            str, int | str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type InventoryMetrics = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type CycleCountData = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type OrderProcessing = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type FulfillmentWorkflow = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type PickingInstructions = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ShippingConfiguration = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type OrderTracking = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type WorkforceManagement = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type TaskAssignment = dict[str, str | Mapping[str, FlextMeltanoTypes.Container]]
        type ProductivityMetrics = dict[
            str, float | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type PerformanceTracking = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type WorkforceScheduling = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = dict[
            str, str | int | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type CarrierManagement = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ShipmentTracking = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type DeliveryScheduling = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type TransportMetrics = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type RouteOptimization = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.Container]
        ]

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type FieldMapping = dict[
            str, str | list[str] | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type DataValidation = dict[str, str | Mapping[str, FlextMeltanoTypes.Container]]
        type TypeConversion = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type FilteringRules = dict[str, str | Mapping[str, FlextMeltanoTypes.Container]]
        type TransformationResult = dict[str, dict[str, FlextMeltanoTypes.Container]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type StreamMetadata = dict[str, str | Mapping[str, FlextMeltanoTypes.Container]]
        type StreamRecord = dict[
            str,
            FlextMeltanoTypes.Container | Mapping[str, FlextMeltanoTypes.Container],
        ]
        type StreamState = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type StreamBookmark = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type StreamSchema = dict[
            str, str | Mapping[str, FlextMeltanoTypes.Container] | bool
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ErrorRecovery = dict[
            str, str | bool | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ErrorReporting = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ErrorClassification = dict[
            str, str | int | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ErrorMetrics = dict[
            str, int | float | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type ErrorTracking = list[
            dict[str, str | int | Mapping[str, FlextMeltanoTypes.Container]]
        ]

    class Project:
        """Singer Target Oracle WMS-specific project types.

        Adds Singer target Oracle WMS-specific project types.
        Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type ErrorTypeLiteral = c.ErrorTypeLiteral
        type SingerTargetOracleWmsProjectConfig = dict[str, FlextMeltanoTypes.Container]
        type WmsLoaderConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | Mapping[str, FlextMeltanoTypes.Container]
        ]
        type TargetOracleWmsPipelineConfig = dict[str, FlextMeltanoTypes.Container]


t = FlextTargetOracleWmsTypes
__all__ = ["FlextTargetOracleWmsTypes", "t"]
