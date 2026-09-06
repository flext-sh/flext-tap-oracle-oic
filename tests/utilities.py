"""Module skeleton for TestsFlextTapOracleOicUtilities.

Test utilities for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_tap_oracle_oic import FlextTapOracleOicUtilities
from flext_tests import FlextTestsUtilities, tm

if TYPE_CHECKING:
    from flext_tap_oracle_oic import FlextTapOracleOic, m, t


class TestsFlextTapOracleOicUtilities(FlextTestsUtilities, FlextTapOracleOicUtilities):
    """Test utilities for flext-tap-oracle-oic."""

    class TapOracleOic(FlextTapOracleOicUtilities.TapOracleOic):
        """TapOracleOic test utilities namespace."""

        class Tests:
            """Typed helpers for public tap behavior."""

            @staticmethod
            def discover_stream_names(
                tap: FlextTapOracleOic, tap_instance: m.Meltano.TapInstance
            ) -> t.StrSequence:
                """Return stream identifiers from the public Singer catalog."""
                result = tap.discover_streams(tap_instance=tap_instance)
                tm.ok(result)
                catalog = result.unwrap()
                streams = catalog.get("streams")
                tm.that(streams, is_=Sequence)
                if not isinstance(streams, Sequence) or isinstance(
                    streams, (str, bytes)
                ):
                    msg = "public discovery catalog must expose a stream sequence"
                    raise TypeError(msg)
                names: list[str] = []
                for stream in streams:
                    tm.that(stream, is_=Mapping)
                    if not isinstance(stream, Mapping):
                        msg = "public discovery catalog entries must be mappings"
                        raise TypeError(msg)
                    stream_id = stream.get("tap_stream_id")
                    tm.that(stream_id, is_=str)
                    if not isinstance(stream_id, str):
                        msg = "public discovery catalog entries require tap_stream_id"
                        raise TypeError(msg)
                    names.append(stream_id)
                return tuple(names)


u = TestsFlextTapOracleOicUtilities
__all__: list[str] = ["TestsFlextTapOracleOicUtilities", "u"]
