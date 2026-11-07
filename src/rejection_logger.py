"""Save lesson evaluation results and rejected attempts."""

import json
from pathlib import Path


OUTPUT_DIR = Path("output")
LOG_FILE = OUTPUT_DIR / "rejection_logs.jsonl"


def save_run_report(topic, attempts, passed, final_lesson=None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    report = {
        "topic": topic,
        "passed": passed,
        "attempts": attempts
    }

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(report) + "\n")

    if passed and final_lesson:
        lesson_file = OUTPUT_DIR / "final_lesson.md"
        lesson_file.write_text(final_lesson, encoding="utf-8")
