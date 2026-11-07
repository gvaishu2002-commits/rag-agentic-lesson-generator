import json
from types import SimpleNamespace

from src.evaluator import LessonEvaluator


def test_evaluator_passes_all_criteria():
    result_data = {
        "criteria": {
            "accuracy": True,
            "beginner_friendly": True,
            "examples": True,
            "jargon_explained": True,
            "key_points": True,
            "logical_flow": True
        },
        "improvement_instructions": []
    }

    evaluator = object.__new__(LessonEvaluator)
    evaluator.client = SimpleNamespace(
        responses=SimpleNamespace(
            create=lambda **kwargs: SimpleNamespace(
                output_text=json.dumps(result_data)
            )
        )
    )

    result = evaluator.evaluate("Introduction to RAG", "Test lesson")

    assert result["passed"] is True
    assert result["failure_reasons"] == []


def test_evaluator_rejects_failed_criteria():
    result_data = {
        "criteria": {
            "accuracy": True,
            "beginner_friendly": False,
            "examples": True,
            "jargon_explained": True,
            "key_points": True,
            "logical_flow": True
        },
        "improvement_instructions": ["Explain terms simply"]
    }

    evaluator = object.__new__(LessonEvaluator)
    evaluator.client = SimpleNamespace(
        responses=SimpleNamespace(
            create=lambda **kwargs: SimpleNamespace(
                output_text=json.dumps(result_data)
            )
        )
    )

    result = evaluator.evaluate("Introduction to RAG", "Test lesson")

    assert result["passed"] is False
    assert "beginner_friendly" in result["failure_reasons"]
