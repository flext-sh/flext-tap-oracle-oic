# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_tap_oracle_oic import domain
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
    from flext_tap_oracle_oic.health import OICHealthChecker
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
        OicEnvelope,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
        TapOracleOicPrivate,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings,
        create_oracle_oic_tap_config,
        validate_oracle_oic_tap_configuration,
    )
    from flext_tap_oracle_oic.streams_consolidated import (
        ALL_STREAMS,
        CORE_STREAMS,
        EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS,
        AdaptersStream,
        CertificatesStream,
        ConnectionsStream,
        ExecutionsStream,
        IntegrationsStream,
        LibrariesStream,
        LookupsStream,
        MetricsStream,
        PackagesStream,
        ProjectsStream,
        th,
    )
    from flext_tap_oracle_oic.tap_client import (
        FlextOracleOicAuthenticator,
        OracleOicClient,
        TapOracleOic,
        logger,
        main,
    )
    from flext_tap_oracle_oic.tap_exceptions import (
        OICAPIError,
        OICAuthenticationError,
        OICConnectionError,
        OICExceptionFactory,
        OICValidationError,
    )
    from flext_tap_oracle_oic.tap_streams import OICBaseStream, OICPaginator
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "ALL_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "ALL_STREAMS"),
    "AdaptersStream": ("flext_tap_oracle_oic.streams_consolidated", "AdaptersStream"),
    "CORE_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "CORE_STREAMS"),
    "CertificatesStream": (
        "flext_tap_oracle_oic.streams_consolidated",
        "CertificatesStream",
    ),
    "ConnectionStatus": ("flext_tap_oracle_oic.domain.entities", "ConnectionStatus"),
    "ConnectionsStream": (
        "flext_tap_oracle_oic.streams_consolidated",
        "ConnectionsStream",
    ),
    "EXTENDED_STREAMS": (
        "flext_tap_oracle_oic.streams_consolidated",
        "EXTENDED_STREAMS",
    ),
    "ExecutionsStream": (
        "flext_tap_oracle_oic.streams_consolidated",
        "ExecutionsStream",
    ),
    "FlextOracleOicAuthenticator": (
        "flext_tap_oracle_oic.tap_client",
        "FlextOracleOicAuthenticator",
    ),
    "FlextTapOracleOicConstants": (
        "flext_tap_oracle_oic.constants",
        "FlextTapOracleOicConstants",
    ),
    "FlextTapOracleOicModels": (
        "flext_tap_oracle_oic.models",
        "FlextTapOracleOicModels",
    ),
    "FlextTapOracleOicProtocols": (
        "flext_tap_oracle_oic.protocols",
        "FlextTapOracleOicProtocols",
    ),
    "FlextTapOracleOicSettings": (
        "flext_tap_oracle_oic.settings",
        "FlextTapOracleOicSettings",
    ),
    "FlextTapOracleOicTypes": (
        "flext_tap_oracle_oic.typings",
        "FlextTapOracleOicTypes",
    ),
    "FlextTapOracleOicUtilities": (
        "flext_tap_oracle_oic.utilities",
        "FlextTapOracleOicUtilities",
    ),
    "INFRASTRUCTURE_STREAMS": (
        "flext_tap_oracle_oic.streams_consolidated",
        "INFRASTRUCTURE_STREAMS",
    ),
    "IntegrationStatus": ("flext_tap_oracle_oic.domain.entities", "IntegrationStatus"),
    "IntegrationsStream": (
        "flext_tap_oracle_oic.streams_consolidated",
        "IntegrationsStream",
    ),
    "LibrariesStream": ("flext_tap_oracle_oic.streams_consolidated", "LibrariesStream"),
    "LookupsStream": ("flext_tap_oracle_oic.streams_consolidated", "LookupsStream"),
    "MONITORING_STREAMS": (
        "flext_tap_oracle_oic.streams_consolidated",
        "MONITORING_STREAMS",
    ),
    "MetricsStream": ("flext_tap_oracle_oic.streams_consolidated", "MetricsStream"),
    "OICAPIError": ("flext_tap_oracle_oic.tap_exceptions", "OICAPIError"),
    "OICAuthenticationError": (
        "flext_tap_oracle_oic.tap_exceptions",
        "OICAuthenticationError",
    ),
    "OICBaseStream": ("flext_tap_oracle_oic.tap_streams", "OICBaseStream"),
    "OICConnection": ("flext_tap_oracle_oic.domain.entities", "OICConnection"),
    "OICConnectionError": ("flext_tap_oracle_oic.tap_exceptions", "OICConnectionError"),
    "OICExceptionFactory": (
        "flext_tap_oracle_oic.tap_exceptions",
        "OICExceptionFactory",
    ),
    "OICExecutionSummary": (
        "flext_tap_oracle_oic.domain.entities",
        "OICExecutionSummary",
    ),
    "OICHealthChecker": ("flext_tap_oracle_oic.health", "OICHealthChecker"),
    "OICIntegration": ("flext_tap_oracle_oic.domain.entities", "OICIntegration"),
    "OICLookup": ("flext_tap_oracle_oic.domain.entities", "OICLookup"),
    "OICMonitoringRecord": (
        "flext_tap_oracle_oic.domain.entities",
        "OICMonitoringRecord",
    ),
    "OICPaginator": ("flext_tap_oracle_oic.tap_streams", "OICPaginator"),
    "OICProject": ("flext_tap_oracle_oic.domain.entities", "OICProject"),
    "OICResourceMetadata": (
        "flext_tap_oracle_oic.domain.entities",
        "OICResourceMetadata",
    ),
    "OICResourceType": ("flext_tap_oracle_oic.domain.entities", "OICResourceType"),
    "OICValidationError": ("flext_tap_oracle_oic.tap_exceptions", "OICValidationError"),
    "OicEnvelope": ("flext_tap_oracle_oic.models", "OicEnvelope"),
    "OracleOicClient": ("flext_tap_oracle_oic.tap_client", "OracleOicClient"),
    "PackagesStream": ("flext_tap_oracle_oic.streams_consolidated", "PackagesStream"),
    "ProjectsStream": ("flext_tap_oracle_oic.streams_consolidated", "ProjectsStream"),
    "TapOracleOic": ("flext_tap_oracle_oic.tap_client", "TapOracleOic"),
    "TapOracleOicPrivate": ("flext_tap_oracle_oic.protocols", "TapOracleOicPrivate"),
    "__all__": ("flext_tap_oracle_oic.__version__", "__all__"),
    "__author__": ("flext_tap_oracle_oic.__version__", "__author__"),
    "__author_email__": ("flext_tap_oracle_oic.__version__", "__author_email__"),
    "__description__": ("flext_tap_oracle_oic.__version__", "__description__"),
    "__license__": ("flext_tap_oracle_oic.__version__", "__license__"),
    "__title__": ("flext_tap_oracle_oic.__version__", "__title__"),
    "__url__": ("flext_tap_oracle_oic.__version__", "__url__"),
    "__version__": ("flext_tap_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_tap_oracle_oic.__version__", "__version_info__"),
    "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
    "create_oracle_oic_tap_config": (
        "flext_tap_oracle_oic.settings",
        "create_oracle_oic_tap_config",
    ),
    "d": ("flext_meltano", "d"),
    "domain": ("flext_tap_oracle_oic.domain", ""),
    "e": ("flext_meltano", "e"),
    "h": ("flext_meltano", "h"),
    "logger": ("flext_tap_oracle_oic.tap_client", "logger"),
    "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
    "main": ("flext_tap_oracle_oic.tap_client", "main"),
    "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
    "r": ("flext_meltano", "r"),
    "s": ("flext_meltano", "s"),
    "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
    "th": ("flext_tap_oracle_oic.streams_consolidated", "th"),
    "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
    "validate_oracle_oic_tap_configuration": (
        "flext_tap_oracle_oic.settings",
        "validate_oracle_oic_tap_configuration",
    ),
    "x": ("flext_meltano", "x"),
}

__all__ = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
    "AdaptersStream",
    "CertificatesStream",
    "ConnectionStatus",
    "ConnectionsStream",
    "ExecutionsStream",
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "IntegrationStatus",
    "IntegrationsStream",
    "LibrariesStream",
    "LookupsStream",
    "MetricsStream",
    "OICAPIError",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnection",
    "OICConnectionError",
    "OICExceptionFactory",
    "OICExecutionSummary",
    "OICHealthChecker",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICPaginator",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
    "OICValidationError",
    "OicEnvelope",
    "OracleOicClient",
    "PackagesStream",
    "ProjectsStream",
    "TapOracleOic",
    "TapOracleOicPrivate",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "create_oracle_oic_tap_config",
    "d",
    "domain",
    "e",
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
    "validate_oracle_oic_tap_configuration",
    "x",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
