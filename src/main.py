"""Run the self-evaluating lesson generation agent."""

from dotenv import load_dotenv
from src.agent import LessonAgent


def main():
    load_dotenv()

    topic = "Introduction to RAG"
    agent = LessonAgent(max_retries=2)

    result = agent.run(topic)

    if result["passed"]:
        print("\nSUCCESS: Lesson passed evaluation.")
        print(f"Attempts: {len(result['attempts'])}")
        print("\nFINAL LESSON\n")
        print(result["lesson"])
    else:
        print("\nThe lesson did not pass after all attempts.")
        print(f"Attempts: {len(result['attempts'])}")
        print("Check output/rejection_logs.jsonl for details.")


if __name__ == "__main__":
    main()
