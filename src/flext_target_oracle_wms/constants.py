"""FLEXT Target Oracle WMS Constants - Oracle WMS target loading constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_oracle_wms.constants import FlextOracleWmsConstants


class FlextTargetOracleWmsConstants(FlextOracleWmsConstants):
    """Oracle WMS target loading-specific constants following FLEXT unified pattern with nested domains.

    Extends FlextOracleWmsConstants to inherit all WMS constants, adding
    target-specific constants in the TargetOracleWms namespace.

    Hierarchy:
        FlextConstants (flext-core)
        └── FlextOracleWmsConstants (flext-oracle-wms)
            └── FlextTargetOracleWmsConstants (this module)

    Access patterns:
        - c.TargetOracleWms.* (target-specific constants)
        - c.WmsProcessing.* (inherited from FlextOracleWmsConstants)
        - c.Connection.* (inherited from FlextOracleWmsConstants)
        - c.Network.*, c.Errors.*, etc. (inherited from FlextConstants)
    """

    class TargetOracleWms:
        """Target Oracle WMS domain-specific constants namespace."""

        class OracleWms:
            """Oracle WMS specific constants with complete configuration."""

            # Connection defaults from parent FlextOracleWmsConstants
            DEFAULT_TIMEOUT: Final[int] = (
                FlextOracleWmsConstants.Connection.DEFAULT_TIMEOUT
            )
            DEFAULT_MAX_RETRIES: Final[int] = (
                FlextOracleWmsConstants.Connection.DEFAULT_MAX_RETRIES
            )
            DEFAULT_BATCH_SIZE: Final[int] = (
                FlextOracleWmsConstants.WmsProcessing.DEFAULT_BATCH_SIZE
            )
            DEFAULT_CONNECTION_POOL_SIZE: Final[int] = (
                FlextOracleWmsConstants.Connection.DEFAULT_POOL_SIZE
            )
            DEFAULT_CONNECTION_POOL_MAX: Final[int] = (
                FlextOracleWmsConstants.Connection.MAX_POOL_SIZE
            )

            # Connection limits
            MIN_TIMEOUT: Final[int] = 1
            MAX_TIMEOUT: Final[int] = 3600
            MIN_MAX_RETRIES: Final[int] = 0
            MAX_MAX_RETRIES: Final[int] = 10
            MIN_BATCH_SIZE: Final[int] = 1
            MAX_BATCH_SIZE: Final[int] = (
                FlextOracleWmsConstants.WmsProcessing.MAX_BATCH_SIZE
            )
            MIN_CONNECTION_POOL_SIZE: Final[int] = 1
            MAX_CONNECTION_POOL_SIZE: Final[int] = 100
            MIN_CONNECTION_POOL_MAX: Final[int] = 1
            MAX_CONNECTION_POOL_MAX: Final[int] = 100

            # String length limits
            MAX_BASE_URL_LENGTH: Final[int] = 500
            MAX_USERNAME_LENGTH: Final[int] = 128
            MAX_PASSWORD_LENGTH: Final[int] = 128
            MAX_TABLE_NAME_LENGTH: Final[int] = 128
            MAX_SCHEMA_NAME_LENGTH: Final[int] = 128

            # SSL configuration
            DEFAULT_SSL_VERIFY: Final[bool] = True
            DEFAULT_SSL_TIMEOUT: Final[int] = (
                FlextOracleWmsConstants.Connection.DEFAULT_TIMEOUT
            )

            # Performance thresholds
            PARALLEL_OPERATION_THRESHOLD: Final[int] = 5000
            HIGH_VOLUME_THRESHOLD: Final[int] = 10000

            # Validation limits
            MAX_PARALLEL_DEGREE: Final[int] = 32
            MAX_CONNECTION_TIMEOUT: Final[int] = 600

            # Location validation
            MIN_LOCATION_PARTS: Final[int] = 2

            # Processing time validation
            PROCESSING_TIME_TOLERANCE: Final[float] = 0.1

        class LoadMethods:
            """Data load method constants."""

            # Load method types
            APPEND_ONLY: Final[str] = "APPEND_ONLY"
            UPSERT: Final[str] = "UPSERT"
            REPLACE: Final[str] = "REPLACE"
            MERGE: Final[str] = "MERGE"
            TRUNCATE_INSERT: Final[str] = "TRUNCATE_INSERT"

            # Valid load methods
            VALID_LOAD_METHODS: Final[set[str]] = {
                APPEND_ONLY,
                UPSERT,
                REPLACE,
                MERGE,
                TRUNCATE_INSERT,
            }

            # Default load method
            DEFAULT_LOAD_METHOD: Final[str] = APPEND_ONLY

            # Load method descriptions
            LOAD_METHOD_DESCRIPTIONS: Final[dict[str, str]] = {
                APPEND_ONLY: "Append new records only",
                UPSERT: "Insert new records or update existing ones",
                REPLACE: "Replace all records in target table",
                MERGE: "Merge records with complex logic",
                TRUNCATE_INSERT: "Truncate table and insert all records",
            }

        class BatchProcessing:
            """Batch processing specific constants."""

            # Batch status
            BATCH_STATUS_PENDING: Final[str] = "PENDING"
            BATCH_STATUS_PROCESSING: Final[str] = "PROCESSING"
            BATCH_STATUS_COMPLETED: Final[str] = "COMPLETED"
            BATCH_STATUS_FAILED: Final[str] = "FAILED"
            BATCH_STATUS_CANCELLED: Final[str] = "CANCELLED"

            # Valid batch statuses
            VALID_BATCH_STATUSES: Final[set[str]] = {
                BATCH_STATUS_PENDING,
                BATCH_STATUS_PROCESSING,
                BATCH_STATUS_COMPLETED,
                BATCH_STATUS_FAILED,
                BATCH_STATUS_CANCELLED,
            }

            # Batch size limits from parent FlextOracleWmsConstants
            MIN_BATCH_SIZE: Final[int] = 1
            MAX_BATCH_SIZE: Final[int] = (
                FlextOracleWmsConstants.WmsProcessing.MAX_BATCH_SIZE
            )
            DEFAULT_BATCH_SIZE: Final[int] = (
                FlextOracleWmsConstants.WmsProcessing.DEFAULT_BATCH_SIZE
            )
            OPTIMAL_BATCH_SIZE: Final[int] = 5000

            # Batch processing timeouts
            DEFAULT_BATCH_TIMEOUT: Final[int] = 300  # 5 minutes
            MIN_BATCH_TIMEOUT: Final[int] = 30  # 30 seconds
            MAX_BATCH_TIMEOUT: Final[int] = 3600  # 1 hour

            # Batch retry configuration
            DEFAULT_BATCH_RETRIES: Final[int] = (
                FlextOracleWmsConstants.Connection.DEFAULT_MAX_RETRIES
            )
            MAX_BATCH_RETRIES: Final[int] = 10
            BATCH_RETRY_DELAY: Final[float] = 5.0  # seconds

        class ErrorMessages:
            """Error message constants."""

            # Connection errors
            CONNECTION_FAILED: Final[str] = "Failed to connect to Oracle WMS"
            CONNECTION_TIMEOUT: Final[str] = "Connection to Oracle WMS timed out"
            CONNECTION_REFUSED: Final[str] = "Connection to Oracle WMS was refused"
            CONNECTION_LOST: Final[str] = "Connection to Oracle WMS was lost"

            # Authentication errors
            AUTHENTICATION_FAILED: Final[str] = "Authentication to Oracle WMS failed"
            AUTHENTICATION_TIMEOUT: Final[str] = (
                "Authentication to Oracle WMS timed out"
            )
            INVALID_CREDENTIALS: Final[str] = "Invalid Oracle WMS credentials"

            # Data errors
            DATA_VALIDATION_FAILED: Final[str] = "Data validation failed"
            DATA_TRANSFORMATION_FAILED: Final[str] = "Data transformation failed"
            DATA_LOAD_FAILED: Final[str] = "Data load to Oracle WMS failed"

            # Configuration errors
            CONFIGURATION_INVALID: Final[str] = (
                "Invalid Oracle WMS target configuration"
            )
            CONFIGURATION_MISSING: Final[str] = (
                "Required Oracle WMS configuration missing"
            )
            CONFIGURATION_TYPE_ERROR: Final[str] = "Oracle WMS configuration type error"

            # Operation errors
            OPERATION_FAILED: Final[str] = "Oracle WMS target operation failed"
            OPERATION_TIMEOUT: Final[str] = "Oracle WMS target operation timed out"
            OPERATION_CANCELLED: Final[str] = (
                "Oracle WMS target operation was cancelled"
            )

            # General errors
            UNKNOWN_ERROR: Final[str] = "Unknown error occurred in Oracle WMS target"
            INTERNAL_ERROR: Final[str] = "Internal error in Oracle WMS target"
            EXTERNAL_SERVICE_ERROR: Final[str] = "External service error"
            NETWORK_ERROR: Final[str] = "Network error occurred"

    class ErrorType(StrEnum):
        """Oracle WMS target error types using StrEnum for type safety."""

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
