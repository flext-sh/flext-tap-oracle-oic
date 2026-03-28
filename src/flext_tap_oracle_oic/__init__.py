# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_tap_oracle_oic import _models, domain
    from flext_tap_oracle_oic.__version__ import (
        __all__,
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
        CORE_STREAMS,
        EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )
    from flext_tap_oracle_oic.domain.entities import (
        ConnectionStatus,
        IntegrationStatus,
        OICConnection,
        OICExecutionSummary,
        OICIntegration,
        OICLookup,
        OICMonitoringRecord,
        OICProject,
        OICResourceMetadata,
        OICResourceType,
    )
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError,
        FlextTapOracleOicExceptionFactory,
        FlextTapOracleOicValidationError,
    )
    from flext_tap_oracle_oic.health import FlextTapOracleOicHealthChecker
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings,
        flext_tap_oracle_oic_create_config,
        validate_configuration,
    )
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
        logger,
        main,
    )
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "ALL_STREAMS": ["flext_tap_oracle_oic._models.streams", "ALL_STREAMS"],
    "CORE_STREAMS": ["flext_tap_oracle_oic._models.streams", "CORE_STREAMS"],
    "ConnectionStatus": ["flext_tap_oracle_oic.domain.entities", "ConnectionStatus"],
    "EXTENDED_STREAMS": ["flext_tap_oracle_oic._models.streams", "EXTENDED_STREAMS"],
    "FlextOracleOicAuthenticator": [
        "flext_tap_oracle_oic.tap",
        "FlextOracleOicAuthenticator",
    ],
    "FlextTapOracleOic": ["flext_tap_oracle_oic.tap", "FlextTapOracleOic"],
    "FlextTapOracleOicApiError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicApiError",
    ],
    "FlextTapOracleOicAuthenticationError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicAuthenticationError",
    ],
    "FlextTapOracleOicClient": ["flext_tap_oracle_oic.tap", "FlextTapOracleOicClient"],
    "FlextTapOracleOicConnectionError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicConnectionError",
    ],
    "FlextTapOracleOicConstants": [
        "flext_tap_oracle_oic.constants",
        "FlextTapOracleOicConstants",
    ],
    "FlextTapOracleOicExceptionFactory": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicExceptionFactory",
    ],
    "FlextTapOracleOicHealthChecker": [
        "flext_tap_oracle_oic.health",
        "FlextTapOracleOicHealthChecker",
    ],
    "FlextTapOracleOicModels": [
        "flext_tap_oracle_oic.models",
        "FlextTapOracleOicModels",
    ],
    "FlextTapOracleOicModelsStreams": [
        "flext_tap_oracle_oic._models.streams",
        "FlextTapOracleOicModelsStreams",
    ],
    "FlextTapOracleOicPaginator": [
        "flext_tap_oracle_oic.tap_streams",
        "FlextTapOracleOicPaginator",
    ],
    "FlextTapOracleOicProtocols": [
        "flext_tap_oracle_oic.protocols",
        "FlextTapOracleOicProtocols",
    ],
    "FlextTapOracleOicSettings": [
        "flext_tap_oracle_oic.settings",
        "FlextTapOracleOicSettings",
    ],
    "FlextTapOracleOicTypes": [
        "flext_tap_oracle_oic.typings",
        "FlextTapOracleOicTypes",
    ],
    "FlextTapOracleOicUtilities": [
        "flext_tap_oracle_oic.utilities",
        "FlextTapOracleOicUtilities",
    ],
    "FlextTapOracleOicValidationError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicValidationError",
    ],
    "INFRASTRUCTURE_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "INFRASTRUCTURE_STREAMS",
    ],
    "IntegrationStatus": ["flext_tap_oracle_oic.domain.entities", "IntegrationStatus"],
    "MONITORING_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "MONITORING_STREAMS",
    ],
    "OICConnection": ["flext_tap_oracle_oic.domain.entities", "OICConnection"],
    "OICExecutionSummary": [
        "flext_tap_oracle_oic.domain.entities",
        "OICExecutionSummary",
    ],
    "OICIntegration": ["flext_tap_oracle_oic.domain.entities", "OICIntegration"],
    "OICLookup": ["flext_tap_oracle_oic.domain.entities", "OICLookup"],
    "OICMonitoringRecord": [
        "flext_tap_oracle_oic.domain.entities",
        "OICMonitoringRecord",
    ],
    "OICProject": ["flext_tap_oracle_oic.domain.entities", "OICProject"],
    "OICResourceMetadata": [
        "flext_tap_oracle_oic.domain.entities",
        "OICResourceMetadata",
    ],
    "OICResourceType": ["flext_tap_oracle_oic.domain.entities", "OICResourceType"],
    "__all__": ["flext_tap_oracle_oic.__version__", "__all__"],
    "__author__": ["flext_tap_oracle_oic.__version__", "__author__"],
    "__author_email__": ["flext_tap_oracle_oic.__version__", "__author_email__"],
    "__description__": ["flext_tap_oracle_oic.__version__", "__description__"],
    "__license__": ["flext_tap_oracle_oic.__version__", "__license__"],
    "__title__": ["flext_tap_oracle_oic.__version__", "__title__"],
    "__url__": ["flext_tap_oracle_oic.__version__", "__url__"],
    "__version__": ["flext_tap_oracle_oic.__version__", "__version__"],
    "__version_info__": ["flext_tap_oracle_oic.__version__", "__version_info__"],
    "_models": ["flext_tap_oracle_oic._models", ""],
    "c": ["flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"],
    "d": ["flext_meltano", "d"],
    "domain": ["flext_tap_oracle_oic.domain", ""],
    "e": ["flext_meltano", "e"],
    "flext_tap_oracle_oic_create_config": [
        "flext_tap_oracle_oic.settings",
        "flext_tap_oracle_oic_create_config",
    ],
    "h": ["flext_meltano", "h"],
    "logger": ["flext_tap_oracle_oic.tap", "logger"],
    "m": ["flext_tap_oracle_oic.models", "FlextTapOracleOicModels"],
    "main": ["flext_tap_oracle_oic.tap", "main"],
    "p": ["flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "t": ["flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"],
    "th": ["flext_tap_oracle_oic._models.streams", "th"],
    "u": ["flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"],
    "validate_configuration": [
        "flext_tap_oracle_oic.settings",
        "validate_configuration",
    ],
    "x": ["flext_meltano", "x"],
}

__all__ = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
    "ConnectionStatus",
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicExceptionFactory",
    "FlextTapOracleOicHealthChecker",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicValidationError",
    "IntegrationStatus",
    "OICConnection",
    "OICExecutionSummary",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_models",
    "c",
    "d",
    "domain",
    "e",
    "flext_tap_oracle_oic_create_config",
    "h",
    "logger",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "th",
    "u",
    "validate_configuration",
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
