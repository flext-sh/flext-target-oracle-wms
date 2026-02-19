# FLEXT-TARGET-ORACLE-WMS Makefile
# Migrated to use base.mk - 2026-01-03

PROJECT_NAME := flext-target-oracle-wms
# Include shared base.mk for standard targets
include ../base.mk

# =============================================================================
# SINGER TARGET CONFIGURATION
# =============================================================================

TARGET_CONFIG ?= config.json
TARGET_STATE ?= state.json

# =============================================================================
# SINGER TARGET OPERATIONS
# =============================================================================

.PHONY: load validate-target-config test-target dry-run test-singer

load: ## Run target data loading
	$(POETRY) run target-oracle-wms --config $(TARGET_CONFIG) --state $(TARGET_STATE)

validate-target-config: ## Validate target configuration
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "import json; json.load(open('$(TARGET_CONFIG)'))"

test-target: ## Test target functionality
	$(POETRY) run target-oracle-wms --about
	$(POETRY) run target-oracle-wms --version

dry-run: ## Run target in dry-run mode
	$(POETRY) run target-oracle-wms --config $(TARGET_CONFIG) --dry-run

# =============================================================================
# WMS-SPECIFIC TARGETS
# =============================================================================

.PHONY: wms-connect wms-schema wms-write-test wms-entity-check wms-sync-test

wms-connect: ## Test Oracle WMS connection
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_wms.client import test_connection; test_connection()"

wms-schema: ## Validate Oracle WMS schema
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_wms.schema import validate_schema; validate_schema()"

wms-write-test: ## Test Oracle WMS write operations
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_wms.operations import test_write; test_write()"

wms-entity-check: ## Test Oracle WMS entity validation
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_wms.entities import test_entities; test_entities()"

wms-sync-test: ## Test Oracle WMS synchronization
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_target_oracle_wms.sync import test_sync; test_sync()"

# =============================================================================
# PROJECT-SPECIFIC TEST TARGETS
# =============================================================================

test-singer: ## Run Singer protocol tests
	$(POETRY) run pytest $(TESTS_DIR) -m singer -v
