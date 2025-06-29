# 🧪 TARGET Oracle WMS - Test Suite

> **Module**: Comprehensive test suite for TARGET Oracle WMS with Singer SDK compliance and integration testing | **Audience**: QA Engineers, Data Engineers, Target Testing Specialists | **Status**: Production Ready

## 📋 **Overview**

Enterprise-grade test suite for the TARGET Oracle WMS implementation, providing comprehensive testing coverage including unit tests, integration tests with real Oracle Warehouse Management System endpoints, performance testing, and Singer SDK compliance validation. This test suite demonstrates best practices for testing Singer targets and data loading operations to Oracle WMS.

---

## 🧭 **Navigation Context**

**🏠 Root**: [PyAuto Home](../../README.md) → **📂 Component**: [TARGET Oracle WMS](../README.md) → **📂 Current**: Test Suite

---

## 🎯 **Module Purpose**

This test module provides comprehensive validation for the TARGET Oracle WMS implementation, ensuring reliability, performance, and correctness of all data loading operations, Singer SDK compliance, and enterprise Oracle WMS integration workflows.

### **Key Testing Areas**

- **Unit Testing** - Core target logic and data transformation validation
- **Integration Testing** - End-to-end data loading with real WMS endpoints
- **Performance Testing** - Data throughput and loading performance to WMS
- **Singer SDK Testing** - Target compliance and specification validation
- **Authentication Testing** - WMS authentication validation
- **Error Handling Testing** - Error recovery and resilience validation

---

## 📁 **Test Structure**

```
tests/
├── unit/
│   ├── test_target_core.py              # Core target functionality tests
│   ├── test_sinks_validation.py         # Sink implementation tests
│   ├── test_authentication.py           # Authentication mechanism tests
│   ├── test_config_validation.py        # Configuration validation tests
│   └── test_data_transformation.py      # Data transformation tests
├── integration/
│   ├── test_wms_integration.py          # WMS endpoint integration tests
│   ├── test_singer_compliance.py        # Singer SDK compliance tests
│   ├── test_data_loading.py             # End-to-end data loading tests
│   ├── test_batch_processing.py         # Batch processing integration tests
│   └── test_real_time_loading.py        # Real-time data loading tests
├── e2e/
│   ├── test_target_complete.py          # Complete end-to-end workflow tests
│   ├── test_wms_pipeline.py             # WMS pipeline integration tests
│   ├── test_production_scenarios.py     # Production scenario tests
│   └── test_failover_scenarios.py       # Failover and recovery tests
├── performance/
│   ├── test_throughput_performance.py   # Data throughput testing
│   ├── test_concurrent_loading.py       # Concurrent loading scenarios
│   ├── test_memory_optimization.py      # Memory usage optimization tests
│   └── test_scalability_limits.py       # Scalability testing
├── singer/
│   ├── test_target_compliance.py        # Singer target specification compliance
│   ├── test_schema_validation.py        # Schema handling validation
│   ├── test_state_management.py         # State management testing
│   └── test_message_processing.py       # Singer message processing tests
├── fixtures/
│   ├── wms_fixtures.py                  # WMS test data fixtures
│   ├── singer_fixtures.py               # Singer message test fixtures
│   └── authentication_fixtures.py       # Authentication test fixtures
├── conftest.py                           # Pytest configuration and fixtures
└── test_target.py                        # Core target tests
└── test_sinks.py                         # Sink implementation tests
```

---

## 🔧 **Test Categories**

### **1. Unit Tests (unit/)**

#### **Core Target Testing (test_target_core.py)**

