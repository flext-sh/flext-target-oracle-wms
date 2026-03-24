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

from flext_core import FlextTypes
from flext_db_oracle import FlextDbOracleTypes
from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants as _c


class FlextTargetOracleWmsTypes(
    FlextMeltanoTypes, FlextOracleWmsTypes, FlextDbOracleTypes
):
    """Singer Oracle WMS target-specific type definitions extending FlextMeltanoTypes.

    Domain-specific type system for Singer Oracle WMS target operations.
    Contains ONLY complex Oracle WMS target-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TargetOracleWms:
        """Singer target protocol complex types."""

        type TargetConfiguration = Mapping[
            str, t.Scalar | Mapping[str, FlextTypes.Container]
        ]
        type StreamConfiguration = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type MessageProcessing = Mapping[
            str, str | Sequence[Mapping[str, FlextTypes.Container]]
        ]
        type RecordHandling = Mapping[
            str, str | Mapping[str, FlextTypes.Container] | bool
        ]
        type StateManagement = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type BatchProcessing = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]

    class WmsWarehouse:
        """Oracle WMS warehouse management complex types."""

        type WarehouseConfiguration = Mapping[
            str, t.Scalar | Mapping[str, FlextTypes.Container]
        ]
        type FacilityDefinition = Mapping[
            str, str | Sequence[str] | Mapping[str, FlextTypes.Container]
        ]
        type LocationManagement = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type ZoneConfiguration = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type WarehouseMetadata = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type LayoutDefinition = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]

    class WmsInventory:
        """Oracle WMS inventory management complex types."""

        type InventoryConfiguration = Mapping[
            str, t.Scalar | Mapping[str, FlextTypes.Container]
        ]
        type ItemMasterData = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type StockLevelTracking = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type AllocationManagement = Mapping[
            str, int | str | Mapping[str, FlextTypes.Container]
        ]
        type InventoryMetrics = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type CycleCountData = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]

    class WmsOrderManagement:
        """Oracle WMS order management complex types."""

        type OrderConfiguration = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]
        type OrderProcessing = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type FulfillmentWorkflow = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]
        type PickingInstructions = Mapping[
            str, str | Mapping[str, FlextTypes.Container]
        ]
        type ShippingConfiguration = Mapping[
            str, bool | str | Mapping[str, FlextTypes.Container]
        ]
        type OrderTracking = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]

    class WmsLaborManagement:
        """Oracle WMS labor management complex types."""

        type LaborConfiguration = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type WorkforceManagement = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type TaskAssignment = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type ProductivityMetrics = Mapping[
            str, float | int | Mapping[str, FlextTypes.Container]
        ]
        type PerformanceTracking = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type WorkforceScheduling = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]

    class WmsTransportation:
        """Oracle WMS transportation management complex types."""

        type TransportConfiguration = Mapping[
            str, t.Scalar | Mapping[str, FlextTypes.Container]
        ]
        type CarrierManagement = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type ShipmentTracking = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type DeliveryScheduling = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type TransportMetrics = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type RouteOptimization = Mapping[
            str, str | Sequence[str] | Mapping[str, FlextTypes.Container]
        ]

    class DataTransformation:
        """Data transformation complex types."""

        type TransformationConfiguration = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type FieldMapping = Mapping[
            str, str | Sequence[str] | Mapping[str, FlextTypes.Container]
        ]
        type DataValidation = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type TypeConversion = Mapping[
            str, bool | str | Mapping[str, FlextTypes.Container]
        ]
        type FilteringRules = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type TransformationResult = Mapping[str, Mapping[str, FlextTypes.Container]]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = Mapping[
            str, str | bool | int | Mapping[str, FlextTypes.Container]
        ]
        type StreamMetadata = Mapping[str, str | Mapping[str, FlextTypes.Container]]
        type StreamRecord = Mapping[
            str,
            FlextTypes.Container | Mapping[str, FlextTypes.Container],
        ]
        type StreamState = Mapping[str, str | int | Mapping[str, FlextTypes.Container]]
        type StreamBookmark = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]
        type StreamSchema = Mapping[
            str, str | Mapping[str, FlextTypes.Container] | bool
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = Mapping[
            str, bool | str | int | Mapping[str, FlextTypes.Container]
        ]
        type ErrorRecovery = Mapping[
            str, str | bool | Mapping[str, FlextTypes.Container]
        ]
        type ErrorReporting = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]
        type ErrorClassification = Mapping[
            str, str | int | Mapping[str, FlextTypes.Container]
        ]
        type ErrorMetrics = Mapping[
            str, int | float | Mapping[str, FlextTypes.Container]
        ]
        type ErrorTracking = Sequence[
            Mapping[str, str | int | Mapping[str, FlextTypes.Container]]
        ]

    class Project:
        """Singer Target Oracle WMS-specific project types.

        Adds Singer target Oracle WMS-specific project types.
        Follows domain separation principle:
        Singer target Oracle WMS domain owns WMS loading and Singer protocol-specific types.
        """

        type ProjectType = _c.ProjectType
        type ErrorTypeLiteral = _c.ErrorTypeLiteral
        type SingerTargetOracleWmsProjectConfig = Mapping[str, FlextTypes.Container]
        type WmsLoaderConfig = Mapping[str, t.Scalar | Sequence[str]]
        type SingerProtocolConfig = Mapping[
            str, bool | str | Mapping[str, FlextTypes.Container]
        ]
        type TargetOracleWmsPipelineConfig = Mapping[str, FlextTypes.Container]


t = FlextTargetOracleWmsTypes
__all__ = ["FlextTargetOracleWmsTypes", "t"]
