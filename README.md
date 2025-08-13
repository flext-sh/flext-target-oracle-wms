# FLEXT Target Oracle WMS - Enterprise Warehouse Management System Loading

**Type**: Singer Target | **Status**: Active Development | **Dependencies**: Python 3.13+, flext-core, flext-oracle-wms, flext-meltano, singer-sdk

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Singer SDK](https://img.shields.io/badge/singer--sdk-compliant-brightgreen.svg)](https://sdk.meltano.com/)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20Architecture%20%2B%20DDD-green.svg)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
[![Coverage](https://img.shields.io/badge/coverage-90%25+-brightgreen.svg)](https://pytest.org)

Singer-compliant target for loading data into Oracle Warehouse Management Systems (WMS). Built with Python 3.13+, Clean Architecture, and Domain-Driven Design patterns as part of the FLEXT enterprise data integration platform.

## Overview

FLEXT Target Oracle WMS provides enterprise-grade data loading capabilities for Oracle Warehouse Management Systems, implementing the Singer specification for standardized data integration workflows. The target supports comprehensive WMS entity management with advanced error recovery and performance optimization.

### Key Features

- **Oracle WMS Cloud Integration**: Complete WMS data loading including inventory, orders, shipments
- **WMS Entity Support**: 15+ WMS entities with intelligent data transformation
- **Factory Pattern Architecture**: Configurable target instances with flext-oracle-wms integration
- **Enterprise Authentication**: Both Basic Auth and OAuth2 authentication methods
- **Singer Protocol Compliance**: Full Singer SDK implementation with stream processing
- **Clean Architecture**: Domain-driven design with flext-core integration
- **Zero Tolerance Quality**: 90% test coverage with comprehensive quality gates

## Quick Start

### Installation

```bash
# Install via Poetry (recommended)
poetry add flext-target-oracle-wms

# Or via pip
pip install flext-target-oracle-wms
```

### Basic Usage

```bash
# Load data from Singer stream
cat data.jsonl | target-oracle-wms --config config.json

# Generate configuration sample
target-oracle-wms --config-sample > config.json

# Show target information
target-oracle-wms --about
```

### Configuration Example

```json
{
  "base_url": "https://your-wms.oraclecloud.com",
  "auth_method": "oauth2",
  "oauth_client_id": "wms_client_id",
  "oauth_client_secret": "wms_client_secret",
  "oauth_token_url": "https://auth.oraclecloud.com/oauth2/v1/token",
  "company_code": "ACME",
  "facility_code": "DC01",
  "batch_size": 500,
  "validate_records": true,
  "validate_item_codes": true,
  "validate_location_codes": true
}
```

## Architecture

### Clean Architecture with flext-core Integration

```
src/flext_target_oracle_wms/
--- singer/                      # Singer protocol implementation
   - target.py               # Main Singer protocol implementation
   - catalog.py              # Catalog management
   - stream.py               # Stream processing
--- patterns/                    # WMS-specific patterns
   - wms_patterns.py         # Data transformation patterns
   - factory.py                   # Factory for creating target instances
   - cli.py                       # Command-line interface
   - exceptions.py                # Custom exceptions
```

### Core Components

- **Singer Target Implementation**: Main Singer protocol implementation with stream routing
- **Factory Pattern**: FlextTargetFactory for creating configured target instances
- **WMS Patterns**: Domain-specific WMS data transformation patterns
- **CLI Interface**: Command-line interface for the target
- **FlextResult Integration**: Railway-oriented programming for error handling

### Key Design Patterns

- **DRY Implementation**: Uses the real `flext-oracle-wms` library to avoid code duplication
- **Factory Pattern**: `FlextTargetFactory` for creating configured target instances
- **Result Pattern**: `FlextResult` for railway-oriented programming and error handling
- **Clean Architecture**: Clear separation between Singer protocol, domain logic, and Oracle WMS integration

## Development Commands

### Quality Gates (Zero Tolerance)

```bash
# Complete validation pipeline (run before commits)
make validate                # lint + type + security + test (90% coverage)

# Essential checks
make check                   # lint + type + test
make lint                    # Ruff linting (ALL rules enabled)
make type-check              # MyPy strict mode
make security                # Bandit + pip-audit security scanning
make format                  # Auto-format code with Ruff
make fix                     # Auto-fix code issues and format
```

### Testing

```bash
# Complete test suite
make test                    # All tests with 90% coverage requirement
make test-unit               # Unit tests only
make test-integration        # Integration tests only
make test-singer             # Singer protocol tests
make coverage-html           # Generate HTML coverage report

# Test categories
pytest -m unit               # Unit tests
pytest -m oracle             # Oracle WMS specific tests
pytest -m slow               # Slow tests
pytest -m singer             # Singer protocol tests
```

### Singer Target Operations

```bash
# Target functionality
make target-test             # Test basic target functionality
make target-validate         # Validate target configuration
make target-schema           # Validate Oracle WMS schema mappings
make target-run              # Run target with sample data
make target-dry-run          # Dry run mode for testing
```

### Oracle WMS Operations

```bash
# WMS connectivity
make wms-write-test          # Test WMS write operations
make wms-entity-check        # Validate WMS entity mappings
make wms-sync-test           # Test WMS synchronization
make wms-connect             # Test WMS connection
make wms-schema              # Generate WMS schema mappings
make wms-tables              # List WMS tables and mappings

# Data loading operations
make load-sample             # Load sample WMS data
make load-inventory          # Load inventory data
make load-shipments          # Load shipment data
make load-receipts           # Load receipt data
make load-labor              # Load labor data
```

## Configuration

### Connection Settings

| Setting         | Required | Default | Description                                 |
| --------------- | -------- | ------- | ------------------------------------------- |
| `base_url`      | Yes      | -       | Oracle WMS server hostname                  |
| `auth_method`   | Yes      | -       | Authentication method ("basic" or "oauth2") |
| `company_code`  | Yes      | -       | WMS company code                            |
| `facility_code` | Yes      | -       | WMS facility code                           |

### Authentication Settings

#### Basic Authentication

| Setting    | Required | Description  |
| ---------- | -------- | ------------ |
| `username` | Yes      | WMS username |
| `password` | Yes      | WMS password |

#### OAuth2 Authentication

| Setting               | Required | Description           |
| --------------------- | -------- | --------------------- |
| `oauth_client_id`     | Yes      | OAuth2 client ID      |
| `oauth_client_secret` | Yes      | OAuth2 client secret  |
| `oauth_token_url`     | Yes      | OAuth2 token endpoint |

### Processing Settings

| Setting               | Required | Default | Description                         |
| --------------------- | -------- | ------- | ----------------------------------- |
| `batch_size`          | No       | 500     | Records per batch                   |
| `parallel_degree`     | No       | 4       | Oracle parallel processing degree   |
| `enable_bulk_binding` | No       | true    | Enable bulk binding for performance |
| `connection_timeout`  | No       | 60      | Connection timeout in seconds       |

### Validation Settings

| Setting                   | Required | Default | Description                   |
| ------------------------- | -------- | ------- | ----------------------------- |
| `validate_records`        | No       | true    | Enable record validation      |
| `validate_item_codes`     | No       | true    | Validate item codes           |
| `validate_location_codes` | No       | true    | Validate location codes       |
| `enable_wms_hints`        | No       | true    | Use WMS-specific Oracle hints |

### Advanced Configuration

```json
{
  "base_url": "https://prod-wms.oraclecloud.com",
  "auth_method": "oauth2",
  "oauth_client_id": "prod_client_id",
  "oauth_client_secret": "prod_client_secret",
  "oauth_token_url": "https://auth.oraclecloud.com/oauth2/v1/token",
  "company_code": "PROD_COMPANY",
  "facility_code": "MAIN_DC",
  "batch_size": 1000,
  "parallel_degree": 8,
  "enable_bulk_binding": true,
  "validate_records": true,
  "validate_item_codes": true,
  "validate_location_codes": true,
  "enable_wms_hints": true,
  "connection_timeout": 120,
  "request_timeout": 300,
  "max_retries": 5,
  "retry_delay": 2,
  "enable_performance_logging": true
}
```

## Supported WMS Entities

### Core Inventory Entities

| Entity                   | Description                              | Load Method  |
| ------------------------ | ---------------------------------------- | ------------ |
| `inventory`              | Current inventory levels and adjustments | BATCH_INSERT |
| `inventory_transactions` | Inventory transaction records            | STREAMING    |
| `item_location`          | Item-location relationships              | UPSERT       |
| `location_inventory`     | Location-based inventory tracking        | REAL_TIME    |

### Order Management Entities

| Entity       | Description                       | Load Method  |
| ------------ | --------------------------------- | ------------ |
| `orders`     | Outbound orders and order lines   | BATCH_UPSERT |
| `shipments`  | Shipment information and tracking | STREAMING    |
| `receipts`   | Inbound receipts and receiving    | BATCH_INSERT |
| `cross_dock` | Cross-docking operations          | REAL_TIME    |

### Warehouse Operations Entities

| Entity           | Description                      | Load Method  |
| ---------------- | -------------------------------- | ------------ |
| `picks`          | Pick tasks and execution details | STREAMING    |
| `putaways`       | Putaway tasks and execution      | STREAMING    |
| `replenishments` | Replenishment tasks and moves    | BATCH_INSERT |
| `cycle_counts`   | Cycle count tasks and results    | BATCH_UPSERT |

### Labor and Task Management

| Entity            | Description                         | Load Method  |
| ----------------- | ----------------------------------- | ------------ |
| `labor_tasks`     | Labor tracking and task management  | STREAMING    |
| `wave_planning`   | Wave planning and optimization      | BATCH_INSERT |
| `yard_management` | Yard operations and dock scheduling | REAL_TIME    |

## Stream Processing

### WMS Data Transformation

The target applies WMS-specific transformations:

```python
# Example WMS data transformation
{
  "item_id": "ITEM001",
  "location_id": "A-01-01-01",
  "quantity": 100,
  "unit_of_measure": "EA",
  "lot_number": "LOT2025001",
  "expiration_date": "2025-12-31",
  "inventory_status": "AVAILABLE"
}
```

### Data Validation

The target validates:

- Item codes against WMS item master
- Location codes against WMS location master
- Quantity constraints and business rules
- Date formats and logical consistency
- WMS-specific business constraints

### Performance Optimization

- **Oracle Bulk Binding**: Efficient bulk insert operations
- **WMS-Specific Hints**: Oracle hints optimized for WMS tables
- **Parallel Processing**: Configurable parallel degree for large datasets
- **Connection Pooling**: Reusable database connections

## Error Handling

### Comprehensive Error Recovery

- **Connection Failures**: Automatic reconnection with exponential backoff
- **Authentication Errors**: Token refresh and re-authentication
- **WMS Constraint Violations**: Detailed validation errors with suggestions
- **Oracle Errors**: WMS-specific Oracle error handling
- **Network Issues**: Intelligent retry logic with circuit breaker patterns

### Error Categories

| Error Type               | Handling Strategy                            |
| ------------------------ | -------------------------------------------- |
| Connection Timeout       | Retry with exponential backoff               |
| Authentication Failure   | Token refresh and retry                      |
| WMS Constraint Violation | Detailed error reporting and data validation |
| Oracle Deadlock          | Automatic retry with jitter                  |
| Network Failure          | Circuit breaker with fallback strategies     |

## Testing

### Test Architecture

```
tests/
   unit/                           # Unit tests for core logic
   integration/                    # Oracle WMS integration tests
   examples/                       # Example usage tests
   e2e/                           # End-to-end workflow tests
   conftest.py                     # Pytest configuration and fixtures
```

### Test Categories

```bash
# Run specific test types
pytest -m unit                      # Unit tests only
pytest -m integration               # Integration tests requiring Oracle WMS
pytest -m oracle                    # Oracle WMS specific tests
pytest -m singer                    # Singer protocol tests
pytest -m e2e                       # End-to-end workflow tests
```

### Test Data

The project provides comprehensive test fixtures:

- **Sample WMS Data**: Representative WMS entity data for testing
- **Mock WMS API**: Simulated WMS endpoints for isolated testing
- **Configuration Variants**: Multiple config scenarios for testing

## Quality Standards

### Zero Tolerance Quality Gates

- **Test Coverage**: Minimum 90% (enforced by pytest-cov)
- **Type Safety**: Strict MyPy with no untyped code
- **Linting**: Ruff with ALL rules enabled (17 categories)
- **Security**: Bandit scanning + pip-audit for vulnerabilities
- **Pre-commit**: Automated quality checks on every commit

### Code Standards

- **Python 3.13+**: Latest Python with modern type hints
- **Clean Architecture**: Strict layer separation following FLEXT patterns
- **Domain-Driven Design**: Rich domain entities with business logic
- **DRY Principle**: Leverages existing `flext-oracle-wms` library

## Dependencies

### FLEXT Ecosystem Dependencies

- **flext-core**: Base patterns, logging, result handling
- **flext-oracle-wms**: Oracle WMS API client and data models
- **flext-meltano**: Singer/Meltano integration patterns
- **flext-observability**: Monitoring and metrics

### External Dependencies

- **singer-sdk**: Singer specification implementation
- **oracledb**: Modern Oracle database driver
- **pydantic**: Configuration validation and type safety

## Performance Optimization

### WMS Performance

- **Bulk Operations**: Oracle bulk binding for large datasets
- **Parallel Processing**: Configurable parallel degree
- **Connection Pooling**: Efficient connection management
- **WMS Hints**: Oracle hints optimized for WMS workloads

### Memory Management

- **Streaming Processing**: Process large datasets without loading into memory
- **Configurable Batching**: Adjustable batch sizes based on memory constraints
- **Resource Monitoring**: Built-in performance metrics and monitoring

### Best Practices

```json
{
  "batch_size": 1000,
  "parallel_degree": 4,
  "enable_bulk_binding": true,
  "connection_pool_size": 5,
  "enable_wms_hints": true
}
```

## Meltano Integration

This target is designed for use with Meltano orchestration:

```yaml
# meltano.yml
loaders:
  - name: target-oracle-wms
    variant: flext
    pip_url: flext-target-oracle-wms
    config:
      base_url: $WMS_BASE_URL
      auth_method: oauth2
      oauth_client_id: $WMS_CLIENT_ID
      oauth_client_secret: $WMS_CLIENT_SECRET
      company_code: $WMS_COMPANY_CODE
      facility_code: $WMS_FACILITY_CODE
      batch_size: 500
      validate_records: true
```

## Troubleshooting

### Common Issues

**WMS Connection Failures**:

- Verify WMS instance URL and accessibility
- Check authentication credentials and permissions
- Ensure WMS API access is enabled
- Validate company/facility codes

**Data Validation Errors**:

- Check item codes against WMS item master
- Verify location codes are valid in WMS
- Validate business rule constraints
- Review data format requirements

**Performance Issues**:

- Tune `batch_size` based on WMS capacity
- Adjust `parallel_degree` for Oracle optimization
- Monitor WMS system resource usage
- Enable performance logging for diagnostics

**Authentication Issues**:

- Verify OAuth2 client configuration and scopes
- Check token endpoint accessibility
- Ensure WMS license includes required modules

### Diagnostic Commands

```bash
# Project diagnostics
make diagnose                        # Complete system diagnostics
make doctor                          # Health check + diagnostics

# WMS-specific diagnostics
make wms-write-test                  # Test WMS write operations
make wms-entity-check                # Validate WMS entity mappings
make wms-connect                     # Test WMS connection
make wms-performance                 # Run WMS performance benchmarks
```

### Debug Configuration

```json
{
  "log_level": "DEBUG",
  "enable_performance_logging": true,
  "trace_sql_operations": true,
  "dry_run_mode": true,
  "validate_all_constraints": true
}
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run `make validate` before committing
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Documentation

### Architecture & Development

- [CLAUDE.md](CLAUDE.md) - Development guidance and architectural patterns
- [docs/](docs/) - Comprehensive project documentation

### Related Projects

- [../../flext-core/](../../flext-core/) - Foundation library with shared patterns
- [../../flext-oracle-wms/](../../flext-oracle-wms/) - Oracle WMS API client and data models
- [../../flext-meltano/](../../flext-meltano/) - Singer SDK integration

### Ecosystem Integration

- [../../flext-tap-oracle-wms/](../../flext-tap-oracle-wms/) - Corresponding Singer tap
- [../../flext-dbt-oracle-wms/](../../flext-dbt-oracle-wms/) - DBT models for WMS data transformation

---

**Framework**: FLEXT Ecosystem | **Protocol**: Singer SDK | **Language**: Python 3.13+ | **Architecture**: Clean Architecture + DDD | **Updated**: 2025-08-13
