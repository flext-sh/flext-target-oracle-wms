# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `flext-target-oracle-wms`, a Singer target implementation for loading data into Oracle WMS (Warehouse Management System). It's part of the larger FLEXT ecosystem and implements enterprise-grade data loading patterns using Clean Architecture and Domain-Driven Design principles.

**Requirements**: Python 3.13+, Poetry for dependency management, Oracle WMS access

**Status**: Active Development - Production/Stable implementation with 90% test coverage requirement

## Architecture

### Core Components

- **Singer Target Implementation**: `src/flext_target_oracle_wms/target_client.py` - Main Singer protocol implementation (`SingerTargetOracleWMS`)
- **CLI Interface**: `src/flext_target_oracle_wms/cli.py` - Command-line interface for the target
- **Configuration Management**: `src/flext_target_oracle_wms/target_config.py` - Target configuration handling
- **Data Models**: `src/flext_target_oracle_wms/target_models.py` - WMS data transformation models
- **Factory Pattern**: `src/flext_target_oracle_wms/factory.py` - Factory for creating target instances

### Dependencies

The project leverages several FLEXT ecosystem libraries:

- `flext-core`: Base patterns, logging, result handling (`FlextResult`, `FlextValue`)
- `flext-oracle-wms`: Oracle WMS API client and data models
- `flext-meltano`: Singer/Meltano integration patterns (complete Singer SDK integration)
- `flext-observability`: Monitoring and metrics

### Key Design Patterns

- **DRY Implementation**: Uses the real `flext-oracle-wms` library to avoid code duplication
- **Factory Pattern**: `FlextTargetFactory` for creating configured target instances
- **Result Pattern**: `FlextResult` for railway-oriented programming and error handling
- **Clean Architecture**: Clear separation between Singer protocol, domain logic, and Oracle WMS integration
- **Consolidated Implementation**: All Singer components (target, catalog, stream processing) are unified in `target_client.py`

### Key Classes

- **`SingerTargetOracleWMS`**: Main target implementation with Singer protocol compliance
- **`SingerWMSCatalogManager`**: Catalog management for WMS streams
- **`SingerWMSStreamProcessor`**: Stream processing with WMS-specific logic
- **`WMSDataTransformer`**: Data transformation for WMS entities
- **`WMSTableManager`**: WMS table management and operations

## Development Commands

### Essential Commands

```bash
make validate          # Complete validation (lint + type + security + test) - ALL MUST PASS
make check             # Quick validation (lint + type + test)
make test              # Run tests with 90% coverage requirement
make lint              # Ruff linting with ALL rules enabled
make type-check        # MyPy strict type checking
make format            # Auto-format code with ruff
make fix               # Auto-fix issues and format code
make security          # Run security scanning (bandit + pip-audit)
```

### Project Setup Commands

```bash
make install           # Install dependencies with Poetry
make install-dev       # Install dev dependencies  
make setup             # Complete project setup with pre-commit hooks
make diagnose          # Project diagnostics
make doctor            # Health check + diagnostics
```

### Build and Package Commands

```bash
make build             # Build package
make build-clean       # Clean and build
make clean             # Clean build artifacts
make clean-all         # Deep clean including venv
make reset             # Reset project (clean-all + setup)
```

### Testing Commands

```bash
make test-unit         # Unit tests only
make test-integration  # Integration tests only  
make test-singer       # Singer protocol tests
make test-fast         # Run tests without coverage
make coverage-html     # Generate HTML coverage report
pytest -m unit         # Run unit tests by marker
pytest -m oracle       # Run Oracle WMS specific tests  
pytest -m slow         # Run slow tests
pytest -m integration  # Run integration tests
pytest -m smoke        # Run smoke tests
pytest -m e2e          # Run end-to-end tests
pytest -m performance  # Run performance tests
pytest -m resilience   # Run resilience tests
pytest -m integrity    # Run data integrity tests
pytest -m edge_cases   # Run edge case tests
```

### Singer Target Operations

```bash
make test-target       # Test basic target functionality
make validate-target-config  # Validate target configuration
make load              # Run target data loading
make dry-run           # Run target in dry-run mode
```

### Oracle WMS Specific Commands

```bash
make wms-write-test    # Test WMS write operations
make wms-entity-check  # Test Oracle WMS entity validation
make wms-sync-test     # Test Oracle WMS synchronization
make wms-connect       # Test Oracle WMS connection
make wms-schema        # Validate Oracle WMS schema
```

## CLI Usage

### Command Line Interface

The target provides two CLI entry points:

- `target-oracle-wms` - Main Singer target command
- `flext-target-oracle-wms` - Alternative entry point

### Basic CLI Commands

```bash
# Show target information
target-oracle-wms --about

# Show version
target-oracle-wms --version

# Run target with configuration
target-oracle-wms --config config.json

# Run with state file
target-oracle-wms --config config.json --state state.json

# Dry run mode for testing
target-oracle-wms --config config.json --dry-run
```

## Configuration

### Environment Variables

The target uses these key environment variables:

**Oracle WMS Connection:**

