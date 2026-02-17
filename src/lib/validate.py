# src/lib/validate.py

from typing import Any, cast
from src.types.schema import (
    OpsTriageResult,
    REQUIRED_KEYS,
    ALLOWED_PRIORITIES,
    CONFIDENCE_MIN,
    CONFIDENCE_MAX,
)


def validate_output(data: dict[str, Any]) -> OpsTriageResult:
    # Key presence
    missing = REQUIRED_KEYS - set(data.keys())
    if missing:
        raise ValueError(f"Missing keys: {sorted(missing)}")

    # Priority enum
    if data["priority"] not in ALLOWED_PRIORITIES:
        raise ValueError(f"Invalid priority: {data['priority']}")

    # Confidence bounds
    conf = float(data["confidence"])
    conf = max(CONFIDENCE_MIN, min(CONFIDENCE_MAX, conf))
    data["confidence"] = conf

    # Basic type sanity (lightweight)
    for k in ["category", "suggested_team", "summary", "recommended_action", "explanation"]:
        if not isinstance(data[k], str) or not data[k].strip():
            raise ValueError(f"Invalid value for '{k}'")

    return cast(OpsTriageResult, data)
