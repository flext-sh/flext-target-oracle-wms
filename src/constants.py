"""Enhanced Oracle WMS Target constants extending FlextConstants.

Contains comprehensive constants for Oracle WMS target operations with
enhanced organization, validation limits, and security considerations.
"""

from __future__ import annotations

from typing import Any, Final

from flext_core import FlextConstants

# Re-export for convenience
__all__ = ["FlextTargetOracleWmsConstants"]


class FlextTargetOracleWmsConstants(FlextConstants):
    """Enhanced Oracle WMS Target constants extending FlextConstants.

    Contains comprehensive constants for Oracle WMS target operations with
    enhanced organization, validation limits, and security considerations.
    """

    # Project identification
    PROJECT_PREFIX: Final[str] = "FLEXT_TARGET_ORACLE_WMS"
    PROJECT_NAME: Final[str] = "FLEXT Oracle WMS Target"
    PROJECT_VERSION: Final[str] = "1.0.0"
    PROJECT_DESCRIPTION: Final[str] = "Oracle WMS target for FLEXT data pipeline"

    # Oracle WMS Connection Configuration
    class OracleWMS:
        """Oracle WMS specific constants with comprehensive configuration."""

        # Connection defaults
        DEFAULT_TIMEOUT: Final[int] = 30
        DEFAULT_MAX_RETRIES: Final[int] = 3
        DEFAULT_BATCH_SIZE: Final[int] = 1000
        DEFAULT_CONNECTION_POOL_SIZE: Final[int] = 10
        DEFAULT_CONNECTION_POOL_MAX: Final[int] = 20

        # Connection limits
        MIN_TIMEOUT: Final[int] = 1
        MAX_TIMEOUT: Final[int] = 3600
        MIN_MAX_RETRIES: Final[int] = 0
        MAX_MAX_RETRIES: Final[int] = 10
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = 100000
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

        # API configuration
        DEFAULT_API_VERSION: Final[str] = "LGF_V10"
        SUPPORTED_API_VERSIONS: Final[list[str]] = ["LGF_V10", "LGF_V11", "LGF_V12"]

        # SSL configuration
        DEFAULT_SSL_VERIFY: Final[bool] = True
        DEFAULT_SSL_TIMEOUT: Final[int] = 30

    # Target Operation Configuration
    class TargetOperations:
        """Target operation specific constants."""

        # Operation types
        OPERATION_LOAD: Final[str] = "LOAD"
        OPERATION_SYNC: Final[str] = "SYNC"
        OPERATION_VALIDATE: Final[str] = "VALIDATE"
        OPERATION_CLEANUP: Final[str] = "CLEANUP"

        # Valid operation types
        VALID_OPERATION_TYPES: Final[set[str]] = {
            OPERATION_LOAD,
            OPERATION_SYNC,
            OPERATION_VALIDATE,
            OPERATION_CLEANUP,
        }

        # Operation status
        STATUS_PENDING: Final[str] = "PENDING"
        STATUS_RUNNING: Final[str] = "RUNNING"
        STATUS_COMPLETED: Final[str] = "COMPLETED"
        STATUS_FAILED: Final[str] = "FAILED"
        STATUS_CANCELLED: Final[str] = "CANCELLED"

        # Valid operation statuses
        VALID_OPERATION_STATUSES: Final[set[str]] = {
            STATUS_PENDING,
            STATUS_RUNNING,
            STATUS_COMPLETED,
            STATUS_FAILED,
            STATUS_CANCELLED,
        }

        # Operation timeouts
        DEFAULT_OPERATION_TIMEOUT: Final[int] = 300  # 5 minutes
        MIN_OPERATION_TIMEOUT: Final[int] = 30  # 30 seconds
        MAX_OPERATION_TIMEOUT: Final[int] = 3600  # 1 hour

    # Data Load Methods
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

    # Batch Processing Configuration
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

        # Batch size limits
        MIN_BATCH_SIZE: Final[int] = 1
        MAX_BATCH_SIZE: Final[int] = 100000
        DEFAULT_BATCH_SIZE: Final[int] = 1000
        OPTIMAL_BATCH_SIZE: Final[int] = 5000

        # Batch processing timeouts
        DEFAULT_BATCH_TIMEOUT: Final[int] = 300  # 5 minutes
        MIN_BATCH_TIMEOUT: Final[int] = 30  # 30 seconds
        MAX_BATCH_TIMEOUT: Final[int] = 3600  # 1 hour

        # Batch retry configuration
        DEFAULT_BATCH_RETRIES: Final[int] = 3
        MAX_BATCH_RETRIES: Final[int] = 10
        BATCH_RETRY_DELAY: Final[float] = 5.0  # seconds

    # Record Processing Configuration
    class RecordProcessing:
        """Record processing specific constants."""

        # Record operation types
        RECORD_OPERATION_INSERT: Final[str] = "INSERT"
        RECORD_OPERATION_UPDATE: Final[str] = "UPDATE"
        RECORD_OPERATION_DELETE: Final[str] = "DELETE"
        RECORD_OPERATION_UPSERT: Final[str] = "UPSERT"

        # Valid record operations
        VALID_RECORD_OPERATIONS: Final[set[str]] = {
            RECORD_OPERATION_INSERT,
            RECORD_OPERATION_UPDATE,
            RECORD_OPERATION_DELETE,
            RECORD_OPERATION_UPSERT,
        }

        # Default record operation
        DEFAULT_RECORD_OPERATION: Final[str] = RECORD_OPERATION_INSERT

        # Record validation
        MAX_RECORD_DATA_SIZE: Final[int] = 10 * 1024 * 1024  # 10MB
        MIN_RECORD_DATA_SIZE: Final[int] = 1  # 1 byte
        MAX_RECORD_FIELDS: Final[int] = 1000
        MIN_RECORD_FIELDS: Final[int] = 1

        # Record ID generation
        RECORD_ID_LENGTH: Final[int] = 36  # UUID length
        RECORD_ID_ALPHABET: Final[str] = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
        )

    # Performance Configuration
    class Performance:
        """Performance configuration constants."""

        # Throughput limits
        DEFAULT_RECORDS_PER_SECOND: Final[int] = 100
        MAX_RECORDS_PER_SECOND: Final[int] = 10000
        MIN_RECORDS_PER_SECOND: Final[int] = 1

        # Memory limits
        DEFAULT_MEMORY_LIMIT_MB: Final[int] = 1024
        MAX_MEMORY_LIMIT_MB: Final[int] = 8192
        MIN_MEMORY_LIMIT_MB: Final[int] = 256

        # CPU limits
        DEFAULT_CPU_LIMIT_PERCENT: Final[int] = 80
        MAX_CPU_LIMIT_PERCENT: Final[int] = 100
        MIN_CPU_LIMIT_PERCENT: Final[int] = 10

        # Connection limits
        DEFAULT_MAX_CONNECTIONS: Final[int] = 100
        MAX_MAX_CONNECTIONS: Final[int] = 1000
        MIN_MAX_CONNECTIONS: Final[int] = 1

        # Parallel processing
        DEFAULT_MAX_WORKERS: Final[int] = 4
        MAX_MAX_WORKERS: Final[int] = 32
        MIN_MAX_WORKERS: Final[int] = 1

        # Performance thresholds
        PERFORMANCE_WARNING_THRESHOLD: Final[float] = 1000.0  # milliseconds
        PERFORMANCE_CRITICAL_THRESHOLD: Final[float] = 5000.0  # milliseconds
        MEMORY_WARNING_THRESHOLD: Final[float] = 80.0  # percentage
        MEMORY_CRITICAL_THRESHOLD: Final[float] = 95.0  # percentage

    # Security Configuration
    class Security:
        """Security configuration constants."""

        # Encryption
        DEFAULT_ENCRYPTION_ENABLED: Final[bool] = False
        MIN_ENCRYPTION_KEY_LENGTH: Final[int] = 32
        MAX_ENCRYPTION_KEY_LENGTH: Final[int] = 256
        DEFAULT_ENCRYPTION_ALGORITHM: Final[str] = "AES-256-GCM"

        # Authentication
        DEFAULT_AUTH_TIMEOUT: Final[int] = 300  # 5 minutes
        MAX_AUTH_ATTEMPTS: Final[int] = 5
        AUTH_LOCKOUT_DURATION: Final[int] = 900  # 15 minutes

        # SSL/TLS
        DEFAULT_SSL_VERIFY: Final[bool] = True
        DEFAULT_SSL_TIMEOUT: Final[int] = 30
        SUPPORTED_SSL_PROTOCOLS: Final[list[str]] = ["TLSv1.2", "TLSv1.3"]

        # Audit logging
        DEFAULT_AUDIT_LOGGING: Final[bool] = True
        AUDIT_LOG_RETENTION_DAYS: Final[int] = 90

        # Data masking
        DEFAULT_DATA_MASKING: Final[bool] = True
        SENSITIVE_FIELD_PATTERNS: Final[list[str]] = [
            "password",
            "secret",
            "key",
            "token",
            "credential",
        ]

    # Error Handling Configuration
    class ErrorHandling:
        """Error handling configuration constants."""

        # Error types
        ERROR_TYPE_VALIDATION: Final[str] = "VALIDATION_ERROR"
        ERROR_TYPE_CONNECTION: Final[str] = "CONNECTION_ERROR"
        ERROR_TYPE_TIMEOUT: Final[str] = "TIMEOUT_ERROR"
        ERROR_TYPE_AUTHENTICATION: Final[str] = "AUTHENTICATION_ERROR"
        ERROR_TYPE_AUTHORIZATION: Final[str] = "AUTHORIZATION_ERROR"
        ERROR_TYPE_DATA: Final[str] = "DATA_ERROR"
        ERROR_TYPE_SYSTEM: Final[str] = "SYSTEM_ERROR"

        # Valid error types
        VALID_ERROR_TYPES: Final[set[str]] = {
            ERROR_TYPE_VALIDATION,
            ERROR_TYPE_CONNECTION,
            ERROR_TYPE_TIMEOUT,
            ERROR_TYPE_AUTHENTICATION,
            ERROR_TYPE_AUTHORIZATION,
            ERROR_TYPE_DATA,
            ERROR_TYPE_SYSTEM,
        }

        # Error retry configuration
        DEFAULT_ERROR_RETRIES: Final[int] = 3
        MAX_ERROR_RETRIES: Final[int] = 10
        ERROR_RETRY_DELAY: Final[float] = 5.0  # seconds
        ERROR_RETRY_BACKOFF_MULTIPLIER: Final[float] = 2.0

        # Error logging
        DEFAULT_ERROR_LOGGING: Final[bool] = True
        MAX_ERROR_MESSAGE_LENGTH: Final[int] = 1000
        ERROR_LOG_RETENTION_DAYS: Final[int] = 30

    # Monitoring Configuration
    class Monitoring:
        """Monitoring configuration constants."""

        # Metrics collection
        DEFAULT_METRICS_INTERVAL: Final[int] = 60  # seconds
        MIN_METRICS_INTERVAL: Final[int] = 10  # seconds
        MAX_METRICS_INTERVAL: Final[int] = 3600  # 1 hour

        # Health checks
        DEFAULT_HEALTH_CHECK_INTERVAL: Final[int] = 30  # seconds
        HEALTH_CHECK_TIMEOUT: Final[int] = 5  # seconds
        HEALTH_CHECK_RETRIES: Final[int] = 3

        # Performance monitoring
        DEFAULT_PERFORMANCE_MONITORING: Final[bool] = True
        PERFORMANCE_METRICS_RETENTION_DAYS: Final[int] = 30

        # Alert thresholds
        DEFAULT_ALERT_THRESHOLD: Final[float] = 1000.0  # milliseconds
        CRITICAL_ALERT_THRESHOLD: Final[float] = 5000.0  # milliseconds
        ERROR_RATE_THRESHOLD: Final[float] = 5.0  # percentage

    # Plugin System Configuration
    class PluginSystem:
        """Plugin system configuration constants."""

        # Plugin types
        PLUGIN_TYPE_TRANSFORMER: Final[str] = "TRANSFORMER"
        PLUGIN_TYPE_VALIDATOR: Final[str] = "VALIDATOR"
        PLUGIN_TYPE_FILTER: Final[str] = "FILTER"
        PLUGIN_TYPE_ENRICHER: Final[str] = "ENRICHER"

        # Valid plugin types
        VALID_PLUGIN_TYPES: Final[set[str]] = {
            PLUGIN_TYPE_TRANSFORMER,
            PLUGIN_TYPE_VALIDATOR,
            PLUGIN_TYPE_FILTER,
            PLUGIN_TYPE_ENRICHER,
        }

        # Plugin configuration
        DEFAULT_PLUGIN_ENABLED: Final[bool] = False
        DEFAULT_PLUGIN_DIRECTORY: Final[str] = "./plugins"
        DEFAULT_PLUGIN_TIMEOUT: Final[int] = 30  # seconds
        MAX_PLUGIN_TIMEOUT: Final[int] = 300  # 5 minutes
        MIN_PLUGIN_TIMEOUT: Final[int] = 1  # 1 second

        # Plugin limits
        MAX_PLUGINS_PER_OPERATION: Final[int] = 10
        MAX_PLUGIN_MEMORY_MB: Final[int] = 512
        MAX_PLUGIN_CPU_PERCENT: Final[int] = 50

    # Testing Configuration
    class Testing:
        """Testing configuration constants."""

        # Test modes
        TEST_MODE_MOCK: Final[str] = "MOCK"
        TEST_MODE_INTEGRATION: Final[str] = "INTEGRATION"
        TEST_MODE_UNIT: Final[str] = "UNIT"

        # Valid test modes
        VALID_TEST_MODES: Final[set[str]] = {
            TEST_MODE_MOCK,
            TEST_MODE_INTEGRATION,
            TEST_MODE_UNIT,
        }

        # Test data configuration
        DEFAULT_TEST_DATA_SIZE: Final[int] = 100
        MAX_TEST_DATA_SIZE: Final[int] = 10000
        MIN_TEST_DATA_SIZE: Final[int] = 1

        # Test timeouts
        DEFAULT_TEST_TIMEOUT: Final[int] = 30  # seconds
        MAX_TEST_TIMEOUT: Final[int] = 300  # 5 minutes
        MIN_TEST_TIMEOUT: Final[int] = 1  # 1 second

        # Test environments
        TEST_ENVIRONMENT_LOCAL: Final[str] = "local"
        TEST_ENVIRONMENT_CI: Final[str] = "ci"
        TEST_ENVIRONMENT_STAGING: Final[str] = "staging"

        # Valid test environments
        VALID_TEST_ENVIRONMENTS: Final[set[str]] = {
            TEST_ENVIRONMENT_LOCAL,
            TEST_ENVIRONMENT_CI,
            TEST_ENVIRONMENT_STAGING,
        }

    # Environment Configuration
    class Environment:
        """Environment configuration constants."""

        # Environment types
        ENV_DEVELOPMENT: Final[str] = "development"
        ENV_STAGING: Final[str] = "staging"
        ENV_PRODUCTION: Final[str] = "production"
        ENV_TESTING: Final[str] = "testing"
        ENV_LOCAL: Final[str] = "local"

        # Valid environments
        VALID_ENVIRONMENTS: Final[set[str]] = {
            ENV_DEVELOPMENT,
            ENV_STAGING,
            ENV_PRODUCTION,
            ENV_TESTING,
            ENV_LOCAL,
        }

        # Environment-specific defaults
        ENV_DEFAULTS: Final[dict[str, dict[str, Any]]] = {
            ENV_DEVELOPMENT: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": True,
                "batch_size": 100,
                "timeout": 30,
                "max_retries": 3,
            },
            ENV_STAGING: {
                "debug_mode": False,
                "verify_ssl": True,
                "enable_logging": True,
                "batch_size": 500,
                "timeout": 60,
                "max_retries": 5,
            },
            ENV_PRODUCTION: {
                "debug_mode": False,
                "verify_ssl": True,
                "enable_logging": True,
                "batch_size": 1000,
                "timeout": 120,
                "max_retries": 10,
            },
            ENV_TESTING: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": False,
                "batch_size": 10,
                "timeout": 15,
                "max_retries": 1,
            },
            ENV_LOCAL: {
                "debug_mode": True,
                "verify_ssl": False,
                "enable_logging": True,
                "batch_size": 50,
                "timeout": 30,
                "max_retries": 2,
            },
        }

    # Validation Configuration
    class Validation:
        """Validation configuration constants."""

        # String length limits
        MIN_NAME_LENGTH: Final[int] = 1
        MAX_NAME_LENGTH: Final[int] = 255
        MIN_DESCRIPTION_LENGTH: Final[int] = 0
        MAX_DESCRIPTION_LENGTH: Final[int] = 1000

        # Numeric limits
        MIN_PERCENTAGE: Final[float] = 0.0
        MAX_PERCENTAGE: Final[float] = 100.0
        MIN_COUNT: Final[int] = 0
        MAX_COUNT: Final[int] = 1000000

        # URL validation
        MIN_URL_LENGTH: Final[int] = 1
        MAX_URL_LENGTH: Final[int] = 500

        # Table and schema validation
        MIN_TABLE_NAME_LENGTH: Final[int] = 1
        MAX_TABLE_NAME_LENGTH: Final[int] = 128
        MIN_SCHEMA_NAME_LENGTH: Final[int] = 1
        MAX_SCHEMA_NAME_LENGTH: Final[int] = 128

        # Validation patterns
        TABLE_NAME_PATTERN: Final[str] = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        SCHEMA_NAME_PATTERN: Final[str] = r"^[a-zA-Z][a-zA-Z0-9_]*$"
        ENVIRONMENT_PATTERN: Final[str] = r"^[a-zA-Z][a-zA-Z0-9_]*$"

    # Error Messages
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

        # Batch errors
        BATCH_PROCESSING_FAILED = "Batch processing failed"
        BATCH_VALIDATION_FAILED = "Batch validation failed"
        BATCH_SIZE_INVALID = "Invalid batch size"

        # Record errors
        RECORD_VALIDATION_FAILED = "Record validation failed"
        RECORD_TRANSFORMATION_FAILED = "Record transformation failed"
        RECORD_INSERT_FAILED = "Record insert failed"

        # General errors
        UNKNOWN_ERROR = "Unknown error occurred in Oracle WMS target"
        INTERNAL_ERROR = "Internal error in Oracle WMS target"
        EXTERNAL_SERVICE_ERROR = "External service error"
        NETWORK_ERROR = "Network error occurred"
