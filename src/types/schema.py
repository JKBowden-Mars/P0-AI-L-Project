# src/types/schema.py

from typing import TypedDict, Literal


# ---- Allowed enums ----

Priority = Literal["P0", "P1", "P2", "P3"]


# ---- Core schema contract ----

class OpsTriageResult(TypedDict):
    category: str
    priority: Priority
    suggested_team: str
    summary: str
    recommended_action: str
    confidence: float
    explanation: str


# ---- Validation constants ----

REQUIRED_KEYS = {
    "category",
    "priority",
    "suggested_team",
    "summary",
    "recommended_action",
    "confidence",
    "explanation",
}

ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}

CONFIDENCE_MIN = 0.0
CONFIDENCE_MAX = 1.0
