# Private project handlers for flext-tap-oracle-oic.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Each handler maps to `make <verb> WHAT=<what>`.
.PHONY: _custom_run_discover _custom_run_tap _custom_run_oic-test _custom_test_singer
_custom_run_discover: ## make run WHAT=discover — tap discovery -> catalog.json
	$(Q)$(POETRY) run tap-oracle-oic --config config.json --discover > catalog.json
_custom_run_tap: ## make run WHAT=tap — tap extraction
	$(Q)$(POETRY) run tap-oracle-oic --config config.json --catalog catalog.json --state state.json
_custom_run_oic-test: ## make run WHAT=oic-test — test Oracle OIC connectivity
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_tap_oracle_oic.client import test_connection; test_connection()"
_custom_test_singer: ## make test WHAT=singer — Singer protocol tests
	$(Q)$(POETRY) run pytest $(TESTS_DIR) -m singer -v
