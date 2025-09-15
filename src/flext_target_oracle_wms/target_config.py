"""Target configuration module for Oracle WMS Target.

Provides configuration models, validation logic, and environment management
for Oracle WMS target operations with flext-core integration.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_oracle_wms import FlextOracleWmsApiVersion, FlextOracleWmsClientConfig
from pydantic import Field, field_validator

logger = FlextLogger(__name__)


class TargetOracleWmsConfig(FlextModels.Config):
    """Configuration model for Oracle WMS Target with validation.

    Provides comprehensive configuration for Oracle WMS target operations
    with automatic validation and type safety.
    """

    # Oracle WMS Connection
    base_url: str = Field(
        description="Oracle WMS base URL",
        examples=["https://ta29.wms.ocs.oraclecloud.com"],
    )
    username: str = Field(
        description="Oracle WMS username",
        examples=["wms_user"],
    )
    password: str = Field(
        description="Oracle WMS password",
        repr=False,  # Hide in string representation for security
    )
    environment: str = Field(
        default="default",
        description="Environment identifier",
        examples=["development", "staging", "production"],
    )

    # Connection Settings
    timeout: float = Field(
        default=30.0,
        description="Request timeout in seconds",
        gt=0,
    )
    max_retries: int = Field(
        default=3,
        description="Maximum retry attempts",
        ge=0,
    )
    verify_ssl: bool = Field(
        default=True,
        description="Verify SSL certificates",
    )
    enable_logging: bool = Field(
        default=True,
        description="Enable request/response logging",
    )

    # Target Settings
    batch_size: int = Field(
        default=1000,
        description="Batch size for record processing",
        gt=0,
    )
    load_method: str = Field(
        default="APPEND_ONLY",
        description="Data load method",
    )
    table_prefix: str = Field(
        default="",
        description="Prefix for generated table names",
    )
    default_target_schema: str = Field(
        default="WMS_TARGET",
        description="Default schema for target tables",
    )

    # Plugin System
    enable_plugins: bool = Field(
        default=False,
        description="Enable plugin system",
    )
    plugin_directory: str = Field(
        default="./plugins",
        description="Directory for plugins",
    )

    # Testing and Development
    mock_mode: bool = Field(
        default=False,
        description="Enable mock mode for testing",
    )

    # Preset configurations
    PRESETS: ClassVar[dict[str, FlextTypes.Core.Dict]] = {
        "development": {
            "batch_size": 100,
            "table_prefix": "DEV_",
            "default_target_schema": "WMS_DEV",
            "timeout": 30.0,
            "max_retries": 3,
            "verify_ssl": False,
            "enable_logging": True,
        },
        "staging": {
            "batch_size": 500,
            "table_prefix": "STG_",
            "default_target_schema": "WMS_STAGING",
            "timeout": 60.0,
            "max_retries": 5,
            "verify_ssl": True,
            "enable_logging": True,
        },
        "production": {
            "batch_size": 1000,
            "table_prefix": "PROD_",
            "default_target_schema": "WMS_PRODUCTION",
            "timeout": 120.0,
            "max_retries": 10,
            "verify_ssl": True,
            "enable_logging": True,
        },
        "testing": {
            "batch_size": 10,
            "table_prefix": "TEST_",
            "default_target_schema": "WMS_TEST",
            "timeout": 15.0,
            "max_retries": 1,
            "verify_ssl": False,
            "enable_logging": False,
            "mock_mode": True,
        },
    }

    @field_validator("load_method")
    @classmethod
    def validate_load_method(cls, v: str) -> str:
        """Validate load method values."""
        valid_methods = {"APPEND_ONLY", "UPSERT", "REPLACE"}
        if v.upper() not in valid_methods:
            msg = f"Invalid load_method: {v}. Must be one of {valid_methods}"
            raise ValueError(msg)
        return v.upper()

    @field_validator("base_url")
    @classmethod
    def validate_base_url(cls, v: str) -> str:
        """Validate base URL format."""
        if not v.startswith(("http://", "https://")):
            msg = "base_url must start with http:// or https://"
            raise ValueError(msg)
        return v.rstrip("/")

    def to_oracle_wms_config(self) -> FlextOracleWmsClientConfig:
        """Convert to flext-oracle-wms client configuration."""
        return FlextOracleWmsClientConfig(
            oracle_wms_base_url=self.base_url,
            oracle_wms_username=self.username,
            oracle_wms_password=self.password,
            environment=self.environment,
            oracle_wms_timeout=int(self.timeout),
            oracle_wms_max_retries=self.max_retries,
            api_version=FlextOracleWmsApiVersion.LGF_V10,
            oracle_wms_verify_ssl=self.verify_ssl,
            oracle_wms_enable_logging=self.enable_logging,
        )

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate Oracle WMS configuration business rules."""
        try:
            # Validate base URL accessibility
            if not self.base_url.startswith(("http://", "https://")):
                return FlextResult[None].fail(
                    "Base URL must start with http:// or https://"
                )

            # Validate timeout values
            if self.timeout <= 0:
                return FlextResult[None].fail("Timeout must be positive")

            # Validate batch size
            if self.batch_size <= 0:
                return FlextResult[None].fail("Batch size must be positive")

            # Validate load method
            valid_methods = {"APPEND_ONLY", "UPSERT", "REPLACE"}
            if self.load_method.upper() not in valid_methods:
                return FlextResult[None].fail(
                    f"Invalid load_method: {self.load_method}"
                )

            # Validate credentials are provided
            if not self.username.strip():
                return FlextResult[None].fail("Username cannot be empty")
            if not self.password.strip():
                return FlextResult[None].fail("Password cannot be empty")

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Configuration validation failed: {e}")

    def apply_preset(self, preset_name: str) -> FlextResult[TargetOracleWmsConfig]:
        """Apply configuration preset."""
        try:
            if preset_name not in self.PRESETS:
                available = list(self.PRESETS.keys())
                return FlextResult[TargetOracleWmsConfig].fail(
                    f"Unknown preset '{preset_name}'. Available: {available}",
                )

            preset_values = self.PRESETS[preset_name]
            updated_data = self.model_dump()
            updated_data.update(preset_values)

            updated_config = self.__class__(**updated_data)
            logger.info(f"Applied configuration preset: {preset_name}")
            return FlextResult[TargetOracleWmsConfig].ok(updated_config)

        except Exception as e:
            return FlextResult[TargetOracleWmsConfig].fail(
                f"Failed to apply preset {preset_name}: {e}"
            )


