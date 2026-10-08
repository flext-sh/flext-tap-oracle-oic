"""Oracle Integration Cloud tap implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar, override

from flext_meltano.services.abstractions import FlextMeltanoAbstractions

from flext_tap_oracle_oic import (
    FlextTapOracleOicAuthenticator,
    FlextTapOracleOicClient,
    FlextTapOracleOicSettings,
    c,
    m,
    p,
    r,
    t,
    u,
)
from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams

logger = u.fetch_logger(__name__)


class FlextTapOracleOic(FlextMeltanoAbstractions):
    """Oracle Integration Cloud tap implementation using flext-oracle-oic."""

    name: ClassVar[str] = "tap-oracle-oic"
    capabilities: ClassVar[t.StrSequence] = ["catalog", "state", "discover"]
    config_jsonschema: ClassVar[t.JsonMapping] = {
        "type": "object",
        "properties": {
            "oauth_client_id": {"type": "string", "description": "OAuth2 client ID"},
            "oauth_client_secret": {
                "type": "string",
                "description": "OAuth2 client secret",
                # Singer JSON-schema secret marker, not a credential;
                # operator-authorized false positive 2026-09-23 (bead flext-tdtyq).
                "secret": True,  # nosec B105
            },
            "oauth_token_url": {"type": "string", "description": "OAuth2 token URL"},
            "oic_url": {"type": "string", "description": "OIC instance URL"},
            "oauth_scope": {"type": ["string", "null"], "description": "OAuth2 scope"},
            "include_infrastructure": {
                "type": ["boolean", "null"],
                "description": "Include infrastructure streams",
            },
        },
        "required": [
            "oauth_client_id",
            "oauth_client_secret",
            "oauth_token_url",
            "oic_url",
        ],
    }

    def __init__(
        self,
        *,
        settings: t.JsonMapping | None = None,
        validate_config: bool = True,
    ) -> None:
        """Initialize Oracle OIC tap with library composition."""
        super().__init__()
        self._tap_config = t.json_dict_adapter().validate_python(settings or {})
        # NOTE (multi-agent): flat Singer config maps into the namespaced
        # settings SSOT (settings.TapOracleOic.*, ADR-005); unknown keys ignored.
        self._oic_settings = FlextTapOracleOicSettings.model_validate(
            {"TapOracleOic": self._tap_config},
            strict=validate_config,
        )
        self._client: FlextTapOracleOicClient | None = None

    @property
    def oic_settings(self) -> FlextTapOracleOicSettings:
        """The typed OIC settings."""
        return self._oic_settings

    @property
    def client(self) -> FlextTapOracleOicClient:
        """Oracle OIC client instance using flext-oracle-oic."""
        if self._client is None:
            config_dict = self._tap_config
            oic_config_data: t.JsonMapping = {
                "oauth_client_id": str(config_dict["oauth_client_id"]),
                "oauth_client_secret": str(config_dict["oauth_client_secret"]),
                "oauth_token_url": str(config_dict["oauth_token_url"]),
                "oauth_audience": str(
                    config_dict.get("oauth_scope", "urn:opc:resource:consumer:all"),
                ),
                "base_url": str(config_dict["oic_url"]),
                "timeout": u.to_positive_int(
                    config_dict.get("request_timeout"),
                    default=30,
                ),
                "max_retries": u.to_positive_int(
                    config_dict.get("max_retries"),
                    default=3,
                ),
            }
            oic_config = FlextTapOracleOicSettings.model_validate({
                "TapOracleOic": oic_config_data,
            })
            authenticator = FlextTapOracleOicAuthenticator(settings=oic_config)
            self._client = FlextTapOracleOicClient(
                settings=oic_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_oic_streams(self) -> t.SequenceOf[m.TapOracleOic.OICBaseStream]:
        """Discover OIC stream class instances for this tap.

        Returns:
            The resulting ``t.SequenceOf[m.TapOracleOic.OICBaseStream]``.
        """
        logger.info("Discovering Oracle OIC streams using consolidated streams")
        stream_names = list(c.TapOracleOic.CORE_STREAMS)
        if self._tap_config.get("include_infrastructure", False):
            stream_names.extend(c.TapOracleOic.INFRASTRUCTURE_STREAMS)
        # The registry derives from the declaring namespace: every stream class
        # owns its ``name`` default, so no hand-maintained name→class table exists.
        registry = {
            member.model_fields["name"].default: member
            for member in vars(FlextTapOracleOicModelsStreams).values()
            if isinstance(member, type)
            and issubclass(member, m.TapOracleOic.OICBaseStream)
        }
        streams = [
            registry[stream_name].model_validate({"settings": self._tap_config})
            for stream_name in stream_names
            if stream_name in registry
        ]
        logger.info("Discovered %s streams from Oracle OIC", len(streams))
        return streams

    @override
    def discover_streams(
        self,
        tap_instance: m.Meltano.TapInstance,
    ) -> p.Result[t.JsonMapping]:
        """Discover stream catalog matching FlextMeltanoAbstractions contract.

        Returns:
            The resulting ``p.Result[t.JsonMapping]``.
        """
        _ = tap_instance
        streams = self.discover_oic_streams()
        catalog_entries: list[m.Meltano.SingerCatalogEntry] = []
        for stream in streams:
            stream_name = str(getattr(stream, "name", c.IDENTIFIER_UNKNOWN))
            stream_schema_raw: p.AttributeProbe = getattr(stream, "stream_schema", {})
            stream_schema: t.JsonMapping = (
                t.json_mapping_adapter().validate_python(stream_schema_raw)
                if isinstance(stream_schema_raw, Mapping)
                else {}
            )
            entry_result = u.Meltano.build_catalog_entry(
                stream_name=stream_name,
                schema=stream_schema,
                key_properties=(),
                replication_key=(
                    str(replication_key)
                    if (replication_key := getattr(stream, "replication_key", None))
                    is not None
                    else None
                ),
            )
            if entry_result.failure:
                return r[t.JsonMapping].from_failure(entry_result)
            catalog_entries.append(entry_result.value)
        catalog: t.JsonMapping = t.json_mapping_adapter().validate_python(
            m.Meltano.SingerCatalog(streams=catalog_entries).model_dump(
                by_alias=True,
                exclude_defaults=True,
                exclude_none=True,
                mode="json",
            ),
        )
        return r[t.JsonMapping].ok(
            t.json_mapping_adapter().validate_python({
                "streams": catalog.get("streams", []),
            }),
        )

    def test_connection(self) -> p.Result[bool]:
        """Test connection to Oracle OIC using real API client.

        Returns:
            The resulting ``p.Result[bool]``.
        """

        def _run_test_connection() -> p.Result[bool]:
            logger.info("Testing Oracle OIC connection")
            test_result = self.client.get("integrations")
            if test_result.success:
                logger.info("Oracle OIC connection test successful")
                return r[bool].ok(value=True)
            error_msg = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return r[bool].fail(error_msg)

        try:
            return _run_test_connection()
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            exception_msg = f"Oracle OIC connection test exception: {e}"
            logger.exception(exception_msg)
            return r[bool].fail(exception_msg)


__all__: list[str] = ["FlextTapOracleOic"]
