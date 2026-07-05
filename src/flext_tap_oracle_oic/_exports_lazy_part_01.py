# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_TAP_ORACLE_OIC_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._models": ("_models",),
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
        ".typings": (
            "FlextTapOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextTapOracleOicUtilities",
            "u",
        ),
        "flext_core._root_typing_parts": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)

__all__: list[str] = ["FLEXT_TAP_ORACLE_OIC_LAZY_IMPORTS_PART_01"]
