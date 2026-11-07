
"""Persistent memory for storing lesson evaluation feedback."""

import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")


def load_memory():
    """Load previous memory or return an empty memory structure."""
    if not MEMORY_FILE.exists():
        return {
            "total_runs": 0,
            "failure_patterns": {},
            "feedback_history": []
        }

    try:
        with MEMORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {
            "total_runs": 0,
            "failure_patterns": {},
            "feedback_history": []
        }


def get_improvement_guidance(memory):
    """Create guidance from repeated evaluation failures."""
    patterns = memory.get("failure_patterns", {})

    repeated = [
        f"{name}: failed {count} times"
        for name, count in patterns.items()
        if count >= 2
    ]

    if not repeated:
        return "No repeated failure patterns found yet."

    return (
        "Pay special attention to these repeated problems: "
        + "; ".join(repeated)
    )


def update_memory(failure_reasons, feedback):
    """Store feedback and update repeated failure patterns."""
    memory = load_memory()
    memory["total_runs"] = memory.get("total_runs", 0) + 1

    patterns = memory.setdefault("failure_patterns", {})

    for reason in failure_reasons:
        patterns[reason] = patterns.get(reason, 0) + 1

    history = memory.setdefault("feedback_history", [])
    history.append({
        "failure_reasons": failure_reasons,
        "feedback": feedback
    })

    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with MEMORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(memory, file, indent=2)

    return memory
