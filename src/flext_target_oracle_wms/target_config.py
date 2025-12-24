"""Target configuration module for Oracle WMS Target.

Provides configuration models, validation logic, and environment management
for Oracle WMS target operations with flext-core integration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import warnings
from datetime import datetime
from pathlib import Path
from typing import ClassVar, Self

from flext import FlextConstants,
    FlextLogger,
    FlextResult,
    FlextSettings,
    t
from flext_meltano import SingerConstants
from flext_oracle_wms import FlextOracleWmsApiVersion, FlextOracleWmsClientSettings
from pydantic import (
    AnyUrl,
    Field,
    SettingsConfigDict,
    ValidationInfo,
    computed_field,
    field_validator,
    model_validator,
)

from flext_target_oracle_wms.constants import c

logger = FlextLogger(__name__)


class FlextTargetOracleWmsSettings(FlextSettings):
    """Enhanced Oracle WMS Target Configuration extending FlextSettings.

    Provides complete configuration for Oracle WMS target operations
    with automatic validation, type safety, and enhanced Pydantic 2.11 features.
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_",
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
        use_enum_values=True,
        frozen=False,
        # Enhanced Pydantic 2.11 features
        arbitrary_types_allowed=True,
        validate_return=True,
        serialize_by_alias=True,
        populate_by_name=True,
        ser_json_timedelta="iso8601",
        ser_json_bytes="base64",
        str_strip_whitespace=True,
        defer_build=False,
        coerce_numbers_to_str=False,
        validate_default=True,
        enable_decoding=True,
        nested_model_default_partial_update=True,
        cli_parse_args=False,
        cli_avoid_json=True,
        # Custom encoders for complex types
        json_encoders={
            Path: "str",
            datetime: lambda dt: dt.isoformat(),
        },
    )

    # Oracle WMS Connection with enhanced validation
    base_url: AnyUrl = Field(
        description="Oracle WMS base URL",
        examples=["https://invalid.wms.ocs.oraclecloud.com"],
        min_length=1,
        max_length=500,
    )
    username: str = Field(
        description="Oracle WMS username",
        examples=["wms_user"],
        min_length=1,
        max_length=128,
    )
    password: str = Field(
        description="Oracle WMS password",
        repr=False,  # Hide in string representation for security
        min_length=1,
        max_length=128,
    )
    environment: str = Field(
        default=FlextConstants.Defaults.ENVIRONMENT,
        description="Environment identifier",
        examples=["development", "staging", "production"],
        min_length=1,
        max_length=50,
    )

    # Enhanced Connection Settings
    timeout: float = Field(
        default=FlextConstants.Network.DEFAULT_TIMEOUT,
        description="Request timeout in seconds",
        gt=0,
        le=3600,
    )
    max_retries: int = Field(
        default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
        description="Maximum retry attempts",
        ge=0,
        le=10,
    )
    verify_ssl: bool = Field(
        default=True,
        description="Verify SSL certificates",
    )
    enable_logging: bool = Field(
        default=True,
        description="Enable request/response logging",
    )
    connection_pool_size: int = Field(
        default=FlextConstants.Performance.DEFAULT_DB_POOL_SIZE,
        description="Connection pool size",
        ge=1,
        le=100,
    )
    connection_pool_max: int = Field(
        default=FlextConstants.Performance.MAX_DB_POOL_SIZE,
        description="Maximum connection pool size",
        ge=1,
        le=100,
    )

    # Enhanced Target Settings
    batch_size: int = Field(
        default=FlextConstants.Performance.DEFAULT_BATCH_SIZE,
        description="Batch size for record processing",
        gt=0,
        le=100000,
    )
    load_method: str = Field(
        default=c.TargetOracleWms.LoadMethods.APPEND_ONLY,
        description="Data load method",
        min_length=1,
        max_length=50,
    )
    table_prefix: str = Field(
        default="",
        description="Prefix for generated table names",
        max_length=50,
    )
    default_target_schema: str = Field(
        default="WMS_TARGET",
        description="Default schema for target tables",
        min_length=1,
        max_length=128,
    )
    enable_transactions: bool = Field(
        default=True,
        description="Enable database transactions",
    )
    transaction_timeout: int = Field(
        default=300,
        description="Transaction timeout in seconds",
        ge=1,
        le=3600,
    )

    # Enhanced Plugin System
    enable_plugins: bool = Field(
        default=False,
        description="Enable plugin system",
    )
    plugin_directory: str = Field(
        default="./plugins",
        description="Directory for plugins",
        max_length=500,
    )
    plugin_timeout: int = Field(
        default=30,
        description="Plugin execution timeout in seconds",
        ge=1,
        le=300,
    )

    # Enhanced Testing and Development
    mock_mode: bool = Field(
        default=False,
        description="Enable mock mode for testing",
    )
    debug_mode: bool = Field(
        default=False,
        description="Enable debug mode",
    )
    test_data_size: int = Field(
        default=100,
        description="Size of test data sets",
        ge=1,
        le=10000,
    )

    # Enhanced Performance Settings
    parallel_processing: bool = Field(
        default=False,
        description="Enable parallel processing",
    )
    max_workers: int = Field(
        default=FlextConstants.Container.MAX_WORKERS,
        description="Maximum number of worker threads",
        ge=1,
        le=32,
    )
    memory_limit_mb: int = Field(
        default=1024,
        description="Memory limit in megabytes",
        ge=256,
        le=8192,
    )

    # Enhanced Security Settings
    encryption_enabled: bool = Field(
        default=False,
        description="Enable data encryption",
    )
    encryption_key: str | None = Field(
        default=None,
        description="Encryption key for sensitive data",
        min_length=32,
        max_length=256,
    )
    audit_logging: bool = Field(
        default=True,
        description="Enable audit logging",
    )

    # Enhanced validation methods with Pydantic 2.11 features
    @field_validator("load_method")
    @classmethod
    def validate_load_method(cls, v: str) -> str:
        """Enhanced load method validation."""
        valid_methods = {"APPEND_ONLY", "UPSERT", "REPLACE", "MERGE", "TRUNCATE_INSERT"}
        if v.upper() not in valid_methods:
            msg = f"Invalid load_method: {v}. Must be one of {valid_methods}"
            raise ValueError(msg)
        return v.upper()

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate environment against allowed values."""
        valid_environments = [e.value for e in SingerConstants.Environment]
        if v.lower() not in [env.lower() for env in valid_environments]:
            msg = f"Invalid environment: {v}. Valid environments: {valid_environments}"
            raise ValueError(msg)
        return v.lower()

    @field_validator("connection_pool_max")
    @classmethod
    def validate_connection_pool_max(cls, v: int, info: ValidationInfo) -> int:
        """Validate connection pool max is greater than pool size."""
        if (
            "connection_pool_size" in info.data
            and v < info.data["connection_pool_size"]
        ):
            msg = "connection_pool_max must be greater than or equal to connection_pool_size"
            raise ValueError(msg)
        return v

    @field_validator("encryption_key")
    @classmethod
    def validate_encryption_key(cls, v: str | None) -> str | None:
        """Validate encryption key format."""
        if v is None:
            return None

        # Check for weak keys
        weak_keys = {"password", "secret", "key", "123456", "admin", "test"}
        if v.lower() in weak_keys:
            msg = "Encryption key is too weak"
            raise ValueError(msg)

        # Check for minimum complexity
        min_unique_chars = 8
        if len(set(v)) < min_unique_chars:  # At least 8 unique characters
            msg = "Encryption key must contain at least 8 unique characters"
            raise ValueError(msg)

        return v

    @model_validator(mode="after")
    def validate_security_settings(self) -> Self:
        """Validate security-related settings."""
        # Encryption consistency
        if self.encryption_enabled and not self.encryption_key:
            msg = "Encryption key is required when encryption is enabled"
            raise ValueError(msg)

        # SSL and encryption consistency
        if not self.verify_ssl and self.encryption_enabled:
            warnings.warn(
                "SSL verification is disabled but encryption is enabled",
                UserWarning,
                stacklevel=2,
            )

        return self

    @model_validator(mode="after")
    def validate_performance_settings(self) -> Self:
        """Validate performance-related settings."""
        # Worker count consistency
        if self.parallel_processing and self.max_workers == 1:
            warnings.warn(
                "Parallel processing is enabled but max_workers is 1",
                UserWarning,
                stacklevel=2,
            )

        # Memory and batch size consistency
        if self.batch_size > self.memory_limit_mb * 10:  # Rough estimate
            warnings.warn(
                "Batch size may be too large for available memory",
                UserWarning,
                stacklevel=2,
            )

        return self

    # Enhanced computed fields
    @computed_field
    def effective_timeout(self) -> float:
        """Calculate effective timeout considering retry attempts."""
        return self.timeout + (self.max_retries * 5.0)  # 5 seconds per retry

    @computed_field
    def connection_string(self) -> str:
        """Generate connection string for Oracle WMS."""
        return f"{self.username}@{self.base_url}"

    @computed_field
    def memory_limit_bytes(self) -> int:
        """Get memory limit in bytes."""
        return self.memory_limit_mb * 1024 * 1024

    # Enhanced preset configurations
    PRESETS: ClassVar[t.NestedDict] = {
        "development": {
            "batch_size": 100,
            "table_prefix": "DEV_",
            "default_target_schema": "WMS_DEV",
            "timeout": 30.0,
            "max_retries": 3,
            "verify_ssl": "False",
            "enable_logging": "True",
            "debug_mode": "True",
            "mock_mode": "False",
            "parallel_processing": "False",
            "max_workers": 2,
            "memory_limit_mb": 512,
            "encryption_enabled": "False",
            "audit_logging": "True",
        },
        "staging": {
            "batch_size": 500,
            "table_prefix": "STG_",
            "default_target_schema": "WMS_STAGING",
            "timeout": 60.0,
            "max_retries": 5,
            "verify_ssl": "True",
            "enable_logging": "True",
            "debug_mode": "False",
            "mock_mode": "False",
            "parallel_processing": "True",
            "max_workers": 4,
            "memory_limit_mb": 1024,
            "encryption_enabled": "True",
            "audit_logging": "True",
        },
        "production": {
            "batch_size": 1000,
            "table_prefix": "PROD_",
            "default_target_schema": "WMS_PRODUCTION",
            "timeout": 120.0,
            "max_retries": 10,
            "verify_ssl": "True",
            "enable_logging": "True",
            "debug_mode": "False",
            "mock_mode": "False",
            "parallel_processing": "True",
            "max_workers": 8,
            "memory_limit_mb": 2048,
            "encryption_enabled": "True",
            "audit_logging": "True",
        },
        "testing": {
            "batch_size": 10,
            "table_prefix": "TEST_",
            "default_target_schema": "WMS_TEST",
            "timeout": 15.0,
            "max_retries": 1,
            "verify_ssl": "False",
            "enable_logging": "False",
            "debug_mode": "True",
            "mock_mode": "True",
            "parallel_processing": "False",
            "max_workers": 1,
            "memory_limit_mb": 256,
            "encryption_enabled": "False",
            "audit_logging": "False",
        },
    }

    def to_oracle_wms_config(self) -> FlextOracleWmsClientSettings:
        """Convert to flext-oracle-wms client configuration."""
        # Map string environment to proper literal type
        env_mapping: dict[str, str] = {
            "development": "development",
            "production": "production",
            "staging": "staging",
            "test": "test",
            "local": "local",
            "default": "development",
        }

        # Get mapped environment or default to development
        mapped_env = env_mapping.get(self.environment.lower(), "development")

        return FlextOracleWmsClientSettings(
            oracle_wms_base_url=self.base_url,
            oracle_wms_username=self.username,
            oracle_wms_password=self.password,
            environment=mapped_env,
            oracle_wms_timeout=int(self.timeout),
            oracle_wms_max_retries=self.max_retries,
            api_version=FlextOracleWmsApiVersion.LGF_V10,
            oracle_wms_verify_ssl=self.verify_ssl,
            oracle_wms_enable_logging=self.enable_logging,
        )

    def validate_business_rules(self) -> FlextResult[None]:
        """Enhanced Oracle WMS configuration business rules validation."""
        try:
            # Validate timeout values
            if self.timeout <= 0:
                return FlextResult[None].fail("Timeout must be positive")

            # Validate batch size
            if self.batch_size <= 0:
                return FlextResult[None].fail("Batch size must be positive")

            # Validate load method
            valid_methods = {
                "APPEND_ONLY",
                "UPSERT",
                "REPLACE",
                "MERGE",
                "TRUNCATE_INSERT",
            }
            if self.load_method.upper() not in valid_methods:
                return FlextResult[None].fail(
                    f"Invalid load_method: {self.load_method}",
                )

            # Validate credentials are provided
            if not self.username.strip():
                return FlextResult[None].fail("Username cannot be empty")
            if not self.password.strip():
                return FlextResult[None].fail("Password cannot be empty")

            # Validate plugin settings
            if self.enable_plugins and not Path(self.plugin_directory).exists():
                return FlextResult[None].fail(
                    f"Plugin directory does not exist: {self.plugin_directory}",
                )

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Configuration validation failed: {e}")

    def apply_preset(
        self, preset_name: str,
    ) -> FlextResult[FlextTargetOracleWmsSettings]:
        """Enhanced configuration preset application."""
        try:
            if preset_name not in self.PRESETS:
                available = list(self.PRESETS.keys())
                return FlextResult[FlextTargetOracleWmsSettings].fail(
                    f"Unknown preset '{preset_name}'. Available: {available}",
                )

            preset_values = self.PRESETS[preset_name]
            updated_data = self.model_dump()
            updated_data.update(preset_values)

            updated_config = self.__class__(**updated_data)
            logger.info("Applied configuration preset: %s", preset_name)
            return FlextResult[FlextTargetOracleWmsSettings].ok(updated_config)

        except Exception as e:
            return FlextResult[FlextTargetOracleWmsSettings].fail(
                f"Failed to apply preset {preset_name}: {e}",
            )

    def get_config_summary(self) -> dict[str, object]:
        """Get complete configuration summary."""
        return {
            "connection": {
                "base_url": self.base_url,
                "username": self.username,
                "environment": self.environment,
                "timeout": self.timeout,
                "max_retries": self.max_retries,
                "verify_ssl": self.verify_ssl,
                "connection_pool_size": self.connection_pool_size,
                "connection_pool_max": self.connection_pool_max,
            },
            "target_settings": {
                "batch_size": self.batch_size,
                "load_method": self.load_method,
                "table_prefix": self.table_prefix,
                "default_target_schema": self.default_target_schema,
                "enable_transactions": self.enable_transactions,
                "transaction_timeout": self.transaction_timeout,
            },
            "performance": {
                "parallel_processing": self.parallel_processing,
                "max_workers": self.max_workers,
                "memory_limit_mb": self.memory_limit_mb,
                "effective_timeout": self.effective_timeout,
            },
            "security": {
                "encryption_enabled": self.encryption_enabled,
                "audit_logging": self.audit_logging,
                "verify_ssl": self.verify_ssl,
            },
            "development": {
                "debug_mode": self.debug_mode,
                "mock_mode": self.mock_mode,
                "enable_logging": self.enable_logging,
                "test_data_size": self.test_data_size,
            },
            "plugins": {
                "enable_plugins": self.enable_plugins,
                "plugin_directory": self.plugin_directory,
                "plugin_timeout": self.plugin_timeout,
            },
        }

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextSettings pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-target-oracle-wms")

    @classmethod
    def create_for_development(cls, **overrides: object) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, object] = {
            "batch_size": 100,
            "table_prefix": "DEV_",
            "default_target_schema": "WMS_DEV",
            "timeout": 30.0,
            "max_retries": 3,
            "verify_ssl": False,
            "debug_mode": True,
            "mock_mode": False,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-wms",
            **dev_overrides,
        )

    @classmethod
    def create_for_production(cls, **overrides: object) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, object] = {
            "batch_size": 1000,
            "table_prefix": "PROD_",
            "default_target_schema": "WMS_PRODUCTION",
            "timeout": 120.0,
            "max_retries": 10,
            "verify_ssl": True,
            "debug_mode": False,
            "mock_mode": False,
            "encryption_enabled": True,
            "audit_logging": True,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-wms",
            **prod_overrides,
        )

    @classmethod
    def create_for_testing(cls, **overrides: object) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, object] = {
            "batch_size": 10,
            "table_prefix": "TEST_",
            "default_target_schema": "WMS_TEST",
            "timeout": 15.0,
            "max_retries": 1,
            "verify_ssl": False,
            "debug_mode": True,
            "mock_mode": True,
            "encryption_enabled": False,
            "audit_logging": False,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-target-oracle-wms",
            **test_overrides,
        )


def create_config_from_dict(
    config_dict: dict[str, object],
) -> FlextResult[FlextTargetOracleWmsSettings]:
    """Create configuration from dictionary with validation.

    Args:
    config_dict: Raw configuration dictionary

    Returns:
    FlextResult containing validated configuration or error

    """
    try:
        # Use model_validate for proper type conversion from dict
        config: dict[str, object] = FlextTargetOracleWmsSettings.model_validate(
            config_dict,
        )
        logger.debug("Configuration created and validated successfully")
        return FlextResult["FlextTargetOracleWmsSettings"].ok(config)

    except Exception as e:
        logger.exception("Configuration validation failed")
        return FlextResult["FlextTargetOracleWmsSettings"].fail(
            f"Invalid configuration: {e}",
        )


def create_config_with_preset(
    base_config: dict[str, object],
    preset_name: str,
) -> FlextResult[FlextTargetOracleWmsSettings]:
    """Create configuration with preset applied.

    Args:
    base_config: Base configuration dictionary
    preset_name: Name of preset to apply

    Returns:
    FlextResult containing configured instance or error

    """
    try:
        # Create base configuration
        config_result: FlextResult[object] = create_config_from_dict(base_config)
        if not config_result.success:
            return config_result

        config: dict[str, object] = config_result.data
        if config is None:
            return FlextResult["FlextTargetOracleWmsSettings"].fail(
                "Configuration creation returned None",
            )

        # Apply preset
        return config.apply_preset(preset_name)

    except Exception as e:
        return FlextResult["FlextTargetOracleWmsSettings"].fail(
            f"Failed to create config with preset: {e}",
        )


__all__ = [
    "FlextTargetOracleWmsSettings",
    "create_config_from_dict",
    "create_config_with_preset",
]
