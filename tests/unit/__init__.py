# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_auth": ("TestOICOAuth2Authenticator",),
        ".test_tap": ("TestTapOracleOic",),
        ".test_tap_core": (
            "TestTapOracleOicCore",
            "TestTapOracleOicIntegration",
            "TestTapOracleOicWithFixtures",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
