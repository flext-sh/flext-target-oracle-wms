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

from collections.abc import Mapping, Sequence

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants as _c


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """Singer Oracle WMS target-specific type definitions extending FlextMeltanoTypes.

    Domain-specific type system for Singer Oracle WMS target operations.
    Contains ONLY complex Oracle WMS target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetOracleWms:
        """Singer target protocol complex types."""

        type TargetConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type MessageProcessing = Mapping[
            str,
            str | Sequence[Mapping[str, FlextOracleWmsTypes.Container]],
        ]
        type RecordHandling = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container] | bool,
        ]
        type StateManagement = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type BatchProcessing = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type FacilityDefinition = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type LocationManagement = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ZoneConfiguration = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type WarehouseMetadata = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type LayoutDefinition = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ItemMasterData = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StockLevelTracking = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type AllocationManagement = Mapping[
            str,
            int | str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type InventoryMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type CycleCountData = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type OrderProcessing = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type FulfillmentWorkflow = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type PickingInstructions = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ShippingConfiguration = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type OrderTracking = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type WorkforceManagement = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type TaskAssignment = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ProductivityMetrics = Mapping[
            str,
            float | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type PerformanceTracking = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type WorkforceScheduling = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type CarrierManagement = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ShipmentTracking = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type DeliveryScheduling = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type TransportMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type RouteOptimization = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type FieldMapping = Mapping[
            str,
            str
            | FlextOracleWmsTypes.StrSequence
            | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type DataValidation = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type TypeConversion = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type FilteringRules = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type TransformationResult = Mapping[
            str,
            Mapping[str, FlextOracleWmsTypes.Container],
        ]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = Mapping[
            str,
            str | bool | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamMetadata = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamRecord = Mapping[
            str,
            FlextOracleWmsTypes.Container | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamState = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamBookmark = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type StreamSchema = Mapping[
            str,
            str | Mapping[str, FlextOracleWmsTypes.Container] | bool,
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = Mapping[
            str,
            bool | str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ErrorRecovery = Mapping[
            str,
            str | bool | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ErrorReporting = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ErrorClassification = Mapping[
            str,
            str | int | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ErrorMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type ErrorTracking = Sequence[
            Mapping[str, str | int | Mapping[str, FlextOracleWmsTypes.Container]]
        ]

    class Project:
        """Singer Target Oracle WMS-specific project types.

        Adds Singer target Oracle WMS-specific project types.
        Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        type ProjectType = _c.TargetOracleWms.ProjectType
        type ErrorTypeLiteral = _c.TargetOracleWms.ErrorTypeLiteral
        type SingerTargetOracleWmsProjectConfig = Mapping[
            str,
            FlextOracleWmsTypes.Container,
        ]
        type WmsLoaderConfig = Mapping[
            str,
            FlextOracleWmsTypes.Scalar | FlextOracleWmsTypes.StrSequence,
        ]
        type SingerProtocolConfig = Mapping[
            str,
            bool | str | Mapping[str, FlextOracleWmsTypes.Container],
        ]
        type TargetOracleWmsPipelineConfig = Mapping[str, FlextOracleWmsTypes.Container]


t = FlextTargetOracleWmsTypes
__all__ = ["FlextTargetOracleWmsTypes", "t"]
