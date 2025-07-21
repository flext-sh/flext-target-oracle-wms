"""Configuration for FLEXT target-oracle-wms using flext-core patterns with structured value objects.

This module provides comprehensive configuration management for Oracle WMS target integration.
"""

from typing import Any

from flext_core.domain.types import ServiceResult
from flext_core.infrastructure.config import BaseConfig
from pydantic import Field

from flext_target_oracle_wms.domain.value_objects import (
    OracleWMSConnectionConfig,
    OracleWMSTargetConfig,
)


class TargetOracleWMSConfig(BaseConfig):
    """Complete configuration for target-oracle-wms using flext-core patterns.

    Uses flext-core patterns with structured value objects. Zero tolerance for
    legacy patterns or code duplication.
    """

    # Connection configuration
    connection: OracleWMSConnectionConfig = Field(
        default_factory=OracleWMSConnectionConfig,
        description="Oracle WMS connection configuration",
    )

    # Target configuration
    target: OracleWMSTargetConfig = Field(
        default_factory=OracleWMSTargetConfig,
        description="Oracle WMS target configuration",
    )

    def validate_config(self) -> ServiceResult[None]:
        """Validate the complete configuration.

        Returns:
            ServiceResult[None]: Success if valid, error details if invalid

        """
        try:
            # Validate connection
            connection_result = self.connection.validate()
            if not connection_result.success:
                return ServiceResult.failure(
                    f"Connection validation failed: {connection_result.error}",
                )

            # Validate target
            target_result = self.target.validate()
            if not target_result.success:
                return ServiceResult.failure(
                    f"Target validation failed: {target_result.error}",
                )

            return ServiceResult.success(None)
        except Exception as e:
            return ServiceResult.failure(f"Configuration validation failed: {e}")

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary.

        Returns:
            dict[str, Any]: Configuration as dictionary

        """
        return {
            "connection": self.connection.to_dict(),
            "target": self.target.to_dict(),
        }
