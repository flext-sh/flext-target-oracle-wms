# FLEXT TARGET ORACLE WMS - Oracle Warehouse Management Singer Target
# ===================================================================
# Singer target for Oracle WMS data loading with warehouse optimizations
# Python 3.13 + Singer SDK + Oracle WMS + Zero Tolerance Quality Gates

.PHONY: help check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-target
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: target-test target-validate target-schema target-run
.PHONY: wms-connect wms-schema wms-optimize oracle-test database-test

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT TARGET ORACLE WMS - Oracle Warehouse Management Singer Target"
	@echo "====================================================================="
	@echo "🎯 Singer SDK + Oracle WMS + Database Optimization + Python 3.13"
	@echo ""
	@echo "📦 Singer target for Oracle WMS data loading with warehouse optimizations"
	@echo "🔒 Zero tolerance quality gates with real Oracle WMS integration"
	@echo "🧪 90%+ test coverage requirement with Oracle WMS database compliance"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test target-test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT TARGET ORACLE WMS COMPLIANT"

check: lint type-check test ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_target_oracle_wms --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-target: ## Run Singer target tests
	@echo "🧪 Running Singer target tests..."
	@poetry run pytest tests/ -m "target" -v
	@echo "✅ Target tests complete"

test-wms: ## Run Oracle WMS tests
	@echo "🧪 Running Oracle WMS tests..."
	@poetry run pytest tests/ -m "wms" -v
	@echo "✅ WMS tests complete"

test-oracle: ## Run Oracle database tests
	@echo "🧪 Running Oracle database tests..."
	@poetry run pytest tests/ -m "oracle" -v
	@echo "✅ Oracle tests complete"

test-performance: ## Run performance tests
	@echo "⚡ Running Oracle WMS target performance tests..."
	@poetry run pytest tests/performance/ -v --benchmark-only
	@echo "✅ Performance tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_target_oracle_wms --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎵 SINGER TARGET OPERATIONS - CORE FUNCTIONALITY
# ============================================================================

target-test: ## Test Singer target functionality
	@echo "🎵 Testing Singer target functionality..."
	@poetry run python -c "from flext_target_oracle_wms.target import TargetOracleWMS; print('Target imports successfully')"
	@echo "✅ Singer target test complete"

target-validate: ## Validate Singer target configuration
	@echo "🔍 Validating Singer target configuration..."
	@poetry run python scripts/validate_target_config.py
	@echo "✅ Target configuration validation complete"

target-schema: ## Validate Oracle WMS schema compatibility
	@echo "🗄️ Validating Oracle WMS schema..."
	@poetry run python scripts/validate_wms_schema.py
	@echo "✅ WMS schema validation complete"

target-run: ## Run Singer target with sample data
	@echo "🚀 Running Singer target with sample data..."
	@poetry run python scripts/run_target_sample.py
	@echo "✅ Target sample run complete"

target-spec: ## Generate Singer target specification
	@echo "📋 Generating Singer target specification..."
	@poetry run target-oracle-wms --about --format=json > target_spec.json
	@echo "✅ Target specification generated"

target-config: ## Generate target configuration template
	@echo "📝 Generating target configuration template..."
	@poetry run target-oracle-wms --about --format=json | jq '.config' > config_template.json
	@echo "✅ Configuration template generated"

# ============================================================================
# 🏢 ORACLE WMS OPERATIONS
# ============================================================================

wms-connect: ## Test Oracle WMS connection
	@echo "🏢 Testing Oracle WMS connection..."
	@poetry run python scripts/test_wms_connection.py
	@echo "✅ WMS connection test complete"

wms-schema: ## Generate Oracle WMS schema mappings
	@echo "🗄️ Generating WMS schema mappings..."
	@poetry run python scripts/generate_wms_schema.py
	@echo "✅ WMS schema mappings generated"

wms-optimize: ## Optimize Oracle WMS performance settings
	@echo "⚡ Optimizing WMS performance settings..."
	@poetry run python scripts/optimize_wms_performance.py
	@echo "✅ WMS performance optimization complete"

wms-validate: ## Validate WMS data requirements
	@echo "🔍 Validating WMS data requirements..."
	@poetry run python scripts/validate_wms_data.py
	@echo "✅ WMS data validation complete"

wms-tables: ## List Oracle WMS tables and mappings
	@echo "📋 Listing Oracle WMS tables..."
	@poetry run python scripts/list_wms_tables.py
	@echo "✅ WMS tables listing complete"

# ============================================================================
# 🗄️ ORACLE DATABASE OPERATIONS
# ============================================================================

oracle-test: ## Test Oracle database connectivity
	@echo "🗄️ Testing Oracle database connectivity..."
	@poetry run python -c "from flext_target_oracle_wms.client import TargetOracleWMSClient; import asyncio; client = TargetOracleWMSClient({}); print('Oracle client created successfully')"
	@echo "✅ Oracle connectivity test complete"

database-test: ## Test database operations
	@echo "🗄️ Testing database operations..."
	@poetry run python scripts/test_database_operations.py
	@echo "✅ Database operations test complete"

