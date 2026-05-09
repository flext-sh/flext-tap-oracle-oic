"""Test configuration for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Generator

import pytest

from tests import u


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    with u.Tests.env_vars_context({
        "FLEXT_ENV": "test",
        "FLEXT_LOG_LEVEL": "DEBUG",
        "SINGER_SDK_LOG_LEVEL": "DEBUG",
        "OIC_TEST_MODE": "true",
    }):
        yield
