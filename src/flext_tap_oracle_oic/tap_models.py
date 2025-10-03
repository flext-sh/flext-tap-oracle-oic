"""Oracle Integration Cloud data models - PEP8 reorganized.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextTypes
from flext_tap_oracle_oic.domain.entities import OICIntegration

"""Oracle Integration Cloud data models - PEP8 reorganized.

This module consolidates ALL model and entity definitions:
- OIC Integration entities and domain models using flext-core patterns
- Stream configuration classes with type safety
- Response and request models for Oracle OIC APIs
- Value objects following DDD patterns with flext-core integration

Design: Pure domain modeling using:
- flext-core: "FlextModels", FlextModels patterns
- pydantic: Validation and serialization
- typing: Complete type safety and documentation
- Domain-driven design: Rich domain models with behavior

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""
"""

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


# Export for backward compatibility and module interface
__all__: FlextTypes.StringList = [
    "OICIntegration",
]
