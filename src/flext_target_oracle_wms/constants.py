"""FLEXT Target Oracle WMS Constants - Oracle WMS target loading constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_oracle_wms.constants import FlextOracleWmsConstants

from flext_core import FlextConstants


class FlextTargetOracleWmsConstants(FlextConstants):
    """Oracle WMS target loading-specific constants following flext-core patterns.

    Enhanced Oracle WMS Target constants extending FlextConstants with
    comprehensive organization, validation limits, and security considerations.

    Composes with FlextOracleWmsConstants to avoid duplication and ensure consistency.
    """

    PROJECT_VERSION: Final[str] = "1.0.0"
    PROJECT_DESCRIPTION: Final[str] = "Oracle WMS target for FLEXT data pipeline"

    class OracleWms:
        """Oracle WMS specific constants with comprehensive configuration."""

        # Connection defaults from FlextOracleWmsConstants
        DEFAULT_TIMEOUT: Final[int] = FlextOracleWmsConstants.Connection.DEFAULT_TIMEOUT
        DEFAULT_MAX_RETRIES: Final[int] = (
            FlextOracleWmsConstants.Connection.DEFAULT_MAX_RETRIES
        )
        DEFAULT_BATCH_SIZE: Final[int] = (
            FlextOracleWmsConstants.Processing.DEFAULT_BATCH_SIZE
        )
        DEFAULT_CONNECTION_POOL_SIZE: Final[int] = (
            FlextOracleWmsConstants.Connection.DEFAULT_POOL_SIZE
        )
        DEFAULT_CONNECTION_POOL_MAX: Final[int] = (
            FlextOracleWmsConstants.Connection.MAX_POOL_SIZE
        )

        # Connection limits
        MIN_TIMEOUT: Final[int] = 1
        MAX_TIMEOUT: Final[int] = FlextOracleWmsConstants.Connection.MAX_TIMEOUT
        MIN_MAX_RETRIES: Final[int] = 0
        MAX_MAX_RETRIES: Final[int] = 10
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = FlextOracleWmsConstants.Processing.MAX_BATCH_SIZE
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

        # API configuration from FlextOracleWmsConstants
        DEFAULT_API_VERSION: Final[str] = FlextOracleWmsConstants.Api.DEFAULT_VERSION
        SUPPORTED_API_VERSIONS: Final[list[str]] = (
            FlextOracleWmsConstants.Api.SUPPORTED_VERSIONS
        )

        # SSL configuration
        DEFAULT_SSL_VERIFY: Final[bool] = True
        DEFAULT_SSL_TIMEOUT: Final[int] = (
            FlextOracleWmsConstants.Connection.DEFAULT_TIMEOUT
        )

        # Performance thresholds from FlextOracleWmsConstants
        BULK_OPERATION_THRESHOLD: Final[int] = (
            FlextOracleWmsConstants.Processing.BULK_THRESHOLD
        )
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

        # Batch size limits from FlextOracleWmsConstants
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = FlextOracleWmsConstants.Processing.MAX_BATCH_SIZE
        DEFAULT_BATCH_SIZE: Final[int] = (
            FlextOracleWmsConstants.Processing.DEFAULT_BATCH_SIZE
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
        CONNECTION_FAILED = "Failed to connect to Oracle WMS"
        CONNECTION_TIMEOUT = "Connection to Oracle WMS timed out"
        CONNECTION_REFUSED = "Connection to Oracle WMS was refused"
        CONNECTION_LOST = "Connection to Oracle WMS was lost"

        # Authentication errors
        AUTHENTICATION_FAILED = "Authentication to Oracle WMS failed"
        AUTHENTICATION_TIMEOUT = "Authentication to Oracle WMS timed out"
        INVALID_CREDENTIALS = "Invalid Oracle WMS credentials"

        # Data errors
        DATA_VALIDATION_FAILED = "Data validation failed"
        DATA_TRANSFORMATION_FAILED = "Data transformation failed"
        DATA_LOAD_FAILED = "Data load to Oracle WMS failed"

        # Configuration errors
        CONFIGURATION_INVALID = "Invalid Oracle WMS target configuration"
        CONFIGURATION_MISSING = "Required Oracle WMS configuration missing"
        CONFIGURATION_TYPE_ERROR = "Oracle WMS configuration type error"

        # Operation errors
        OPERATION_FAILED = "Oracle WMS target operation failed"
        OPERATION_TIMEOUT = "Oracle WMS target operation timed out"
        OPERATION_CANCELLED = "Oracle WMS target operation was cancelled"

        # General errors
        UNKNOWN_ERROR = "Unknown error occurred in Oracle WMS target"
        INTERNAL_ERROR = "Internal error in Oracle WMS target"
        EXTERNAL_SERVICE_ERROR = "External service error"
        NETWORK_ERROR = "Network error occurred"


__all__ = ["FlextTargetOracleWmsConstants"]
