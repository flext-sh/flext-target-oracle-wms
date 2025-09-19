# FLEXT Project Purpose and Tech Stack

## Project Purpose

FLEXT is an enterprise-grade data integration platform under active development that orchestrates, monitors, and manages distributed data pipelines. Built with a hybrid Go/Python architecture implementing Clean Architecture, DDD, and CQRS patterns.

## Tech Stack

- **Python**: 3.13+ (Primary language)
- **Go**: For core runtime and performance-critical components
- **Framework**: Pydantic v2 for data validation and models
- **Architecture**: Clean Architecture + Domain-Driven Design + CQRS patterns
- **Dependency Management**: Poetry
- **Virtual Environment**: ~/flext/.venv
- **Version**: 0.9.0 (preparing for 1.0.0 stable release)

## Core Technologies

- **Pydantic v2**: Data validation and serialization
- **Click**: CLI framework (through flext-cli abstraction)
- **Rich**: Terminal UI (through flext-cli abstraction)
- **StructLog**: Structured logging
- **Docker**: Containerization
- **PyYAML**: Configuration management
- **Protobuf**: Service communication

## Architecture

- **flext-core**: Foundation library (0.9.9 RC, 79% test coverage)
- **Monorepo Structure**: 30+ subprojects
- **Domain Separation**: Each flext-\* project has specific responsibility
- **Railway Pattern**: FlextResult[T] for error handling
- **Dependency Injection**: FlextContainer.get_global()
- **One Class Per Module**: Unified service classes with nested helpers
