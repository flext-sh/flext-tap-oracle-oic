"""Oracle Integration Cloud stream base model (leaf declarations).

Extracted from the models facade so ``_models`` consumers (the streams
namespace and the facade) share one owner without a facade import cycle.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import FlextMeltanoModels, u
from typing_extensions import TypeForm

from flext_tap_oracle_oic import p, t


class FlextTapOracleOicStreamBase(FlextMeltanoModels.BaseModel):
    """Base stream model for Oracle Integration Cloud APIs.

    Carries the Singer stream contract shared by every OIC stream:
    incremental replication identity, the JSON schema mapping, and the
    audit-trail properties spread into each concrete stream schema.
    """

    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(arbitrary_types_allowed=True, extra="forbid")
    )

    settings: Annotated[
        t.JsonMapping,
        u.Field(
            default_factory=u.empty(TypeForm(t.JsonMapping)),
            description="Runtime stream settings passed by the tap",
        ),
    ]
    name: Annotated[
        str,
        u.Field(default="", description="Canonical Singer stream name"),
    ]
    replication_key: Annotated[
        str | None,
        u.Field(default=None, description="Incremental replication key field"),
    ]
    stream_schema: Annotated[
        t.JsonMapping,
        u.Field(
            default_factory=u.empty(TypeForm(t.JsonMapping)),
            description="Singer JSON schema mapping for the stream",
        ),
    ]
    logger: p.Logger = u.Field(
        default_factory=lambda: u.fetch_logger(__name__),
        description="Stream logger",
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
        FlextMeltanoModels.Meltano.SingerProperty(
            "created",
            FlextMeltanoModels.Meltano.SingerDateTimeType(),
            description="Creation timestamp",
        ),
        FlextMeltanoModels.Meltano.SingerProperty(
            "lastUpdated",
            FlextMeltanoModels.Meltano.SingerDateTimeType(),
            description="Last update timestamp",
        ),
        FlextMeltanoModels.Meltano.SingerProperty(
            "createdBy",
            FlextMeltanoModels.Meltano.SingerStringType(),
            description="Created by user",
        ),
        FlextMeltanoModels.Meltano.SingerProperty(
            "lastUpdatedBy",
            FlextMeltanoModels.Meltano.SingerStringType(),
            description="Last updated by user",
        ),
    )

    @staticmethod
    def schema_mapping(properties: p.TapOracleOic.SchemaSource) -> t.JsonMapping:
        """Dump one Singer property list into the typed stream schema contract.

        Args:
            properties: The constructed Singer SDK property list to dump.

        Returns:
            The resulting ``t.JsonMapping``.
        """
        return properties.to_dict()


__all__: list[str] = ["FlextTapOracleOicStreamBase"]
