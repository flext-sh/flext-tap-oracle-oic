"""Base models for flext-tap-oracle-oic private family.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import m, u
from typing_extensions import TypeForm

from flext_tap_oracle_oic import p, t


class FlextTapOracleOicModelsBase:
    """Base models for the flext-tap-oracle-oic _models family."""

    class ConfigNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain."""

        model_config = m.ConfigDict(extra="allow", frozen=True)

    class StreamBase(m.BaseModel):
        """Base stream model for Oracle Integration Cloud APIs.

        Carries the Singer stream contract shared by every OIC stream:
        incremental replication identity, the JSON schema mapping, and the
        audit-trail properties spread into each concrete stream schema.

        """

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            arbitrary_types_allowed=True, extra="forbid"
        )

        settings: Annotated[
            t.JsonMapping,
            m.Field(
                description="Runtime stream settings passed by the tap",
            ),
        ] = m.Field(
            default_factory=u.empty(TypeForm(t.JsonMapping)),
            validate_default=True,
        )
        name: Annotated[
            str,
            m.Field(description="Canonical Singer stream name"),
        ] = ""
        replication_key: Annotated[
            str | None,
            m.Field(description="Incremental replication key field"),
        ] = None
        stream_schema: Annotated[
            t.JsonMapping,
            m.Field(
                description="Singer JSON schema mapping for the stream",
            ),
        ] = m.Field(
            default_factory=u.empty(TypeForm(t.JsonMapping)),
            validate_default=True,
        )
        requires_design_api: ClassVar[bool] = False
        requires_runtime_api: ClassVar[bool] = False
        api_path: ClassVar[str | None] = None
        api_category: ClassVar[str] = "core"
        default_sort: ClassVar[str | None] = None
        primary_keys: ClassVar[t.StrSequence] = []
        # Audit-trail properties carried by every OIC stream schema; declared
        # once here and spread into each stream's SingerPropertiesList.
        oic_common_properties: ClassVar[tuple[p.TapOracleOic.SingerProperty, ...]] = (
            m.Meltano.SingerProperty(
                "created",
                m.Meltano.SingerDateTimeType(),
                description="Creation timestamp",
            ),
            m.Meltano.SingerProperty(
                "lastUpdated",
                m.Meltano.SingerDateTimeType(),
                description="Last update timestamp",
            ),
            m.Meltano.SingerProperty(
                "createdBy",
                m.Meltano.SingerStringType(),
                description="Created by user",
            ),
            m.Meltano.SingerProperty(
                "lastUpdatedBy",
                m.Meltano.SingerStringType(),
                description="Last updated by user",
            ),
        )

        @staticmethod
        def schema_mapping(properties: p.TapOracleOic.SchemaSource) -> t.JsonMapping:
            """Dump one Singer property list into the typed stream schema contract.

            Args:
                properties: The constructed Singer SDK property list to dump.

            Returns:
                The stream schema mapping produced by the property list.

            """
            return properties.to_dict()


__all__: list[str] = ["FlextTapOracleOicModelsBase"]