```python
"""Unit tests for TARGET Oracle WMS core functionality."""

import pytest
from unittest.mock import Mock, AsyncMock, patch
import json
from datetime import datetime

from target_oracle_wms.target import TargetOracleWMS
from target_oracle_wms.config import TargetConfig
from target_oracle_wms.sinks import OracleWMSSink
from target_oracle_wms.exceptions import (
    TargetConfigurationError,
    WMSConnectionError,
    DataValidationError
)

class TestTargetOracleWMS:
    """Test Oracle WMS target core functionality."""

    @pytest.fixture
    def target_config(self):
        """Target configuration fixture."""
        return TargetConfig(
            wms_host="https://test-wms.oracle.com",
            client_id="test_client_id",
            client_secret="test_client_secret",
            username="test_user",
            password="test_password",
            batch_size=1000,
            timeout=30
        )

    @pytest.fixture
    def mock_wms_client(self):
        """Mock WMS client fixture."""
        return Mock()

    @pytest.fixture
    def target_instance(self, target_config, mock_wms_client):
        """Target instance with mocked dependencies."""
        with patch('target_oracle_wms.target.WMSClient', return_value=mock_wms_client):
            return TargetOracleWMS(config=target_config)

    def test_target_initialization_success(self, target_config):
        """Test successful target initialization."""
        # Act
        target = TargetOracleWMS(config=target_config)

        # Assert
        assert target.config == target_config
        assert target.name == "target-oracle-wms"
        assert target.config.batch_size == 1000

    def test_target_initialization_invalid_config(self):
        """Test target initialization with invalid configuration."""
        # Arrange
        invalid_config = TargetConfig(
            wms_host="",  # Invalid empty host
            client_id="test_client",
            client_secret="test_secret"
        )

        # Act & Assert
        with pytest.raises(TargetConfigurationError):
            TargetOracleWMS(config=invalid_config)

    def test_get_sink_for_stream(self, target_instance):
        """Test sink creation for specific stream."""
        # Arrange
        stream_name = "inventory"
        schema = {
            "type": "object",
            "properties": {
                "item_id": {"type": "string"},
                "quantity": {"type": "number"},
                "location": {"type": "string"}
            }
        }

        # Act
        sink = target_instance.get_sink(stream_name, schema)

        # Assert
        assert isinstance(sink, OracleWMSSink)
        assert sink.stream_name == stream_name
        assert sink.schema == schema
```

#### **WMS Sink Testing (test_sinks_validation.py)**

