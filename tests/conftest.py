"""Test configuration for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
from collections.abc import Generator

import pytest


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "DEBUG"
    os.environ["SINGER_SDK_LOG_LEVEL"] = "DEBUG"
    os.environ["OIC_TEST_MODE"] = "true"
    yield
    os.environ.pop("FLEXT_ENV", None)
    os.environ.pop("FLEXT_LOG_LEVEL", None)
    os.environ.pop("SINGER_SDK_LOG_LEVEL", None)
    os.environ.pop("OIC_TEST_MODE", None)
