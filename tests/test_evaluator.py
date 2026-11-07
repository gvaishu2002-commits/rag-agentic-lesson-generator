import json
from src.evaluator import LessonEvaluator


class MockResponse:
    def __init__(self, output_text):
        self.output_text = output_text


class MockResponses:
    def __init__(self, output_text):
        self.output_text = output_text

    def create(self, **kwargs):
        return MockResponse(self.output_text)


class MockClient:
    def __init__(self, output_text):
        self.responses = MockResponses(output_text)


def test_evaluator_passes_all_criteria(monkeypatch):
    evaluator = LessonEvaluator.__new__(LessonEvaluator)

    result = {
        "passed": True,
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

    evaluator.client = MockClient(json.dumps(result))

    evaluation = evaluator.evaluate("Introduction to RAG", "Test lesson")

    assert evaluation["passed"] is True
    assert len(evaluation["failure_reasons"]) == 0


def test_evaluator_fails_missing_criteria():
    evaluator = LessonEvaluator.__new__(LessonEvaluator)

    result = {
        "passed": True,
        "criteria": {
            "accuracy": True,
            "beginner_friendly": False
        },
        "improvement_instructions": ["Explain concepts simply"]
    }

    evaluator.client = MockClient(json.dumps(result))

    evaluation = evaluator.evaluate("Introduction to RAG", "Test lesson")

    assert evaluation["passed"] is False
    assert "beginner_friendly" in evaluation["failure_reasons"]


def test_evaluator_handles_invalid_json():
    evaluator = LessonEvaluator.__new__(LessonEvaluator)
    evaluator.client = MockClient("Invalid JSON")

    evaluation = evaluator.evaluate("Introduction to RAG", "Test lesson")

    assert evaluation["passed"] is False
    assert "Evaluator returned invalid JSON" in evaluation["failure_reasons"]
