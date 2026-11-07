class LessonEvaluator:

    def evaluate(self, lesson):
        failures = []

        if len(lesson.split()) < 300:
            failures.append("Lesson is too short")

        if "example" not in lesson.lower():
            failures.append("Example is missing")

        if failures:
            return {
                "passed": False,
                "failures": failures
            }

        return {
            "passed": True,
            "failures": []
        }
