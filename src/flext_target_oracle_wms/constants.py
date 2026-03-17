"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final


class FlextTargetOracleWmsConstants:
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = 30
            DEFAULT_MAX_RETRIES: Final[int] = 3
            DEFAULT_BATCH_SIZE: Final[int] = 1000
            DEFAULT_CONNECTION_POOL_SIZE: Final[int] = 5
            DEFAULT_CONNECTION_POOL_MAX: Final[int] = 20
            MIN_LOCATION_PARTS: Final[int] = 2
            PROCESSING_TIME_TOLERANCE: Final[float] = 0.1

        class LoadMethods:
            """Allowed load methods."""

            APPEND_ONLY: Final[str] = "APPEND_ONLY"
            UPSERT: Final[str] = "UPSERT"
            REPLACE: Final[str] = "REPLACE"
            MERGE: Final[str] = "MERGE"
            TRUNCATE_INSERT: Final[str] = "TRUNCATE_INSERT"
            VALID_LOAD_METHODS: Final[set[str]] = {
                APPEND_ONLY,
                UPSERT,
                REPLACE,
                MERGE,
                TRUNCATE_INSERT,
            }

    @unique
    class ErrorType(StrEnum):
        """Project error categories."""

        WMS_CONNECTION = "WMS_CONNECTION"
        WMS_AUTHENTICATION = "WMS_AUTHENTICATION"
        WMS_BUSINESS_RULE = "WMS_BUSINESS_RULE"
        WMS_VALIDATION = "WMS_VALIDATION"
        SINGER_PROTOCOL = "SINGER_PROTOCOL"
        DATA_TRANSFORMATION = "DATA_TRANSFORMATION"
        PERFORMANCE = "PERFORMANCE"
        CONFIGURATION = "CONFIGURATION"

    @unique
    class ProjectType(StrEnum):
        """Project type literals for target package metadata."""

        LIBRARY = "library"
        APPLICATION = "application"
        SERVICE = "service"
        SINGER_TARGET = "singer-target"
        WMS_LOADER = "wms-loader"
        WAREHOUSE_LOADER = "warehouse-loader"
        SINGER_TARGET_ORACLE_WMS = "singer-target-oracle-wms"
        TARGET_ORACLE_WMS = "target-oracle-wms"
        WMS_CONNECTOR = "wms-connector"
        WAREHOUSE_CONNECTOR = "warehouse-connector"
        SINGER_PROTOCOL = "singer-protocol"
        WMS_INTEGRATION = "wms-integration"
        ORACLE_WMS = "oracle-wms"
        WAREHOUSE_MANAGEMENT = "warehouse-management"
        SINGER_STREAM = "singer-stream"
        ETL_TARGET = "etl-target"
        DATA_PIPELINE = "data-pipeline"
        WMS_SINK = "wms-sink"
        SINGER_INTEGRATION = "singer-integration"

    @unique
    class ErrorTypeLiteral(StrEnum):
        """Error category literals for target operations."""

        WMS_CONNECTION = "WMS_CONNECTION"
        WMS_AUTHENTICATION = "WMS_AUTHENTICATION"
        WMS_BUSINESS_RULE = "WMS_BUSINESS_RULE"
        WMS_VALIDATION = "WMS_VALIDATION"
        SINGER_PROTOCOL = "SINGER_PROTOCOL"
        DATA_TRANSFORMATION = "DATA_TRANSFORMATION"
        PERFORMANCE = "PERFORMANCE"
        CONFIGURATION = "CONFIGURATION"


c = FlextTargetOracleWmsConstants
__all__ = ["FlextTargetOracleWmsConstants", "c"]