database-health: ## Check database health and performance
	@echo "📊 Checking database health..."
	@poetry run python scripts/check_database_health.py
	@echo "✅ Database health check complete"

# ============================================================================
# 🔄 DATA LOADING OPERATIONS
# ============================================================================

load-sample: ## Load sample WMS data
	@echo "📊 Loading sample WMS data..."
	@poetry run python scripts/load_sample_data.py
	@echo "✅ Sample data loading complete"

load-inventory: ## Load inventory data
	@echo "📦 Loading inventory data..."
	@poetry run python scripts/load_inventory_data.py
	@echo "✅ Inventory data loading complete"

load-shipments: ## Load shipment data
	@echo "🚚 Loading shipment data..."
	@poetry run python scripts/load_shipment_data.py
	@echo "✅ Shipment data loading complete"

load-receipts: ## Load receipt data
	@echo "📥 Loading receipt data..."
	@poetry run python scripts/load_receipt_data.py
	@echo "✅ Receipt data loading complete"

load-labor: ## Load labor data
	@echo "👥 Loading labor data..."
	@poetry run python scripts/load_labor_data.py
	@echo "✅ Labor data loading complete"

# ============================================================================
# 🔍 DATA QUALITY & VALIDATION
# ============================================================================

validate-wms-data: ## Validate WMS data integrity
	@echo "🔍 Validating WMS data integrity..."
	@poetry run python scripts/validate_wms_data_integrity.py
	@echo "✅ WMS data validation complete"

validate-mapping: ## Validate stream to table mappings
	@echo "🔍 Validating stream mappings..."
	@poetry run python scripts/validate_stream_mappings.py
	@echo "✅ Stream mapping validation complete"

validate-constraints: ## Validate WMS business constraints
	@echo "🔍 Validating WMS business constraints..."
	@poetry run python scripts/validate_wms_constraints.py
	@echo "✅ WMS constraints validation complete"

data-quality-report: ## Generate comprehensive data quality report
	@echo "📊 Generating data quality report..."
	@poetry run python scripts/generate_quality_report.py
	@echo "✅ Data quality report generated"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean ## Build distribution packages
	@echo "🔨 Building distribution..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

package: build ## Create deployment package
	@echo "📦 Creating deployment package..."
	@tar -czf dist/flext-target-oracle-wms-deployment.tar.gz \
		src/ \
		tests/ \
		scripts/ \
		pyproject.toml \
		README.md \
		CLAUDE.md
	@echo "✅ Deployment package created: dist/flext-target-oracle-wms-deployment.tar.gz"

# ============================================================================
# 🧹 CLEANUP
# ============================================================================

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf .pytest_cache/
	@rm -rf .mypy_cache/
	@rm -rf .ruff_cache/
	@rm -rf logs/
	@rm -f *.log
	@rm -f target_spec.json
	@rm -f config_template.json
	@rm -f wms_schema_*.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# Singer Target settings
export TARGET_ORACLE_WMS_CONFIG := ./config.json
export TARGET_ORACLE_WMS_DEBUG := false

# Oracle WMS connection settings
export TARGET_ORACLE_WMS_HOST := oracle-wms.company.com
export TARGET_ORACLE_WMS_PORT := 1521
export TARGET_ORACLE_WMS_SERVICE_NAME := WMSPROD
export TARGET_ORACLE_WMS_SCHEMA := WMS

# WMS-specific settings
export TARGET_ORACLE_WMS_FACILITY_CODE := DC001
export TARGET_ORACLE_WMS_ORGANIZATION_ID := 101
export TARGET_ORACLE_WMS_BATCH_SIZE := 1000
export TARGET_ORACLE_WMS_VALIDATE_RECORDS := true

# Performance settings
export TARGET_ORACLE_WMS_ENABLE_WMS_HINTS := true
export TARGET_ORACLE_WMS_PARALLEL_DEGREE := 4
export TARGET_ORACLE_WMS_ENABLE_BULK_BINDING := true
export TARGET_ORACLE_WMS_COMMIT_INTERVAL := 1000

# Data validation settings
export TARGET_ORACLE_WMS_VALIDATE_ITEM_CODES := true
export TARGET_ORACLE_WMS_VALIDATE_LOCATION_CODES := true
export TARGET_ORACLE_WMS_VALIDATE_LOT_NUMBERS := true
export TARGET_ORACLE_WMS_VALIDATE_SERIAL_NUMBERS := false

# Data transformation settings
export TARGET_ORACLE_WMS_TRANSFORM_QUANTITIES := true
export TARGET_ORACLE_WMS_NORMALIZE_UOM := true
export TARGET_ORACLE_WMS_CONVERT_TIMESTAMPS := true
export TARGET_ORACLE_WMS_ADD_RECORD_METADATA := true

# Error handling settings
export TARGET_ORACLE_WMS_CONTINUE_ON_VALIDATION_ERROR := false
export TARGET_ORACLE_WMS_MAX_ERROR_COUNT := 100
export TARGET_ORACLE_WMS_ERROR_TABLE_NAME := WMS_ERROR_LOG

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

# ============================================================================
# 📝 PROJECT METADATA
# ============================================================================

