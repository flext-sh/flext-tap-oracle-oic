# FLEXT-TAP-ORACLE-OIC Makefile
# Migrated to use base.mk - 2026-01-03

PROJECT_NAME := flext-tap-oracle-oic
# Include shared base.mk for standard targets
ifneq ("$(wildcard ../base.mk)", "")
include ../base.mk
else
include base.mk
endif

# =============================================================================
# SINGER TAP CONFIGURATION
# =============================================================================

TAP_CONFIG ?= config.json
TAP_CATALOG ?= catalog.json
TAP_STATE ?= state.json

# =============================================================================
# SINGER TAP OPERATIONS
# =============================================================================

.PHONY: discover run catalog sync validate-config test-singer

discover: ## Run tap discovery mode
	$(POETRY) run tap-oracle-oic --config $(TAP_CONFIG) --discover > $(TAP_CATALOG)

run: ## Run tap extraction
	$(POETRY) run tap-oracle-oic --config $(TAP_CONFIG) --catalog $(TAP_CATALOG) --state $(TAP_STATE)

catalog: discover ## Alias for discover

sync: run ## Alias for run

validate-config: ## Validate tap configuration
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "import json; json.load(open('$(TAP_CONFIG)'))"

# =============================================================================
# OIC-SPECIFIC TARGETS
# =============================================================================

.PHONY: oic-test oic-endpoints oic-auth

oic-test: ## Test Oracle OIC API connectivity
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_tap_oracle_oic.client import test_connection; test_connection()"

oic-endpoints: ## List available Oracle OIC endpoints
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_tap_oracle_oic.client import list_endpoints; list_endpoints()"

oic-auth: ## Test Oracle OIC OAuth2 authentication
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -c "from flext_tap_oracle_oic.auth import test_auth; test_auth()"

# =============================================================================
# PROJECT-SPECIFIC TEST TARGETS
# =============================================================================

test-singer: ## Run Singer protocol tests
	$(POETRY) run pytest $(TESTS_DIR) -m singer -v
