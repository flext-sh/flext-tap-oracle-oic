# flext-tap-oracle-oic - Oracle OIC Singer Tap
PROJECT_NAME := flext-tap-oracle-oic
COV_DIR := flext_tap_oracle_oic
MIN_COVERAGE := 90

include ../base.mk

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: tap-run tap-discover test-unit test-integration build shell

tap-run: ## Run tap with config
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run tap-oracle-oic --config config.json

tap-discover: ## Run discovery mode
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run tap-oracle-oic --config config.json --discover

.DEFAULT_GOAL := help
