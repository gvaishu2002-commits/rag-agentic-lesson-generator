from generator import LessonGenerator
from evaluator import LessonEvaluator
from rejection_logger import RejectionLogger

topic = "Introduction to RAG"

generator = LessonGenerator()
evaluator = LessonEvaluator()
logger = RejectionLogger()

lesson = generator.generate(topic)

result = evaluator.evaluate(lesson)

if result["passed"]:
    print("Lesson Passed")
    print(lesson)
else:
    print("Lesson Failed")
    logger.log(result["failures"])

    for failure in result["failures"]:
        print(failure)
