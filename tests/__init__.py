# AUTO-GENERATED FILE — canonical lazy tests facade. Regenerate with: make gen
"""Test package facade exposing the project test aliases lazily."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from tests.base import (
        TestsFlextTapOracleOicServiceBase as TestsFlextTapOracleOicServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextTapOracleOicConstants as TestsFlextTapOracleOicConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextTapOracleOicModels as TestsFlextTapOracleOicModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextTapOracleOicProtocols as TestsFlextTapOracleOicProtocols,
        p,
    )
    from tests.typings import (
        TestsFlextTapOracleOicTypes as TestsFlextTapOracleOicTypes,
        t as t,
    )
    from tests.utilities import (
        TestsFlextTapOracleOicUtilities as TestsFlextTapOracleOicUtilities,
        u,
    )

_LAZY_IMPORTS = build_lazy_import_map({
    ".constants": ("TestsFlextTapOracleOicConstants", "c"),
    ".typings": ("TestsFlextTapOracleOicTypes", "t"),
    ".protocols": ("TestsFlextTapOracleOicProtocols", "p"),
    ".models": ("TestsFlextTapOracleOicModels", "m"),
    ".utilities": ("TestsFlextTapOracleOicUtilities", "u"),
    ".base": ("TestsFlextTapOracleOicServiceBase", "s"),
})

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
