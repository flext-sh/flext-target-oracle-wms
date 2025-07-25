"""Oracle WMS connection configuration using flext-core patterns."""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextValueObject as FlextDomainBaseModel


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