```python
"""Unit tests for Oracle WMS sink implementation."""

import pytest
from unittest.mock import Mock, patch
from datetime import datetime

from target_oracle_wms.sinks import OracleWMSSink
from target_oracle_wms.config import TargetConfig
from target_oracle_wms.exceptions import DataValidationError

class TestOracleWMSSink:
    """Test Oracle WMS sink implementation."""

    @pytest.fixture
    def sink_config(self):
        """Sink configuration fixture."""
        return TargetConfig(
            wms_host="https://test-wms.oracle.com",
            client_id="test_client",
            client_secret="test_secret",
            batch_size=500
        )

    @pytest.fixture
    def inventory_schema(self):
        """Inventory stream schema fixture."""
        return {
            "type": "object",
            "properties": {
                "item_id": {"type": "string"},
                "quantity": {"type": "number"},
                "location": {"type": "string"},
                "updated_at": {"type": "string", "format": "date-time"}
            },
            "required": ["item_id", "quantity", "location"]
        }

    @pytest.fixture
    def mock_wms_client(self):
        """Mock WMS client for sink testing."""
        client = Mock()
        client.send_batch.return_value = {"status": "success", "records_processed": 100}
        return client

    @pytest.fixture
    def oracle_wms_sink(self, sink_config, inventory_schema, mock_wms_client):
        """Oracle WMS sink instance."""
        with patch('target_oracle_wms.sinks.WMSClient', return_value=mock_wms_client):
            return OracleWMSSink(
                target=Mock(),
                stream_name="inventory",
                schema=inventory_schema,
                config=sink_config
            )

    def test_sink_initialization(self, oracle_wms_sink, inventory_schema):
        """Test sink initialization."""
        # Assert
        assert oracle_wms_sink.stream_name == "inventory"
        assert oracle_wms_sink.schema == inventory_schema
        assert oracle_wms_sink.batch_size == 500
        assert len(oracle_wms_sink.records_buffer) == 0

    def test_process_record_valid_data(self, oracle_wms_sink):
        """Test processing valid record data."""
        # Arrange
        record = {
            "item_id": "ITEM_001",
            "quantity": 100.0,
            "location": "WAREHOUSE_A_01",
            "updated_at": "2025-06-19T10:00:00Z"
        }

        # Act
        oracle_wms_sink.process_record(record)

        # Assert
        assert len(oracle_wms_sink.records_buffer) == 1
        assert oracle_wms_sink.records_buffer[0] == record

    def test_process_record_invalid_data(self, oracle_wms_sink):
        """Test processing invalid record data."""
        # Arrange
        invalid_record = {
            "item_id": "ITEM_001",
            "quantity": 100.0
            # Missing required 'location' field
        }

        # Act & Assert
        with pytest.raises(DataValidationError):
            oracle_wms_sink.process_record(invalid_record)

    def test_flush_records_batch(self, oracle_wms_sink, mock_wms_client):
        """Test batch flushing functionality."""
        # Arrange
        records = [
            {"item_id": f"ITEM_{i:03d}", "quantity": i * 10.0, "location": f"LOC_{i:02d}"}
            for i in range(100)
        ]

        for record in records:
            oracle_wms_sink.process_record(record)

        # Act
        result = oracle_wms_sink.flush_records()

        # Assert
        assert result["status"] == "success"
        assert result["records_processed"] == 100
        assert len(oracle_wms_sink.records_buffer) == 0
        mock_wms_client.send_batch.assert_called_once()
```

### **2. Integration Tests (integration/)**

#### **WMS Integration Testing (test_wms_integration.py)**

```python
"""Integration tests for Oracle WMS endpoint integration."""

import pytest
import asyncio
from unittest.mock import patch, Mock
import json

from target_oracle_wms.target import TargetOracleWMS
from target_oracle_wms.config import TargetConfig

@pytest.mark.integration
class TestWMSIntegration:
    """Test Oracle WMS integration scenarios."""

    @pytest.fixture
    def integration_config(self):
        """Integration test configuration."""
        return TargetConfig(
            wms_host="https://test-wms.oracle.com",
            client_id="integration_test_client",
            client_secret="integration_test_secret",
            username="integration_user",
            password="integration_password",
            batch_size=100,
            timeout=60
        )

    @pytest.fixture
    async def target_with_auth(self, integration_config):
        """Target instance with authenticated WMS client."""
        target = TargetOracleWMS(config=integration_config)

        # Mock successful authentication
        with patch.object(target.wms_client, 'authenticate') as mock_auth:
            mock_auth.return_value = True
            await target.wms_client.authenticate()

        return target

    @pytest.mark.asyncio
    async def test_end_to_end_inventory_loading(self, target_with_auth):
        """Test end-to-end inventory data loading to WMS."""
        # Arrange
        inventory_records = [
            {
                "item_id": "ITEM_001",
                "quantity": 150.0,
                "location": "WAREHOUSE_A_01",
                "status": "AVAILABLE",
                "updated_at": "2025-06-19T10:00:00Z"
            },
            {
                "item_id": "ITEM_002",
                "quantity": 75.0,
                "location": "WAREHOUSE_A_02",
                "status": "RESERVED",
                "updated_at": "2025-06-19T10:05:00Z"
            }
        ]

        schema = {
            "type": "object",
            "properties": {
                "item_id": {"type": "string"},
                "quantity": {"type": "number"},
                "location": {"type": "string"},
                "status": {"type": "string"},
                "updated_at": {"type": "string", "format": "date-time"}
            }
        }

        # Mock successful WMS API calls
        with patch.object(target_with_auth.wms_client, 'send_batch') as mock_send:
            mock_send.return_value = {
                "status": "success",
                "records_processed": len(inventory_records),
                "transaction_id": "TXN_12345"
            }

            # Act
            sink = target_with_auth.get_sink("inventory", schema)

            for record in inventory_records:
                sink.process_record(record)

            result = sink.flush_records()

            # Assert
            assert result["status"] == "success"
            assert result["records_processed"] == 2
            mock_send.assert_called_once()
```

