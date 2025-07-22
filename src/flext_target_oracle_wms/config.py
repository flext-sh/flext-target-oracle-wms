"""Configuration for FLEXT target-oracle-wms using flext-core patterns with structured value objects.

This module provides comprehensive configuration management for Oracle WMS target integration.
"""

from typing import Any

from flext_core.config.base import BaseConfig
from flext_core.domain.shared_types import ServiceResult
from pydantic import Field

# TODO: Create domain.value_objects module when implementing full WMS functionality
# from flext_target_oracle_wms.domain.value_objects import (
#     OracleWMSConnectionConfig,
#     OracleWMSTargetConfig,
# )


class TargetOracleWMSConfig(BaseConfig):
    """Complete configuration for target-oracle-wms using flext-core patterns.

    Uses flext-core patterns with structured value objects. Zero tolerance for
    legacy patterns or code duplication.
    """

    # Connection configuration
    host: str = Field(..., description="Oracle WMS server hostname")
    port: int = Field(1521, description="Oracle WMS server port")
    service_name: str = Field(..., description="Oracle WMS service name")
    user: str = Field(..., description="Oracle WMS username")
    password: str = Field(..., description="Oracle WMS password")

    # Target configuration
    schema_name: str = Field(
        "WMS",
        description="Oracle WMS schema name",
        alias="schema",
    )
    batch_size: int = Field(1000, ge=1, description="Batch size for WMS operations")

    def validate_config(self) -> ServiceResult[Any]:
        """Validate the complete configuration.

        Returns:
            ServiceResult[None]: Success if valid, error details if invalid

        """
        try:
            # Basic validation
            if not self.host:
                return ServiceResult.fail("Host is required")
            if not self.service_name:
                return ServiceResult.fail("Service name is required")
            if not self.user:
                return ServiceResult.fail("User is required")
            if not self.password:
                return ServiceResult.fail("Password is required")

            return ServiceResult.ok(None)
        except Exception as e:
            return ServiceResult.fail(f"Configuration validation failed: {e}",
            )

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary.

        Returns:
            dict[str, Any]: Configuration as dictionary

        """
        return {
            "host": self.host,
            "port": self.port,
            "service_name": self.service_name,
            "user": self.user,
            "password": self.password,
            "schema": self.schema,
            "batch_size": self.batch_size,
        }
