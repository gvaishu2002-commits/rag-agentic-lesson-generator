
"""Control the generate, evaluate and regenerate workflow."""

from src.generator import LessonGenerator
from src.evaluator import LessonEvaluator
from src.memory import load_memory, get_improvement_guidance, update_memory
from src.rejection_logger import save_run_report


class LessonAgent:
    def __init__(self, max_retries=2):
        self.generator = LessonGenerator()
        self.evaluator = LessonEvaluator()
        self.max_retries = min(max(0, max_retries), 2)

    def run(self, topic):
        attempts = []
        feedback = ""

        memory = load_memory()
        memory_guidance = get_improvement_guidance(memory)

        for attempt_number in range(self.max_retries + 1):
            lesson = self.generator.generate(
                topic=topic,
                feedback=feedback,
                memory_guidance=memory_guidance
            )

            evaluation = self.evaluator.evaluate(topic, lesson)

            attempt_record = {
                "attempt": attempt_number + 1,
                "passed": evaluation["passed"],
                "criteria": evaluation["criteria"],
                "failure_reasons": evaluation.get("failure_reasons", []),
                "changes_applied": feedback
            }

            attempts.append(attempt_record)

            if evaluation["passed"]:
                save_run_report(
                    topic, attempts, True, final_lesson=lesson
                )
                return {
                    "passed": True,
                    "lesson": lesson,
                    "attempts": attempts
                }

            reasons = evaluation.get("failure_reasons", [])
            instructions = evaluation.get(
                "improvement_instructions", []
            )

            feedback = (
                "Fix these failed criteria: "
                + ", ".join(map(str, reasons))
                + ". Improvement instructions: "
                + "; ".join(map(str, instructions))
            )

            update_memory(reasons, feedback)

        save_run_report(topic, attempts, False)

        return {
            "passed": False,
            "lesson": None,
            "attempts": attempts
        }
