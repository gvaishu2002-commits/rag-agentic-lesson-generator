import json
from src import memory


def test_load_memory_returns_empty_structure(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "MEMORY_FILE", tmp_path / "memory.json")

    result = memory.load_memory()

    assert result["total_runs"] == 0
    assert result["failure_patterns"] == {}
    assert result["feedback_history"] == []


def test_update_memory_saves_feedback(tmp_path, monkeypatch):
    monkeypatch.setattr(memory, "MEMORY_FILE", tmp_path / "memory.json")

    result = memory.update_memory(
        ["examples"],
        "Add more beginner-friendly examples"
    )

    assert result["failure_patterns"]["examples"] == 1
    assert result["total_runs"] == 1

    saved = json.loads(
        (tmp_path / "memory.json").read_text(encoding="utf-8")
    )

    assert saved["feedback_history"][0]["failure_reasons"] == ["examples"]


def test_repeated_failures_generate_guidance():
    guidance = memory.get_improvement_guidance({
        "failure_patterns": {"examples": 2}
    })

    assert "examples" in guidance
