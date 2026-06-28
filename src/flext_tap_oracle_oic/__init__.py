# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_tap_oracle_oic.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _t.TYPE_CHECKING:
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS as ALL_STREAMS,
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
        th as th,
    )
    from flext_tap_oracle_oic.api import (
        FlextTapOracleOicService as FlextTapOracleOicService,
        tap_oracle_oic as tap_oracle_oic,
    )
    from flext_tap_oracle_oic.cli import (
        FlextTapOracleOicCli as FlextTapOracleOicCli,
        main as main,
    )
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants as FlextTapOracleOicConstants,
        c as c,
    )
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError as FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError as FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError as FlextTapOracleOicConnectionError,
        FlextTapOracleOicValidationError as FlextTapOracleOicValidationError,
    )
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels as FlextTapOracleOicModels,
        m as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols as FlextTapOracleOicProtocols,
        p as p,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings as FlextTapOracleOicSettings,
    )
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator as FlextOracleOicAuthenticator,
        FlextTapOracleOic as FlextTapOracleOic,
        FlextTapOracleOicClient as FlextTapOracleOicClient,
    )
    from flext_tap_oracle_oic.tap_streams import (
        FlextTapOracleOicPaginator as FlextTapOracleOicPaginator,
    )
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes as FlextTapOracleOicTypes,
        t as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities as FlextTapOracleOicUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("._models",),
    build_lazy_import_map(
        {
            "._models.streams": (
                "ALL_STREAMS",
                "FlextTapOracleOicModelsStreams",
                "th",
            ),
            ".api": (
                "FlextTapOracleOicService",
                "tap_oracle_oic",
            ),
            ".cli": (
                "FlextTapOracleOicCli",
                "main",
            ),
            ".constants": (
                "FlextTapOracleOicConstants",
                "c",
            ),
            ".errors": (
                "FlextTapOracleOicApiError",
                "FlextTapOracleOicAuthenticationError",
                "FlextTapOracleOicConnectionError",
                "FlextTapOracleOicValidationError",
            ),
            ".models": (
                "FlextTapOracleOicModels",
                "m",
            ),
            ".protocols": (
                "FlextTapOracleOicProtocols",
                "p",
            ),
            ".settings": ("FlextTapOracleOicSettings",),
            ".tap": (
                "FlextOracleOicAuthenticator",
                "FlextTapOracleOic",
                "FlextTapOracleOicClient",
            ),
            ".tap_streams": ("FlextTapOracleOicPaginator",),
            ".typings": (
                "FlextTapOracleOicTypes",
                "t",
            ),
            ".utilities": (
                "FlextTapOracleOicUtilities",
                "u",
            ),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)

__all__: list[str] = [
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicService",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicValidationError",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "tap_oracle_oic",
    "u",
    "x",
]
