# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""init module.

This module is part of the FLEXT ecosystem. Docstrings follow PEP 257 and Google style.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tests import d, e, h, r, s, x

    from tests.conftest import (
        basic_oic_config,
        benchmark_config,
        extended_oic_config,
        filtered_oic_config,
        large_integration_dataset,
        mock_connections_response,
        mock_http_error_response,
        mock_integrations_response,
        mock_lookups_response,
        mock_oauth_authenticator,
        mock_oauth_token_response,
        mock_oic_client,
        mock_packages_response,
        mock_rate_limit_response,
        performance_oic_config,
        pytest_configure,
        sample_adapter_data,
        sample_certificate_data,
        sample_connection_data,
        sample_integration_data,
        sample_library_data,
        sample_lookup_data,
        sample_package_data,
        set_test_environment,
        singer_catalog,
        singer_state,
    )
    from tests.constants import (
        FlextTapOracleOicTestConstants,
        FlextTapOracleOicTestConstants as c,
    )
    from tests.models import (
        FlextTapOracleOicTestModels,
        FlextTapOracleOicTestModels as m,
    )
    from tests.protocols import (
        FlextTapOracleOicTestProtocols,
        FlextTapOracleOicTestProtocols as p,
    )
    from tests.test_auth import TestOICOAuth2Authenticator
    from tests.test_tap_core import (
        TestTapOracleOic,
        TestTapOracleOicIntegration,
        TestTapOracleOicWithFixtures,
        sample_config,
        sample_config_with_extended,
    )
    from tests.typings import (
        FlextTapOracleOicTestTypes,
        FlextTapOracleOicTestTypes as t,
    )
    from tests.utilities import (
        FlextTapOracleOicTestUtilities,
        FlextTapOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTapOracleOicTestConstants": [
        "tests.constants",
        "FlextTapOracleOicTestConstants",
    ],
    "FlextTapOracleOicTestModels": ["tests.models", "FlextTapOracleOicTestModels"],
    "FlextTapOracleOicTestProtocols": [
        "tests.protocols",
        "FlextTapOracleOicTestProtocols",
    ],
    "FlextTapOracleOicTestTypes": ["tests.typings", "FlextTapOracleOicTestTypes"],
    "FlextTapOracleOicTestUtilities": [
        "tests.utilities",
        "FlextTapOracleOicTestUtilities",
    ],
    "TestOICOAuth2Authenticator": ["tests.test_auth", "TestOICOAuth2Authenticator"],
    "TestTapOracleOic": ["tests.test_tap_core", "TestTapOracleOic"],
    "TestTapOracleOicIntegration": [
        "tests.test_tap_core",
        "TestTapOracleOicIntegration",
    ],
    "TestTapOracleOicWithFixtures": [
        "tests.test_tap_core",
        "TestTapOracleOicWithFixtures",
    ],
    "basic_oic_config": ["tests.conftest", "basic_oic_config"],
    "benchmark_config": ["tests.conftest", "benchmark_config"],
    "c": ["tests.constants", "FlextTapOracleOicTestConstants"],
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
    "p": ["tests.protocols", "FlextTapOracleOicTestProtocols"],
    "performance_oic_config": ["tests.conftest", "performance_oic_config"],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_adapter_data": ["tests.conftest", "sample_adapter_data"],
    "sample_certificate_data": ["tests.conftest", "sample_certificate_data"],
    "sample_config": ["tests.test_tap_core", "sample_config"],
    "sample_config_with_extended": [
        "tests.test_tap_core",
        "sample_config_with_extended",
    ],
    "sample_connection_data": ["tests.conftest", "sample_connection_data"],
    "sample_integration_data": ["tests.conftest", "sample_integration_data"],
    "sample_library_data": ["tests.conftest", "sample_library_data"],
    "sample_lookup_data": ["tests.conftest", "sample_lookup_data"],
    "sample_package_data": ["tests.conftest", "sample_package_data"],
    "set_test_environment": ["tests.conftest", "set_test_environment"],
    "singer_catalog": ["tests.conftest", "singer_catalog"],
    "singer_state": ["tests.conftest", "singer_state"],
    "t": ["tests.typings", "FlextTapOracleOicTestTypes"],
    "u": ["tests.utilities", "FlextTapOracleOicTestUtilities"],
    "x": ["flext_tests", "x"],
}

__all__ = [
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
    "p",
    "performance_oic_config",
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
    "u",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