def create_config_from_dict(
    config_dict: FlextTypes.Core.Dict,
) -> FlextResult[TargetOracleWmsConfig]:
    """Create configuration from dictionary with validation.

    Args:
      config_dict: Raw configuration dictionary

    Returns:
      FlextResult containing validated configuration or error

    """
    try:
        # Use model_validate for proper type conversion from dict
        config = TargetOracleWmsConfig.model_validate(config_dict)
        logger.debug("Configuration created and validated successfully")
        return FlextResult[TargetOracleWmsConfig].ok(config)

    except Exception as e:
        logger.exception("Configuration validation failed")
        return FlextResult[TargetOracleWmsConfig].fail(f"Invalid configuration: {e}")


def create_config_with_preset(
    base_config: FlextTypes.Core.Dict,
    preset_name: str,
) -> FlextResult[TargetOracleWmsConfig]:
    """Create configuration with preset applied.

    Args:
      base_config: Base configuration dictionary
      preset_name: Name of preset to apply

    Returns:
      FlextResult containing configured instance or error

    """
    try:
        # Create base configuration
        config_result = create_config_from_dict(base_config)
        if not config_result.success:
            return config_result

        config = config_result.data
        if config is None:
            return FlextResult[TargetOracleWmsConfig].fail("Configuration creation returned None")

        # Apply preset
        return config.apply_preset(preset_name)

    except Exception as e:
        return FlextResult[TargetOracleWmsConfig].fail(
            f"Failed to create config with preset: {e}"
        )


__all__ = [
    "TargetOracleWmsConfig",
    "create_config_from_dict",
    "create_config_with_preset",
]
