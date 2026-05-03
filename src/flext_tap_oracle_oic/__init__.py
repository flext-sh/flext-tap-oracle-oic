# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x
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
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )
    from flext_tap_oracle_oic.api import FlextTapOracleOicService, tap_oracle_oic
    from flext_tap_oracle_oic.cli import FlextTapOracleOicCli, main
    from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants, c
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError,
        FlextTapOracleOicValidationError,
    )
    from flext_tap_oracle_oic.models import FlextTapOracleOicModels, m
    from flext_tap_oracle_oic.protocols import FlextTapOracleOicProtocols, p
    from flext_tap_oracle_oic.settings import FlextTapOracleOicSettings
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
    )
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator
    from flext_tap_oracle_oic.typings import FlextTapOracleOicTypes, t
    from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    ("._models",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "ALL_STREAMS",
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicModelsStreams",
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
    "th",
    "u",
    "x",
]
