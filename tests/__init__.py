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
    from flext_tests import d, e, h, r, s, x

    from tests import (
        conftest as conftest,
        constants as constants,
        models as models,
        protocols as protocols,
        test_auth as test_auth,
        test_tap as test_tap,
        test_tap_core as test_tap_core,
        typings as typings,
        utilities as utilities,
    )
    from tests.conftest import (
        basic_oic_config as basic_oic_config,
        benchmark_config as benchmark_config,
        extended_oic_config as extended_oic_config,
        filtered_oic_config as filtered_oic_config,
        large_integration_dataset as large_integration_dataset,
        mock_connections_response as mock_connections_response,
        mock_http_error_response as mock_http_error_response,
        mock_integrations_response as mock_integrations_response,
        mock_lookups_response as mock_lookups_response,
        mock_oauth_authenticator as mock_oauth_authenticator,
        mock_oauth_token_response as mock_oauth_token_response,
        mock_oic_client as mock_oic_client,
        mock_packages_response as mock_packages_response,
        mock_rate_limit_response as mock_rate_limit_response,
        performance_oic_config as performance_oic_config,
        pytest_configure as pytest_configure,
        sample_adapter_data as sample_adapter_data,
        sample_certificate_data as sample_certificate_data,
        sample_connection_data as sample_connection_data,
        sample_integration_data as sample_integration_data,
        sample_library_data as sample_library_data,
        sample_lookup_data as sample_lookup_data,
        sample_package_data as sample_package_data,
        set_test_environment as set_test_environment,
        singer_catalog as singer_catalog,
        singer_state as singer_state,
    )
    from tests.constants import (
        FlextTapOracleOicTestConstants as FlextTapOracleOicTestConstants,
        FlextTapOracleOicTestConstants as c,
    )
    from tests.models import (
        FlextTapOracleOicTestModels as FlextTapOracleOicTestModels,
        FlextTapOracleOicTestModels as m,
    )
    from tests.protocols import (
        FlextTapOracleOicTestProtocols as FlextTapOracleOicTestProtocols,
        FlextTapOracleOicTestProtocols as p,
    )
    from tests.test_auth import TestOICOAuth2Authenticator as TestOICOAuth2Authenticator
    from tests.test_tap_core import (
        TestTapOracleOic as TestTapOracleOic,
        TestTapOracleOicIntegration as TestTapOracleOicIntegration,
        TestTapOracleOicWithFixtures as TestTapOracleOicWithFixtures,
        sample_config as sample_config,
        sample_config_with_extended as sample_config_with_extended,
    )
    from tests.typings import (
        FlextTapOracleOicTestTypes as FlextTapOracleOicTestTypes,
        FlextTapOracleOicTestTypes as t,
    )
    from tests.utilities import (
        FlextTapOracleOicTestUtilities as FlextTapOracleOicTestUtilities,
        FlextTapOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTapOracleOicTestConstants": ["tests.constants", "FlextTapOracleOicTestConstants"],
    "FlextTapOracleOicTestModels": ["tests.models", "FlextTapOracleOicTestModels"],
    "FlextTapOracleOicTestProtocols": ["tests.protocols", "FlextTapOracleOicTestProtocols"],
    "FlextTapOracleOicTestTypes": ["tests.typings", "FlextTapOracleOicTestTypes"],
    "FlextTapOracleOicTestUtilities": ["tests.utilities", "FlextTapOracleOicTestUtilities"],
    "TestOICOAuth2Authenticator": ["tests.test_auth", "TestOICOAuth2Authenticator"],
    "TestTapOracleOic": ["tests.test_tap_core", "TestTapOracleOic"],
    "TestTapOracleOicIntegration": ["tests.test_tap_core", "TestTapOracleOicIntegration"],
    "TestTapOracleOicWithFixtures": ["tests.test_tap_core", "TestTapOracleOicWithFixtures"],
    "basic_oic_config": ["tests.conftest", "basic_oic_config"],
    "benchmark_config": ["tests.conftest", "benchmark_config"],
    "c": ["tests.constants", "FlextTapOracleOicTestConstants"],
    "conftest": ["tests.conftest", ""],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "e": ["flext_tests", "e"],
    "extended_oic_config": ["tests.conftest", "extended_oic_config"],
    "filtered_oic_config": ["tests.conftest", "filtered_oic_config"],
    "h": ["flext_tests", "h"],
    "large_integration_dataset": ["tests.conftest", "large_integration_dataset"],
    "m": ["tests.models", "FlextTapOracleOicTestModels"],
    "mock_connections_response": ["tests.conftest", "mock_connections_response"],
    "mock_http_error_response": ["tests.conftest", "mock_http_error_response"],
    "mock_integrations_response": ["tests.conftest", "mock_integrations_response"],
    "mock_lookups_response": ["tests.conftest", "mock_lookups_response"],
    "mock_oauth_authenticator": ["tests.conftest", "mock_oauth_authenticator"],
    "mock_oauth_token_response": ["tests.conftest", "mock_oauth_token_response"],
    "mock_oic_client": ["tests.conftest", "mock_oic_client"],
    "mock_packages_response": ["tests.conftest", "mock_packages_response"],
    "mock_rate_limit_response": ["tests.conftest", "mock_rate_limit_response"],
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextTapOracleOicTestProtocols"],
    "performance_oic_config": ["tests.conftest", "performance_oic_config"],
    "protocols": ["tests.protocols", ""],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_adapter_data": ["tests.conftest", "sample_adapter_data"],
    "sample_certificate_data": ["tests.conftest", "sample_certificate_data"],
    "sample_config": ["tests.test_tap_core", "sample_config"],
    "sample_config_with_extended": ["tests.test_tap_core", "sample_config_with_extended"],
    "sample_connection_data": ["tests.conftest", "sample_connection_data"],
    "sample_integration_data": ["tests.conftest", "sample_integration_data"],
    "sample_library_data": ["tests.conftest", "sample_library_data"],
    "sample_lookup_data": ["tests.conftest", "sample_lookup_data"],
    "sample_package_data": ["tests.conftest", "sample_package_data"],
    "set_test_environment": ["tests.conftest", "set_test_environment"],
    "singer_catalog": ["tests.conftest", "singer_catalog"],
    "singer_state": ["tests.conftest", "singer_state"],
    "t": ["tests.typings", "FlextTapOracleOicTestTypes"],
    "test_auth": ["tests.test_auth", ""],
    "test_tap": ["tests.test_tap", ""],
    "test_tap_core": ["tests.test_tap_core", ""],
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextTapOracleOicTestUtilities"],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextTapOracleOicTestConstants",
    "FlextTapOracleOicTestModels",
    "FlextTapOracleOicTestProtocols",
    "FlextTapOracleOicTestTypes",
    "FlextTapOracleOicTestUtilities",
    "TestOICOAuth2Authenticator",
    "TestTapOracleOic",
    "TestTapOracleOicIntegration",
    "TestTapOracleOicWithFixtures",
    "basic_oic_config",
    "benchmark_config",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "extended_oic_config",
    "filtered_oic_config",
    "h",
    "large_integration_dataset",
    "m",
    "mock_connections_response",
    "mock_http_error_response",
    "mock_integrations_response",
    "mock_lookups_response",
    "mock_oauth_authenticator",
    "mock_oauth_token_response",
    "mock_oic_client",
    "mock_packages_response",
    "mock_rate_limit_response",
    "models",
    "p",
    "performance_oic_config",
    "protocols",
    "pytest_configure",
    "r",
    "s",
    "sample_adapter_data",
    "sample_certificate_data",
    "sample_config",
    "sample_config_with_extended",
    "sample_connection_data",
    "sample_integration_data",
    "sample_library_data",
    "sample_lookup_data",
    "sample_package_data",
    "set_test_environment",
    "singer_catalog",
    "singer_state",
    "t",
    "test_auth",
    "test_tap",
    "test_tap_core",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
