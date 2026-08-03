# Private project handlers for flext-target-oracle-wms.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Each handler maps to `make <verb> WHAT=<what>`.
.PHONY: _custom_run_load _custom_run_target-test _custom_test_singer
_custom_run_load: ## make run WHAT=load — target data loading
	$(Q)$(POETRY) run target-oracle-wms --config config.json --state state.json
_custom_run_target-test: ## make run WHAT=target-test — target about/version
	$(Q)$(POETRY) run target-oracle-wms --about
	$(Q)$(POETRY) run target-oracle-wms --version
_custom_test_singer: ## make test WHAT=singer — Singer protocol tests
	$(Q)$(POETRY) run pytest $(TESTS_DIR) -m singer -v
