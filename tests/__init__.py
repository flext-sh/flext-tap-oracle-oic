# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_tap_oracle_oic import (
        conftest,
        constants,
        models,
        protocols,
        test_auth,
        test_tap,
        test_tap_core,
        typings,
        utilities,
    )
    from flext_tap_oracle_oic.conftest import (
        basic_oic_config,
        benchmark_config,
        config,
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
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicTestConstants,
        FlextTapOracleOicTestConstants as c,
    )
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicTestModels,
        FlextTapOracleOicTestModels as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicTestProtocols,
        FlextTapOracleOicTestProtocols as p,
    )
    from flext_tap_oracle_oic.test_auth import TestOICOAuth2Authenticator
    from flext_tap_oracle_oic.test_tap_core import (
        sample_config,
        sample_config_with_extended,
    )
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTestTypes,
        FlextTapOracleOicTestTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicTestUtilities,
        FlextTapOracleOicTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTapOracleOicTestConstants": "flext_tap_oracle_oic.constants",
    "FlextTapOracleOicTestModels": "flext_tap_oracle_oic.models",
    "FlextTapOracleOicTestProtocols": "flext_tap_oracle_oic.protocols",
    "FlextTapOracleOicTestTypes": "flext_tap_oracle_oic.typings",
    "FlextTapOracleOicTestUtilities": "flext_tap_oracle_oic.utilities",
    "TestOICOAuth2Authenticator": "flext_tap_oracle_oic.test_auth",
    "basic_oic_config": "flext_tap_oracle_oic.conftest",
    "benchmark_config": "flext_tap_oracle_oic.conftest",
    "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicTestConstants"),
    "config": "flext_tap_oracle_oic.conftest",
    "conftest": "flext_tap_oracle_oic.conftest",
    "constants": "flext_tap_oracle_oic.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "extended_oic_config": "flext_tap_oracle_oic.conftest",
    "filtered_oic_config": "flext_tap_oracle_oic.conftest",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "large_integration_dataset": "flext_tap_oracle_oic.conftest",
    "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicTestModels"),
    "mock_connections_response": "flext_tap_oracle_oic.conftest",
    "mock_http_error_response": "flext_tap_oracle_oic.conftest",
    "mock_integrations_response": "flext_tap_oracle_oic.conftest",
    "mock_lookups_response": "flext_tap_oracle_oic.conftest",
    "mock_oauth_authenticator": "flext_tap_oracle_oic.conftest",
    "mock_oauth_token_response": "flext_tap_oracle_oic.conftest",
    "mock_oic_client": "flext_tap_oracle_oic.conftest",
    "mock_packages_response": "flext_tap_oracle_oic.conftest",
    "mock_rate_limit_response": "flext_tap_oracle_oic.conftest",
    "models": "flext_tap_oracle_oic.models",
    "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicTestProtocols"),
    "performance_oic_config": "flext_tap_oracle_oic.conftest",
    "protocols": "flext_tap_oracle_oic.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "sample_adapter_data": "flext_tap_oracle_oic.conftest",
    "sample_certificate_data": "flext_tap_oracle_oic.conftest",
    "sample_config": "flext_tap_oracle_oic.test_tap_core",
    "sample_config_with_extended": "flext_tap_oracle_oic.test_tap_core",
    "sample_connection_data": "flext_tap_oracle_oic.conftest",
    "sample_integration_data": "flext_tap_oracle_oic.conftest",
    "sample_library_data": "flext_tap_oracle_oic.conftest",
    "sample_lookup_data": "flext_tap_oracle_oic.conftest",
    "sample_package_data": "flext_tap_oracle_oic.conftest",
    "set_test_environment": "flext_tap_oracle_oic.conftest",
    "singer_catalog": "flext_tap_oracle_oic.conftest",
    "singer_state": "flext_tap_oracle_oic.conftest",
    "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTestTypes"),
    "test_auth": "flext_tap_oracle_oic.test_auth",
    "test_tap": "flext_tap_oracle_oic.test_tap",
    "test_tap_core": "flext_tap_oracle_oic.test_tap_core",
    "typings": "flext_tap_oracle_oic.typings",
    "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicTestUtilities"),
    "utilities": "flext_tap_oracle_oic.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
