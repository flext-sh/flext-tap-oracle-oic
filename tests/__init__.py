# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
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
        pytest_plugins,
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

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextTapOracleOicTestConstants,
        FlextTapOracleOicTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        FlextTapOracleOicTestModels,
        FlextTapOracleOicTestModels as m,
    )

    protocols = _tests_protocols
    import tests.test_auth as _tests_test_auth
    from tests.protocols import (
        FlextTapOracleOicTestProtocols,
        FlextTapOracleOicTestProtocols as p,
    )

    test_auth = _tests_test_auth
    import tests.test_tap as _tests_test_tap
    from tests.test_auth import TestOICOAuth2Authenticator

    test_tap = _tests_test_tap
    import tests.test_tap_core as _tests_test_tap_core

    test_tap_core = _tests_test_tap_core
    import tests.typings as _tests_typings
    from tests.test_tap_core import (
        TestTapOracleOic,
        TestTapOracleOicIntegration,
        TestTapOracleOicWithFixtures,
        sample_config,
        sample_config_with_extended,
    )

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import (
        FlextTapOracleOicTestTypes,
        FlextTapOracleOicTestTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextTapOracleOicTestUtilities,
        FlextTapOracleOicTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "FlextTapOracleOicTestConstants": (
        "tests.constants",
        "FlextTapOracleOicTestConstants",
    ),
    "FlextTapOracleOicTestModels": ("tests.models", "FlextTapOracleOicTestModels"),
    "FlextTapOracleOicTestProtocols": (
        "tests.protocols",
        "FlextTapOracleOicTestProtocols",
    ),
    "FlextTapOracleOicTestTypes": ("tests.typings", "FlextTapOracleOicTestTypes"),
    "FlextTapOracleOicTestUtilities": (
        "tests.utilities",
        "FlextTapOracleOicTestUtilities",
    ),
    "TestOICOAuth2Authenticator": ("tests.test_auth", "TestOICOAuth2Authenticator"),
    "TestTapOracleOic": ("tests.test_tap_core", "TestTapOracleOic"),
    "TestTapOracleOicIntegration": (
        "tests.test_tap_core",
        "TestTapOracleOicIntegration",
    ),
    "TestTapOracleOicWithFixtures": (
        "tests.test_tap_core",
        "TestTapOracleOicWithFixtures",
    ),
    "basic_oic_config": ("tests.conftest", "basic_oic_config"),
    "benchmark_config": ("tests.conftest", "benchmark_config"),
    "c": ("tests.constants", "FlextTapOracleOicTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "extended_oic_config": ("tests.conftest", "extended_oic_config"),
    "filtered_oic_config": ("tests.conftest", "filtered_oic_config"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "large_integration_dataset": ("tests.conftest", "large_integration_dataset"),
    "m": ("tests.models", "FlextTapOracleOicTestModels"),
    "mock_connections_response": ("tests.conftest", "mock_connections_response"),
    "mock_http_error_response": ("tests.conftest", "mock_http_error_response"),
    "mock_integrations_response": ("tests.conftest", "mock_integrations_response"),
    "mock_lookups_response": ("tests.conftest", "mock_lookups_response"),
    "mock_oauth_authenticator": ("tests.conftest", "mock_oauth_authenticator"),
    "mock_oauth_token_response": ("tests.conftest", "mock_oauth_token_response"),
    "mock_oic_client": ("tests.conftest", "mock_oic_client"),
    "mock_packages_response": ("tests.conftest", "mock_packages_response"),
    "mock_rate_limit_response": ("tests.conftest", "mock_rate_limit_response"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTapOracleOicTestProtocols"),
    "performance_oic_config": ("tests.conftest", "performance_oic_config"),
    "protocols": "tests.protocols",
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "sample_adapter_data": ("tests.conftest", "sample_adapter_data"),
    "sample_certificate_data": ("tests.conftest", "sample_certificate_data"),
    "sample_config": ("tests.test_tap_core", "sample_config"),
    "sample_config_with_extended": (
        "tests.test_tap_core",
        "sample_config_with_extended",
    ),
    "sample_connection_data": ("tests.conftest", "sample_connection_data"),
    "sample_integration_data": ("tests.conftest", "sample_integration_data"),
    "sample_library_data": ("tests.conftest", "sample_library_data"),
    "sample_lookup_data": ("tests.conftest", "sample_lookup_data"),
    "sample_package_data": ("tests.conftest", "sample_package_data"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "singer_catalog": ("tests.conftest", "singer_catalog"),
    "singer_state": ("tests.conftest", "singer_state"),
    "t": ("tests.typings", "FlextTapOracleOicTestTypes"),
    "test_auth": "tests.test_auth",
    "test_tap": "tests.test_tap",
    "test_tap_core": "tests.test_tap_core",
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTapOracleOicTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
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
    "pytest_plugins",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