- `TARGET_ORACLE_WMS_HOST`: Oracle WMS server hostname
- `TARGET_ORACLE_WMS_PORT`: Database port (default: 1521)
- `TARGET_ORACLE_WMS_SERVICE_NAME`: Oracle service name
- `TARGET_ORACLE_WMS_SCHEMA`: WMS schema name

**Performance Settings:**

- `TARGET_ORACLE_WMS_BATCH_SIZE`: Batch size for data loading (default: 1000)
- `TARGET_ORACLE_WMS_PARALLEL_DEGREE`: Parallel processing degree (default: 4)
- `TARGET_ORACLE_WMS_ENABLE_BULK_BINDING`: Enable bulk binding for performance

**Data Validation:**

- `TARGET_ORACLE_WMS_VALIDATE_RECORDS`: Enable record validation
- `TARGET_ORACLE_WMS_VALIDATE_ITEM_CODES`: Validate item codes
- `TARGET_ORACLE_WMS_VALIDATE_LOCATION_CODES`: Validate location codes

### Singer Configuration

The target expects a Singer configuration file with these sections:

- Database connection parameters
- WMS-specific settings (facility_code, organization_id)
- Performance tuning parameters
- Validation rules and constraints

## Quality Standards

### Zero Tolerance Quality Gates

- **Test Coverage**: Minimum 90% required (`--cov-fail-under=90`)
- **Type Safety**: Strict MyPy with no `Any` types allowed
- **Linting**: Ruff with ALL rules enabled (17 categories)
- **Security**: Bandit security scanning + pip-audit vulnerability checks
- **Pre-commit**: All quality gates must pass before commits

### Testing Strategy

- **Unit Tests**: Core business logic and domain patterns
- **Integration Tests**: Oracle WMS API integration
- **Singer Tests**: Singer protocol compliance
- **E2E Tests**: Complete data loading workflows
- **Performance Tests**: Bulk loading and optimization

## Singer Protocol Implementation

### Target Capabilities

- Supports Singer SCHEMA, RECORD, and STATE messages
- Handles stream-to-table mapping for WMS entities
- Implements proper error handling and logging
- Supports batch processing and bulk loading
- Validates data against WMS business rules

### Stream Processing

The target processes these WMS data streams:

- Inventory transactions and adjustments
- Shipment and receipt records
- Labor and task management data
- Location and item master data
- Cross-docking and wave planning data

### Error Handling

- Uses `FlextResult` pattern for consistent error handling
- Implements retry logic for transient failures
- Provides detailed error messages with context
- Supports partial batch processing on errors

## Common Workflows

### Adding New WMS Entity Support

1. Define entity model in `target_models.py` (WMS data transformation models)
2. Update the main target implementation in `target_client.py`
3. Add stream processing logic in `SingerTargetOracleWMS` class
4. Add comprehensive tests for the new entity
5. Update schema mappings and validation rules in configuration

### Performance Optimization

1. Use WMS-specific Oracle hints (`ENABLE_WMS_HINTS=true`)
2. Enable bulk binding for large datasets
3. Tune batch sizes based on data volume
4. Monitor performance with built-in metrics
5. Use parallel processing for independent streams

### Debugging Data Issues

1. Enable debug logging: `--log-level DEBUG`
2. Use dry-run mode to test transformations
3. Validate schema mappings with `make wms-schema`
4. Check data quality with validation scripts
5. Review WMS constraints and business rules

## File Structure

### Source Code Organization

```
src/flext_target_oracle_wms/
├── __init__.py           # Main exports and flext-meltano integration
├── cli.py               # Command-line interface (OracleWMSTargetCli)
├── factory.py           # Factory patterns for target creation
├── exceptions.py        # Custom exceptions
├── models.py            # Data models (legacy)
├── target_client.py     # Main Singer target implementation (SingerTargetOracleWMS)
├── target_config.py     # Configuration management
├── target_models.py     # WMS data transformation models
├── typings.py           # Type definitions
└── py.typed             # Type marker file
```

### Test Organization

```
tests/
├── unit/                # Unit tests for core logic
├── integration/         # Oracle WMS integration tests
├── examples/           # Example usage tests
├── e2e/                # End-to-end workflow tests
└── conftest.py          # Pytest configuration and fixtures
```

## Best Practices

### Code Organization

- Follow Clean Architecture boundaries strictly
- Use dependency injection via factory patterns
- Implement proper error handling with `FlextResult`
- Leverage existing `flext-oracle-wms` library (DRY principle)
- Maintain comprehensive test coverage (90%+ required)

### WMS Data Handling

- Always validate WMS business constraints
- Use appropriate Oracle hints for WMS tables
- Implement proper transaction boundaries
- Handle WMS-specific error codes and messages
- Support both real-time and batch processing modes

### Performance Considerations

- Use bulk binding for large datasets
- Implement proper connection pooling
- Monitor Oracle WMS system resources
- Tune batch sizes based on data characteristics
- Enable parallel processing where appropriate

### Error Recovery

- Implement retry logic for transient failures
- Support partial batch processing
- Provide detailed error context and suggestions
- Log errors appropriately for troubleshooting
- Support resume capability for long-running loads
