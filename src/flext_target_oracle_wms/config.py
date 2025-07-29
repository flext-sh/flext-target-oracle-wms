"""Configuration for FLEXT target-oracle-wms using flext-core patterns.

This module provides configuration management for Oracle WMS target integration.
"""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import (
    FlextResult,
    FlextValueObject,
)

# Import flext-core patterns for configuration
from pydantic import Field, field_validator


class TargetOracleWMSConfig(FlextValueObject):
    """Configuration for Oracle WMS target."""

    # Oracle Database connection settings
    host: str = Field(..., description="Oracle database host")
    port: int = Field(1521, description="Oracle database port")
    service_name: str = Field(..., description="Oracle service name")
    username: str = Field(..., description="Database username")
    password: str = Field(..., description="Database password")

    # WMS-specific settings
    batch_size: int = Field(1000, description="Batch size for bulk operations")
    max_connections: int = Field(10, description="Maximum database connections")
    connection_timeout: int = Field(30, description="Connection timeout in seconds")

    # Target behavior settings
    create_tables: bool = Field(True, description="Create tables if they don't exist")
    truncate_before_load: bool = Field(
        False,
        description="Truncate tables before loading",
    )

    @field_validator("host")
    @classmethod
    def validate_host_field(cls, v: str) -> str:
        """Validate Oracle host."""
        if not isinstance(v, str) or not v.strip():
            msg = "Host must be a non-empty string"
            raise ValueError(msg)
        return v.strip()

    @field_validator("service_name")
    @classmethod
    def validate_service_name_field(cls, v: str) -> str:
        """Validate Oracle service name."""
        if not isinstance(v, str) or not v.strip():
            msg = "Service name must be a non-empty string"
            raise ValueError(msg)
        return v.strip()

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate domain-specific business rules."""
        try:
            # Validate host is reachable (basic format check)
            if not self.host or not self.host.strip():
                return FlextResult.fail("Host is required")

            # Validate service name
            if not self.service_name or not self.service_name.strip():
                return FlextResult.fail("Service name is required")

            # Validate port range
            if not (1 <= self.port <= 65535):
                return FlextResult.fail("Port must be between 1 and 65535")

            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Configuration validation failed: {e}")

    class Config:
        """Pydantic configuration."""

        env_prefix = "TARGET_ORACLE_WMS_"
        case_sensitive = False


class WMSConnectionSettings(FlextValueObject):
    """WMS connection settings value object."""

    host: str = Field(..., description="Oracle database host")
    port: int = Field(1521, description="Oracle database port")
    service_name: str = Field(..., description="Oracle service name")
    username: str = Field(..., description="Database username")
    password: str = Field(..., description="Database password")


class WMSOperationSettings(FlextValueObject):
    """WMS operation settings value object."""

    batch_size: int = Field(1000, description="Batch size for operations")
    max_connections: int = Field(10, description="Maximum connections")
    connection_timeout: int = Field(30, description="Connection timeout")
    create_tables: bool = Field(True, description="Create tables if needed")
    truncate_before_load: bool = Field(False, description="Truncate before load")


def create_wms_config(**kwargs: Any) -> TargetOracleWMSConfig:
    """Create WMS configuration with validation."""
    return TargetOracleWMSConfig(**kwargs)


def validate_wms_config(config: dict[str, Any]) -> FlextResult[TargetOracleWMSConfig]:
    """Validate WMS configuration."""
    try:
        validated_config = create_wms_config(**config)
        return FlextResult.ok(validated_config)
    except (RuntimeError, ValueError, TypeError) as e:
        return FlextResult.fail(f"Configuration validation failed: {e}")
