# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

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
    from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants, c
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
    from flext_tap_oracle_oic.models import FlextTapOracleOicModels, m
    from flext_tap_oracle_oic.protocols import FlextTapOracleOicProtocols, p
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
    from flext_tap_oracle_oic.typings import FlextTapOracleOicTypes, t
    from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities, u

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "ALL_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "ALL_STREAMS"),
    "AdaptersStream": ("flext_tap_oracle_oic.streams_consolidated", "AdaptersStream"),
    "CORE_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "CORE_STREAMS"),
    "CertificatesStream": ("flext_tap_oracle_oic.streams_consolidated", "CertificatesStream"),
    "ConnectionStatus": ("flext_tap_oracle_oic.domain.entities", "ConnectionStatus"),
    "ConnectionsStream": ("flext_tap_oracle_oic.streams_consolidated", "ConnectionsStream"),
    "EXTENDED_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "EXTENDED_STREAMS"),
    "ExecutionsStream": ("flext_tap_oracle_oic.streams_consolidated", "ExecutionsStream"),
    "FlextOracleOicAuthenticator": ("flext_tap_oracle_oic.tap_client", "FlextOracleOicAuthenticator"),
    "FlextTapOracleOicConstants": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
    "FlextTapOracleOicModels": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
    "FlextTapOracleOicProtocols": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
    "FlextTapOracleOicSettings": ("flext_tap_oracle_oic.settings", "FlextTapOracleOicSettings"),
    "FlextTapOracleOicTypes": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
    "FlextTapOracleOicUtilities": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
    "INFRASTRUCTURE_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "INFRASTRUCTURE_STREAMS"),
    "IntegrationStatus": ("flext_tap_oracle_oic.domain.entities", "IntegrationStatus"),
    "IntegrationsStream": ("flext_tap_oracle_oic.streams_consolidated", "IntegrationsStream"),
    "LibrariesStream": ("flext_tap_oracle_oic.streams_consolidated", "LibrariesStream"),
    "LookupsStream": ("flext_tap_oracle_oic.streams_consolidated", "LookupsStream"),
    "MONITORING_STREAMS": ("flext_tap_oracle_oic.streams_consolidated", "MONITORING_STREAMS"),
    "MetricsStream": ("flext_tap_oracle_oic.streams_consolidated", "MetricsStream"),
    "OICAPIError": ("flext_tap_oracle_oic.tap_exceptions", "OICAPIError"),
    "OICAuthenticationError": ("flext_tap_oracle_oic.tap_exceptions", "OICAuthenticationError"),
    "OICBaseStream": ("flext_tap_oracle_oic.tap_streams", "OICBaseStream"),
    "OICConnection": ("flext_tap_oracle_oic.domain.entities", "OICConnection"),
    "OICConnectionError": ("flext_tap_oracle_oic.tap_exceptions", "OICConnectionError"),
    "OICExceptionFactory": ("flext_tap_oracle_oic.tap_exceptions", "OICExceptionFactory"),
    "OICExecutionSummary": ("flext_tap_oracle_oic.domain.entities", "OICExecutionSummary"),
    "OICHealthChecker": ("flext_tap_oracle_oic.health", "OICHealthChecker"),
    "OICIntegration": ("flext_tap_oracle_oic.domain.entities", "OICIntegration"),
    "OICLookup": ("flext_tap_oracle_oic.domain.entities", "OICLookup"),
    "OICMonitoringRecord": ("flext_tap_oracle_oic.domain.entities", "OICMonitoringRecord"),
    "OICPaginator": ("flext_tap_oracle_oic.tap_streams", "OICPaginator"),
    "OICProject": ("flext_tap_oracle_oic.domain.entities", "OICProject"),
    "OICResourceMetadata": ("flext_tap_oracle_oic.domain.entities", "OICResourceMetadata"),
    "OICResourceType": ("flext_tap_oracle_oic.domain.entities", "OICResourceType"),
    "OICValidationError": ("flext_tap_oracle_oic.tap_exceptions", "OICValidationError"),
    "OracleOicClient": ("flext_tap_oracle_oic.tap_client", "OracleOicClient"),
    "PackagesStream": ("flext_tap_oracle_oic.streams_consolidated", "PackagesStream"),
    "ProjectsStream": ("flext_tap_oracle_oic.streams_consolidated", "ProjectsStream"),
    "TapOracleOic": ("flext_tap_oracle_oic.tap_client", "TapOracleOic"),
    "__all__": ("flext_tap_oracle_oic.__version__", "__all__"),
    "__author__": ("flext_tap_oracle_oic.__version__", "__author__"),
    "__author_email__": ("flext_tap_oracle_oic.__version__", "__author_email__"),
    "__description__": ("flext_tap_oracle_oic.__version__", "__description__"),
    "__license__": ("flext_tap_oracle_oic.__version__", "__license__"),
    "__title__": ("flext_tap_oracle_oic.__version__", "__title__"),
    "__url__": ("flext_tap_oracle_oic.__version__", "__url__"),
    "__version__": ("flext_tap_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_tap_oracle_oic.__version__", "__version_info__"),
    "c": ("flext_tap_oracle_oic.constants", "c"),
    "create_oracle_oic_tap_config": ("flext_tap_oracle_oic.settings", "create_oracle_oic_tap_config"),
    "logger": ("flext_tap_oracle_oic.tap_client", "logger"),
    "m": ("flext_tap_oracle_oic.models", "m"),
    "main": ("flext_tap_oracle_oic.tap_client", "main"),
    "p": ("flext_tap_oracle_oic.protocols", "p"),
    "t": ("flext_tap_oracle_oic.typings", "t"),
    "th": ("flext_tap_oracle_oic.streams_consolidated", "th"),
    "u": ("flext_tap_oracle_oic.utilities", "u"),
    "validate_oracle_oic_tap_configuration": ("flext_tap_oracle_oic.settings", "validate_oracle_oic_tap_configuration"),
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
    "OracleOicClient",
    "PackagesStream",
    "ProjectsStream",
    "TapOracleOic",
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
    "logger",
    "m",
    "main",
    "p",
    "t",
    "th",
    "u",
    "validate_oracle_oic_tap_configuration",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