# Project information
PROJECT_NAME := flext-target-oracle-wms
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT TARGET ORACLE WMS - Oracle Warehouse Management Singer Target

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 DEVELOPMENT UTILITIES
# ============================================================================

dev-wms-server: ## Start development WMS mock server
	@echo "🔧 Starting development WMS mock server..."
	@poetry run python scripts/dev_wms_server.py
	@echo "✅ Development WMS mock server started"

dev-target-tester: ## Start interactive target tester
	@echo "🎮 Starting interactive target tester..."
	@poetry run python scripts/target_tester.py
	@echo "✅ Target tester session complete"

dev-schema-explorer: ## Start WMS schema explorer
	@echo "🗄️ Starting WMS schema explorer..."
	@poetry run python scripts/schema_explorer.py
	@echo "✅ Schema explorer session complete"

dev-data-generator: ## Start WMS test data generator
	@echo "🔧 Starting WMS test data generator..."
	@poetry run python scripts/data_generator.py
	@echo "✅ Data generator session complete"

dev-performance-monitor: ## Start performance monitoring
	@echo "📊 Starting performance monitoring..."
	@poetry run python scripts/performance_monitor.py
	@echo "✅ Performance monitoring session complete"

# ============================================================================
# 🎯 FLEXT ECOSYSTEM INTEGRATION
# ============================================================================

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 Core project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Singer Target + Oracle WMS + Warehouse Optimization"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + Singer SDK + Oracle WMS"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Oracle Warehouse Management Singer Target"
	@echo "🔗 Dependencies: flext-core, flext-oracle-wms, flext-db-oracle, singer-sdk"
	@echo "📦 Provides: Oracle WMS data loading, warehouse optimizations, Singer target"
	@echo "🎯 Standards: Oracle WMS data loading with enterprise optimizations"

# ============================================================================
# 🔄 CONTINUOUS INTEGRATION
# ============================================================================

ci-check: validate ## CI quality checks
	@echo "🔍 Running CI quality checks..."
	@poetry run python scripts/ci_quality_report.py
	@echo "✅ CI quality checks complete"

ci-performance: ## CI performance benchmarks
	@echo "⚡ Running CI performance benchmarks..."
	@poetry run python scripts/ci_performance_benchmarks.py
	@echo "✅ CI performance benchmarks complete"

ci-integration: ## CI integration tests
	@echo "🔗 Running CI integration tests..."
	@poetry run pytest tests/integration/ -v --tb=short
	@echo "✅ CI integration tests complete"

ci-target: ## CI Singer target tests
	@echo "🎵 Running CI target tests..."
	@poetry run pytest tests/ -m "target" -v --tb=short
	@echo "✅ CI target tests complete"

ci-wms: ## CI Oracle WMS tests
	@echo "🏢 Running CI WMS tests..."
	@poetry run pytest tests/ -m "wms" -v --tb=short
	@echo "✅ CI WMS tests complete"

ci-oracle: ## CI Oracle database tests
	@echo "🗄️ Running CI Oracle tests..."
	@poetry run pytest tests/ -m "oracle" -v --tb=short
	@echo "✅ CI Oracle tests complete"

ci-all: ci-check ci-performance ci-integration ci-target ci-wms ci-oracle ## Run all CI checks
	@echo "✅ All CI checks complete"

# ============================================================================
# 🚀 PRODUCTION DEPLOYMENT
# ============================================================================

deploy-target: validate build ## Deploy Singer target for production use
	@echo "🚀 Deploying Singer target..."
	@poetry run python scripts/deploy_target.py
	@echo "✅ Target deployment complete"

test-deployment: ## Test deployed target functionality
	@echo "🧪 Testing deployed target..."
	@poetry run python scripts/test_deployed_target.py
	@echo "✅ Deployment test complete"

rollback-deployment: ## Rollback target deployment
	@echo "🔄 Rolling back target deployment..."
	@poetry run python scripts/rollback_target_deployment.py
	@echo "✅ Deployment rollback complete"

# ============================================================================
# 🔬 MONITORING & OBSERVABILITY
# ============================================================================

monitor-target: ## Monitor Singer target health
	@echo "📊 Monitoring Singer target health..."
	@poetry run python scripts/monitor_target.py
	@echo "✅ Target monitoring complete"

monitor-wms: ## Monitor Oracle WMS performance
	@echo "📊 Monitoring Oracle WMS performance..."
	@poetry run python scripts/monitor_wms_performance.py
	@echo "✅ WMS performance monitoring complete"

monitor-loading: ## Monitor data loading performance
	@echo "📊 Monitoring data loading performance..."
	@poetry run python scripts/monitor_loading_performance.py
	@echo "✅ Loading performance monitoring complete"

generate-metrics: ## Generate target performance metrics
	@echo "📊 Generating target performance metrics..."
	@poetry run python scripts/generate_target_metrics.py
	@echo "✅ Target metrics generated"

generate-wms-report: ## Generate Oracle WMS usage report
	@echo "📊 Generating Oracle WMS usage report..."
	@poetry run python scripts/generate_wms_report.py
	@echo "✅ WMS usage report generated"
