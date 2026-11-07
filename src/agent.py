"""Control the generate, evaluate and regenerate workflow."""

from src.generator import LessonGenerator
from src.evaluator import LessonEvaluator
from src.memory import (
    load_memory,
    get_improvement_guidance,
    update_memory
)
from src.rejection_logger import save_run_report


class LessonAgent:
    def __init__(self, max_retries=2):
        self.generator = LessonGenerator()
        self.evaluator = LessonEvaluator()
        self.max_retries = min(max(0
