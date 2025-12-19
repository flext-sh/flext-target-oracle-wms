# flext-target-oracle-wms - Oracle WMS Singer Target
PROJECT_NAME := flext-target-oracle-wms
COV_DIR := flext_target_oracle_wms
MIN_COVERAGE := 90

include ../base.mk

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: target-run test-unit test-integration build shell

target-run: ## Run target with config
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run target-oracle-wms --config config.json

.DEFAULT_GOAL := help
