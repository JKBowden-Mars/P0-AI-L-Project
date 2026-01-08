# src/examples/fixtures.py

from src.types.schema import OpsTriageResult


# Each fixture represents a "correct" system output
# keyed by a short, descriptive name.

FIXTURES: dict[str, OpsTriageResult] = {
    "access_blocker_leadership": {
        "category": "Access / Permissions",
        "priority": "P0",
        "suggested_team": "IT / Systems Operations",
        "summary": "User cannot access a required folder despite prior direction that access would be granted.",
        "recommended_action": "Verify and grant the appropriate folder permissions. Confirm whether any related access issues exist.",
        "confidence": 0.72,
        "explanation": "Leadership involvement and a missed access timeline indicate a critical blocker."
    },

    "missed_deadline_accountability": {
        "category": "Delivery / Accountability",
        "priority": "P1",
        "suggested_team": "Engineering / Web",
        "summary": "A scheduled fix missed its deadline and ownership of the task is unclear.",
        "recommended_action": "Identify the responsible owner and provide a status update. Determine if escalation is required.",
        "confidence": 0.68,
        "explanation": "The request references a missed deadline and leadership pressure but no confirmed outage."
    },

    "conflicting_release_reports": {
        "category": "Release / Verification",
        "priority": "P1",
        "suggested_team": "Engineering / Release Management",
        "summary": "Conflicting reports indicate uncertainty about whether a recent release was successfully deployed.",
        "recommended_action": "Verify the active release version and reconcile reports from product and support teams.",
        "confidence": 0.71,
        "explanation": "Contradictory information from different teams requires verification before further action."
    },

    "silent_night_shift_risk": {
        "category": "Monitoring / Risk",
        "priority": "P3",
        "suggested_team": "Operations",
        "summary": "Expected updates from the night shift have not been posted, though no issues have been reported.",
        "recommended_action": "Confirm whether the lack of updates is expected and continue monitoring.",
        "confidence": 0.55,
        "explanation": "The absence of reported impact suggests an early warning rather than an active incident."
    }
}
