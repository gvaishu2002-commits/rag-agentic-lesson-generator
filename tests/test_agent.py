from src import agent as agent_module


class MockGenerator:
    def generate(self, **kwargs):
        return "Beginner-friendly RAG lesson"


class MockEvaluator:
    def __init__(self, results):
        self.results = iter(results)

    def evaluate(self, topic, lesson):
        return next(self.results)


def test_agent_passes_first_attempt(monkeypatch):
    monkeypatch.setattr(agent_module, "LessonGenerator", MockGenerator)
    monkeypatch.setattr(
        agent_module, "LessonEvaluator",
        lambda: MockEvaluator([{
            "passed": True,
            "criteria": {},
            "failure_reasons": []
        }])
    )
    monkeypatch.setattr(agent_module, "load_memory", lambda: {})
    monkeypatch.setattr(agent_module, "get_improvement_guidance", lambda m: "")
    monkeypatch.setattr(agent_module, "save_run_report", lambda *a, **k: None)

    result = agent_module.LessonAgent().run("Introduction to RAG")

    assert result["passed"] is True
    assert len(result["attempts"]) == 1


def test_agent_retries_after_failure(monkeypatch):
    monkeypatch.setattr(agent_module, "LessonGenerator", MockGenerator)
    monkeypatch.setattr(
        agent_module, "LessonEvaluator",
        lambda: MockEvaluator([
            {
                "passed": False,
                "criteria": {},
                "failure_reasons": ["examples"],
                "improvement_instructions": ["Add examples"]
            },
            {
                "passed": True,
                "criteria": {},
                "failure_reasons": []
            }
        ])
    )
    monkeypatch.setattr(agent_module, "load_memory", lambda: {})
    monkeypatch.setattr(agent_module, "get_improvement_guidance", lambda m: "")
    monkeypatch.setattr(agent_module, "update_memory", lambda *a: None)
    monkeypatch.setattr(agent_module, "save_run_report", lambda *a, **k: None)

    result = agent_module.LessonAgent(max_retries=2).run("Introduction to RAG")

    assert result["passed"] is True
    assert len(result["attempts"]) == 2
