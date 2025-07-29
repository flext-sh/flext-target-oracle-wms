"""Oracle WMS connection configuration using flext-core patterns."""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextResult, FlextValueObject as FlextDomainBaseModel


class FlextOracleOracleWMSConnectionConfig(FlextDomainBaseModel):
    """Oracle WMS connection configuration using flext-core patterns."""

    host: str
    port: int
    service_name: str
    username: str
    password: str
    schema_name: str = "WMS_TARGET"
    max_connections: int = 10
    connection_timeout: int = 30
    encoding: str = "UTF-8"
    nencoding: str = "UTF-8"
    threaded: bool = True

    def build_connection_string(self) -> str:
        """Build Oracle connection string."""
        return f"oracle+oracledb://{self.username}:{self.password}@{self.host}:{self.port}/?service_name={self.service_name}"

    def build_dsn(self) -> str:
        """Build Oracle DSN."""
        return f"{self.host}:{self.port}/{self.service_name}"

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for cx_Oracle connection."""
        return {
            "user": self.username,
            "password": self.password,
            "dsn": self.build_dsn(),
            "encoding": self.encoding,
            "nencoding": self.nencoding,
            "threaded": self.threaded,
        }

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate connection configuration domain rules."""
        try:
            if not self.host or not self.host.strip():
                return FlextResult.fail("Host is required")
            if not self.service_name or not self.service_name.strip():
                return FlextResult.fail("Service name is required")
            if not (1 <= self.port <= 65535):
                return FlextResult.fail("Port must be between 1 and 65535")
            if not self.username or not self.username.strip():
                return FlextResult.fail("Username is required")
            if not self.password:
                return FlextResult.fail("Password is required")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Connection configuration validation failed: {e}")


# Alias for backward compatibility
OracleWMSConnectionConfig = FlextOracleOracleWMSConnectionConfig
