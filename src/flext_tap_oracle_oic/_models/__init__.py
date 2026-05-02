# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        "._activity": ("OicActivityRecord",),
        "._agent": ("OicAgentEntity",),
        "._api_response": ("OicApiResponse",),
        "._auth_config": ("OicAuthenticationConfig",),
        "._connection": ("OicConnectionEntity",),
        "._envelope": ("OicEnvelope",),
        "._error_context": ("OicErrorContext",),
        "._helpers": (
            "require_entity_value",
            "validate_entity_identity_and_port",
            "validate_optional_port",
        ),
        "._integration": ("OicIntegrationEntity",),
        "._metrics": ("OicMetricsRecord",),
        "._oic_connection": ("OICConnection",),
        "._oic_execution_summary": ("OICExecutionSummary",),
        "._oic_integration": ("OICIntegration",),
        "._oic_lookup": ("OICLookup",),
        "._oic_monitoring": ("OICMonitoringRecord",),
        "._oic_project": ("OICProject",),
        "._oic_resource_metadata": ("OICResourceMetadata",),
        "._package": ("OicPackageEntity",),
        "._stream_config": ("OicStreamConfiguration",),
        ".streams": (
            "ALL_STREAMS",
            "FlextTapOracleOicModelsStreams",
            "th",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
