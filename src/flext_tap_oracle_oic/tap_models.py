"""Oracle Integration Cloud data models - PEP8 reorganized.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_tap_oracle_oic import t
from flext_tap_oracle_oic.models import FlextTapOracleOicModels as _Models

OICIntegration = _Models.OracleOic.OICIntegration

'Oracle Integration Cloud data models - PEP8 reorganized.\n\nThis module consolidates ALL model and entity definitions:\n- OIC Integration entities and domain models using flext-core patterns\n- Stream configuration classes with type safety\n- Response and request models for Oracle OIC APIs\n- Value objects following DDD patterns with flext-core integration\n\nDesign: Pure domain modeling using:\n- flext-core: "FlextModels", FlextModels patterns\n- pydantic: Validation and serialization\n- typing: Complete type safety and documentation\n- Domain-driven design: Rich domain models with behavior\n\nCopyright (c) 2025 FLEXT Team. All rights reserved.\nSPDX-License-Identifier: MIT\n\n'
"\n\nCopyright (c) 2025 FLEXT Team. All rights reserved.\nSPDX-License-Identifier: MIT\n\n"
__all__: t.StrSequence = ["OICIntegration"]
