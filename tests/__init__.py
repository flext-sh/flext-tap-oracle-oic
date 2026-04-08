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
    from tests.conftest import pytest_configure, pytest_plugins

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

    test_tap = _tests_test_tap
    import tests.test_tap_core as _tests_test_tap_core

    test_tap_core = _tests_test_tap_core
    import tests.typings as _tests_typings

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
    "c": ("tests.constants", "FlextTapOracleOicTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "FlextTapOracleOicTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTapOracleOicTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
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
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "pytest_configure",
    "pytest_plugins",
    "r",
    "s",
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