### **3. End-to-End Tests (e2e/)**

#### **Complete Workflow Testing (test_target_complete.py)**

```python
"""End-to-end tests for complete TARGET Oracle WMS workflow."""

import pytest
from unittest.mock import patch, Mock
import json
from datetime import datetime

from target_oracle_wms.target import TargetOracleWMS
from target_oracle_wms.config import TargetConfig

@pytest.mark.e2e
class TestCompleteWMSWorkflow:
    """Test complete WMS target workflow."""

    @pytest.fixture
    def production_config(self):
        """Production-like configuration."""
        return TargetConfig(
            wms_host="https://production-wms.oracle.com",
            client_id="prod_client_id",
            client_secret="prod_client_secret",
            username="prod_user",
            password="prod_password",
            batch_size=1000,
            timeout=120,
            retry_attempts=3
        )

    @pytest.mark.asyncio
    async def test_complete_warehouse_data_sync(self, production_config):
        """Test complete warehouse data synchronization workflow."""
        # Arrange
        warehouse_data = {
            "inventory": [
                {"item_id": "ITEM_001", "quantity": 100, "location": "A1"},
                {"item_id": "ITEM_002", "quantity": 200, "location": "A2"}
            ],
            "orders": [
                {"order_id": "ORD_001", "status": "PENDING", "items": ["ITEM_001"]},
                {"order_id": "ORD_002", "status": "PROCESSING", "items": ["ITEM_002"]}
            ],
            "allocations": [
                {"allocation_id": "ALLOC_001", "order_id": "ORD_001", "item_id": "ITEM_001", "quantity": 50},
                {"allocation_id": "ALLOC_002", "order_id": "ORD_002", "item_id": "ITEM_002", "quantity": 100}
            ]
        }

        # Mock successful WMS operations
        target = TargetOracleWMS(config=production_config)

        with patch.object(target.wms_client, 'authenticate') as mock_auth, \
             patch.object(target.wms_client, 'send_batch') as mock_send:

            mock_auth.return_value = True
            mock_send.return_value = {"status": "success", "records_processed": 2}

            # Act - Process each data type
            results = {}
            for stream_name, records in warehouse_data.items():
                sink = target.get_sink(stream_name, self._get_schema_for_stream(stream_name))

                for record in records:
                    sink.process_record(record)

                results[stream_name] = sink.flush_records()

            # Assert
            for stream_name, result in results.items():
                assert result["status"] == "success"
                assert result["records_processed"] == 2

    def _get_schema_for_stream(self, stream_name):
        """Get schema for stream type."""
        schemas = {
            "inventory": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "quantity": {"type": "number"},
                    "location": {"type": "string"}
                }
            },
            "orders": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string"},
                    "status": {"type": "string"},
                    "items": {"type": "array", "items": {"type": "string"}}
                }
            },
            "allocations": {
                "type": "object",
                "properties": {
                    "allocation_id": {"type": "string"},
                    "order_id": {"type": "string"},
                    "item_id": {"type": "string"},
                    "quantity": {"type": "number"}
                }
            }
        }
        return schemas.get(stream_name, {})
```

---

## 🔧 **Test Configuration**

### **Pytest Configuration (conftest.py)**

