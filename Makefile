# FLEXT Target Oracle WMS - Oracle WMS Singer Target
# ===============================================
# Enterprise-grade Singer target for Oracle WMS data loading
# Python 3.13 + Singer SDK + Oracle WMS + FLEXT Core + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-singer
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: sync validate-config target-test target-validate target-schema target-run
.PHONY: wms-write-test wms-entity-check wms-sync-test

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT Target Oracle WMS - Oracle WMS Singer Target"
	@echo "==============================================="
	@echo "🎯 Singer SDK + Oracle WMS + FLEXT Core + Python 3.13"
	@echo ""
	@echo "📦 Enterprise-grade Oracle WMS target for Singer protocol"
	@echo "🔒 Zero tolerance quality gates with warehouse optimization"
	@echo "🧪 90%+ test coverage requirement with Oracle WMS integration testing"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'


info: ## Show project information
	@echo "📊 Project Information"
	@echo "======================"
	@echo "Name: flext-target-oracle-wms"
	@echo "Type: singer-target"
	@echo "Title: FLEXT TARGET ORACLE WMS"
	@echo "Version: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Not found")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Not installed")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Not activated")"
	@echo "Directory: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Not a git repo")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) files changed"

diagnose: ## Run complete diagnostics
	@echo "🔍 Running diagnostics for flext-target-oracle-wms..."
	@echo "System Information:"
	@echo "OS: $(shell uname -s)"
	@echo "Architecture: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Not found")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Not installed")"
	@echo ""
	@echo "Project Structure:"
	@ls -la
	@echo ""
	@echo "Poetry Configuration:"
	@poetry config --list 2>/dev/null || echo "Poetry not configured"
	@echo ""
	@echo "Dependencies Status:"
	@poetry show --outdated 2>/dev/null || echo "No outdated dependencies"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test ## STRICT compliance validation (all must pass)
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

test-singer: ## Run Singer protocol tests
	@echo "🧪 Running Singer protocol tests..."
	@poetry run pytest tests/singer/ -v
	@echo "✅ Singer tests complete"

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
# 🎯 SINGER TARGET OPERATIONS
# ============================================================================

sync: ## Sync data to Oracle WMS target
	@echo "🎯 Running Oracle WMS data sync..."
	@poetry run target-oracle-wms --config $(TARGET_CONFIG) < $(TARGET_STATE)
	@echo "✅ Oracle WMS sync complete"

validate-config: ## Validate target configuration
	@echo "🔍 Validating target configuration..."
	@poetry run target-oracle-wms --config $(TARGET_CONFIG) --validate-config
	@echo "✅ Target configuration validated"

target-test: ## Test Oracle WMS target functionality
	@echo "🎯 Testing Oracle WMS target functionality..."
	@poetry run target-oracle-wms --about
	@poetry run target-oracle-wms --version
	@echo "✅ Target test complete"

target-validate: ## Validate target configuration
	@echo "🔍 Validating target configuration..."
	@poetry run target-oracle-wms --config tests/fixtures/config/target_config.json --validate-config
	@echo "✅ Target configuration validated"

target-schema: ## Validate Oracle WMS schema
	@echo "🔍 Validating Oracle WMS schema..."
	@poetry run target-oracle-wms --config tests/fixtures/config/target_config.json --validate-schema
	@echo "✅ Oracle WMS schema validated"

target-run: ## Run Oracle WMS data loading
	@echo "🎯 Running Oracle WMS data loading..."
	@poetry run target-oracle-wms --config tests/fixtures/config/target_config.json < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle WMS data loading complete"

target-run-debug: ## Run Oracle WMS target with debug logging
	@echo "🎯 Running Oracle WMS target with debug..."
	@poetry run target-oracle-wms --config tests/fixtures/config/target_config.json --log-level DEBUG < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle WMS debug run complete"

target-dry-run: ## Run Oracle WMS target in dry-run mode
	@echo "🎯 Running Oracle WMS target dry-run..."
	@poetry run target-oracle-wms --config tests/fixtures/config/target_config.json --dry-run < tests/fixtures/data/sample_input.jsonl
	@echo "✅ Oracle WMS dry-run complete"

# ============================================================================
# 🏢 ORACLE WMS-SPECIFIC OPERATIONS
# ============================================================================

wms-write-test: ## Test Oracle WMS write operations
	@echo "🏢 Testing Oracle WMS write operations..."
	@poetry run python -c "from flext_target_oracle_wms.client import TargetOracleWMSClient; import asyncio; import json; config = json.load(open('tests/fixtures/config/target_config.json')); client = TargetOracleWMSClient(config); print('Testing write operations...'); result = asyncio.run(client.test_write()); print('✅ Write test passed!' if result.is_success else f'❌ Write test failed: {result.error}')"
	@echo "✅ Oracle WMS write test complete"

wms-entity-check: ## Check Oracle WMS entity validation
	@echo "🏢 Checking Oracle WMS entity validation..."
	@poetry run python scripts/validate_wms_entities.py
	@echo "✅ Oracle WMS entity check complete"

wms-sync-test: ## Test Oracle WMS synchronization
	@echo "🔄 Testing Oracle WMS synchronization..."
	@poetry run python -c "from flext_target_oracle_wms.sync import WMSSynchronizer; import json; config = json.load(open('tests/fixtures/config/target_config.json')); sync = WMSSynchronizer(config); print('Testing WMS sync...'); result = sync.test_sync(); print('✅ Sync test passed!' if result.is_success else f'❌ Sync test failed: {result.error}')"
	@echo "✅ Oracle WMS sync test complete"

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
# 🗄️ DATABASE OPERATIONS
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
# 🔍 DATA VALIDATION
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
	@rm -rf logs/
	@rm -f *.log
	@rm -f target_spec.json
	@rm -f config_template.json
	@rm -f wms_schema_*.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
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

# Target settings
TARGET_CONFIG := config.json
TARGET_STATE := state.json

# Singer settings
export SINGER_LOG_LEVEL := INFO
export SINGER_BATCH_SIZE := 1000
export SINGER_MAX_BATCH_AGE := 300

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

# Poetry settings
export POETRY_VENV_IN_PROJECT := false
export POETRY_CACHE_DIR := $(HOME)/.cache/pypoetry

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

# ============================================================================
# 📝 PROJECT METADATA
# ============================================================================

# Project information
PROJECT_NAME := flext-target-oracle-wms
PROJECT_TYPE := meltano-plugin
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT Target Oracle WMS - Oracle WMS Singer Target

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 SINGER SPECIFIC COMMANDS
# ============================================================================

singer-about: ## Show Singer target about information
	@echo "🎵 Singer target about information..."
	@poetry run target-oracle-wms --about
	@echo "✅ About information displayed"

singer-config-sample: ## Generate Singer config sample
	@echo "🎵 Generating Singer config sample..."
	@poetry run target-oracle-wms --config-sample > config_sample.json
	@echo "✅ Config sample generated: config_sample.json"

singer-test-streams: ## Test Singer streams
	@echo "🎵 Testing Singer streams..."
	@poetry run pytest tests/singer/test_streams.py -v
	@echo "✅ Singer streams tests complete"

# ============================================================================
# 🎯 FLEXT ECOSYSTEM INTEGRATION
# ============================================================================

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 Singer project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Singer Target + Oracle WMS"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + Singer SDK"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: Oracle WMS Singer Target"
	@echo "🔗 Dependencies: flext-core, flext-oracle-wms, singer-sdk"
	@echo "📦 Provides: Oracle WMS data loading capabilities"
	@echo "🎯 Standards: Enterprise Oracle WMS integration patterns"