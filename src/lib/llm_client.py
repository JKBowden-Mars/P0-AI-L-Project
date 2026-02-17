# src/lib/llm_client.py

from src.types.schema import OpsTriageResult
from src.fixtures import FIXTURES


def analyze_ops_request(text: str) -> OpsTriageResult:
    """
    Mock LLM adapter.

    Today: returns a fixture based on simple keyword routing.
    Later: replace internals with a real model API call.
    """
    t = text.lower()

    # Simple routing rules (good enough for Day 3)
    if any(k in t for k in ["access", "permission", "can't get into", "cant get into", "grant me", "give me access"]):
        return FIXTURES["access_blocker_leadership"]

    if any(k in t for k in ["deadline", "two days ago", "overdue", "was due", "yesterday"]):
        return FIXTURES["missed_deadline_accountability"]

    if any(k in t for k in ["release", "deployed", "old behavior", "support", "product says"]):
        return FIXTURES["conflicting_release_reports"]

    if any(k in t for k in ["night shift", "hasn't posted", "hasnt posted", "no one's complained", "no ones complained"]):
        return FIXTURES["silent_night_shift_risk"]

    # Default fallback (pick the most conservative / low-risk fixture)
    return FIXTURES["silent_night_shift_risk"]
