# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""init module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.conftest import *
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.test_auth import *
    from tests.test_tap_core import *
    from tests.typings import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextTapOracleOicTestConstants": "tests.constants",
    "FlextTapOracleOicTestModels": "tests.models",
    "FlextTapOracleOicTestProtocols": "tests.protocols",
    "FlextTapOracleOicTestTypes": "tests.typings",
    "FlextTapOracleOicTestUtilities": "tests.utilities",
    "TestOICOAuth2Authenticator": "tests.test_auth",
    "TestTapOracleOic": "tests.test_tap_core",
    "TestTapOracleOicIntegration": "tests.test_tap_core",
    "TestTapOracleOicWithFixtures": "tests.test_tap_core",
    "basic_oic_config": "tests.conftest",
    "benchmark_config": "tests.conftest",
    "c": ("tests.constants", "FlextTapOracleOicTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_tests",
    "e": "flext_tests",
    "extended_oic_config": "tests.conftest",
    "filtered_oic_config": "tests.conftest",
    "h": "flext_tests",
    "large_integration_dataset": "tests.conftest",
    "m": ("tests.models", "FlextTapOracleOicTestModels"),
    "mock_connections_response": "tests.conftest",
    "mock_http_error_response": "tests.conftest",
    "mock_integrations_response": "tests.conftest",
    "mock_lookups_response": "tests.conftest",
    "mock_oauth_authenticator": "tests.conftest",
    "mock_oauth_token_response": "tests.conftest",
    "mock_oic_client": "tests.conftest",
    "mock_packages_response": "tests.conftest",
    "mock_rate_limit_response": "tests.conftest",
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTapOracleOicTestProtocols"),
    "performance_oic_config": "tests.conftest",
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_tests",
    "s": "flext_tests",
    "sample_adapter_data": "tests.conftest",
    "sample_certificate_data": "tests.conftest",
    "sample_config": "tests.test_tap_core",
    "sample_config_with_extended": "tests.test_tap_core",
    "sample_connection_data": "tests.conftest",
    "sample_integration_data": "tests.conftest",
    "sample_library_data": "tests.conftest",
    "sample_lookup_data": "tests.conftest",
    "sample_package_data": "tests.conftest",
    "set_test_environment": "tests.conftest",
    "singer_catalog": "tests.conftest",
    "singer_state": "tests.conftest",
    "t": ("tests.typings", "FlextTapOracleOicTestTypes"),
    "test_auth": "tests.test_auth",
    "test_tap": "tests.test_tap",
    "test_tap_core": "tests.test_tap_core",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTapOracleOicTestUtilities"),
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