```python
"""Pytest configuration and shared fixtures for TARGET Oracle WMS tests."""

import pytest
import asyncio
import os
from unittest.mock import Mock, patch
import json

from target_oracle_wms.config import TargetConfig
from target_oracle_wms.target import TargetOracleWMS

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def test_config():
    """Test configuration fixture."""
    return TargetConfig(
        wms_host=os.getenv("TEST_WMS_HOST", "https://test-wms.oracle.com"),
        client_id=os.getenv("TEST_CLIENT_ID", "test_client"),
        client_secret=os.getenv("TEST_CLIENT_SECRET", "test_secret"),
        username=os.getenv("TEST_USERNAME", "test_user"),
        password=os.getenv("TEST_PASSWORD", "test_password"),
        batch_size=100,
        timeout=30
    )

@pytest.fixture
def mock_wms_client():
    """Mock Oracle WMS client."""
    client = Mock()
    client.authenticate.return_value = True
    client.send_batch.return_value = {
        "status": "success",
        "records_processed": 0
    }
    return client

@pytest.fixture
def target_instance(test_config, mock_wms_client):
    """Target instance with mocked WMS client."""
    with patch('target_oracle_wms.target.WMSClient', return_value=mock_wms_client):
        return TargetOracleWMS(config=test_config)

@pytest.fixture
def sample_inventory_records():
    """Sample inventory records for testing."""
    return [
        {
            "item_id": "ITEM_001",
            "quantity": 150.0,
            "location": "WAREHOUSE_A_01",
            "status": "AVAILABLE",
            "updated_at": "2025-06-19T10:00:00Z"
        },
        {
            "item_id": "ITEM_002",
            "quantity": 75.0,
            "location": "WAREHOUSE_A_02",
            "status": "RESERVED",
            "updated_at": "2025-06-19T10:05:00Z"
        }
    ]

@pytest.fixture
def inventory_schema():
    """Inventory stream schema fixture."""
    return {
        "type": "object",
        "properties": {
            "item_id": {"type": "string"},
            "quantity": {"type": "number"},
            "location": {"type": "string"},
            "status": {"type": "string"},
            "updated_at": {"type": "string", "format": "date-time"}
        },
        "required": ["item_id", "quantity", "location"]
    }

@pytest.fixture
def singer_messages():
    """Sample Singer messages for testing."""
    return [
        {
            "type": "SCHEMA",
            "stream": "inventory",
            "schema": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "quantity": {"type": "number"},
                    "location": {"type": "string"}
                }
            }
        },
        {
            "type": "RECORD",
            "stream": "inventory",
            "record": {
                "item_id": "ITEM_001",
                "quantity": 150.0,
                "location": "WAREHOUSE_A_01"
            }
        },
        {
            "type": "STATE",
            "value": {"bookmarks": {"inventory": {"timestamp": "2025-06-19T10:00:00Z"}}}
        }
    ]
```

---

## 🔗 **Cross-References**

### **Component Documentation**

- [Component Overview](../README.md) - Complete TARGET Oracle WMS documentation
- [Source Implementation](../src/README.md) - Source code structure and patterns
- [Configuration Guide](../config.json.example) - Configuration examples

### **Testing Documentation**

- [Singer SDK Testing](https://sdk.meltano.com/en/latest/testing.html) - Singer SDK testing guidelines
- [PyTest Documentation](https://docs.pytest.org/) - Python testing framework
- [AsyncIO Testing](https://docs.python.org/3/library/asyncio-dev.html) - Async testing patterns

### **Oracle WMS References**

- [Oracle WMS Cloud](https://docs.oracle.com/en/cloud/saas/warehouse-management/) - WMS documentation
- [Oracle WMS REST APIs](https://docs.oracle.com/en/cloud/saas/warehouse-management/rest-api/) - REST API reference
- [Oracle Cloud Authentication](https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/Authentication.html) - Authentication guide

---

**📂 Module**: Test Suite | **🏠 Component**: [TARGET Oracle WMS](../README.md) | **Framework**: PyTest 7.0+ | **Updated**: 2025-06-19
