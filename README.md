
# Self-Evaluating AI Lesson Content Generator

## 1. Project Overview

This project is designed to build an Agentic AI system that generates, evaluates, and improves beginner-friendly learning content.

The assessment topic is Introduction to RAG (Retrieval-Augmented Generation).

The target audience is a Class 12 graduate from India with limited English vocabulary and a non-English-medium educational background who wants to start an AI career.

The system follows a generate, evaluate, and regenerate workflow to ensure that the lesson meets the required quality standards before it is accepted.

## 2. Problem Statement

AI-generated educational content may contain incorrect information, difficult language, missing explanations, or confusing examples.

The goal of this project is to create a system that can generate a lesson, evaluate its quality, identify problems, and improve the content using feedback.

## 3. Project Objectives

- Generate a standalone beginner-friendly lesson about RAG.
- Explain what RAG is, why it matters, and how it works.
- Evaluate the lesson using a clear pass/fail rubric.
- Identify and record content failures.
- Regenerate failed content using evaluator feedback.
- Limit regeneration to a maximum of two retries.
- Maintain rejection logs.
- Store feedback in persistent memory.
- Use repeated failure patterns to improve future prompts and evaluation instructions.

## 4. Agentic Workflow

The system follows these steps:

1. **Input:** Receive a topic from the user.
2. **Generate:** Create a beginner-friendly lesson.
3. **Evaluate:** Check the lesson against the quality rubric.
4. **Decision:** Decide whether the lesson passes or fails.
5. **Reject:** Record the reasons when the lesson fails.
6. **Feedback:** Send improvement instructions to the generator.
7. **Regenerate:** Create an improved lesson, with a maximum of two retries.
8. **Output:** Save the passing lesson and rejection log.
9. **Memory:** Store feedback and repeated failure patterns for future runs.

## 5. Quality Evaluation Rubric

Each criterion has a strict pass/fail result. No partial credit is given.

| Criterion | Evaluation |
|---|---|
| Accuracy and grounding | Information must be correct and reliable. |
| Beginner-friendly language | A beginner should understand the explanation. |
| Teaching by example | The lesson should include useful examples. |
| Clear language | Technical terms must be explained. |
| Key point coverage | Important concepts must be covered. |
| Coherent teaching flow | The lesson must follow a logical order. |

The lesson is accepted only when all required criteria pass.

## 6. Retry and Rejection Handling

When a lesson fails the evaluation:

- The evaluator identifies the failed criteria.
- The reasons for rejection are recorded.
- Improvement instructions are created.
- The generator uses the feedback to improve the lesson.
- The evaluator checks the revised lesson again.

The system allows a maximum of two retries. If the lesson still fails, the workflow terminates and reports the failure instead of accepting unsuccessful content.

## 7. Self-Evolving Mechanism

The system records repeated failure patterns and uses previous feedback to improve future generation instructions.

For example, if lessons repeatedly contain unexplained technical terms, the system can store this failure pattern and strengthen future instructions to explain technical words in simple language.

This allows the workflow to improve its instructions based on previous results.

## 8. Persistent Memory

The project uses JSON-based persistent memory to store information across multiple runs.

Memory is designed to store:

- Previous generation runs
- Repeated failure patterns
- Evaluation feedback
- Improvement instructions
- Run history

The stored feedback is used to guide future generation and improvement.

## 9. System Architecture

The project is divided into separate components:

- **Generator:** Creates the lesson.
- **Evaluator:** Checks the lesson against the quality rubric.
- **Agent:** Controls the workflow and retry limit.
- **Memory:** Stores previous feedback and failure patterns.
- **Rejection Logger:** Records failures and improvement details.
- **Output Handler:** Saves the final lesson and run report.

This modular structure makes the workflow easier to understand, test, maintain, and improve.

The generator and evaluator are separate so that generated content is checked before acceptance.

## 10. Technology Stack

- Python
- OpenAI API
- JSON for persistent memory
- Pytest for testing
- GitHub for version control

## 11. Project Structure

```text
rag-agentic-lesson-generator/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── generator.py
│   ├── evaluator.py
│   ├── prompts.py
│   ├── memory.py
│   └── rejection_logger.py
├── tests/
│   └── test_evaluator.py
├── docs/
│   └── architecture.md
├── data/
└── output/
```

## 12. Setup Instructions

### Step 1: Clone the repository

```bash
git clone https://github.com/gvaishu2002-commits/rag-agentic-lesson-generator.git
cd rag-agentic-lesson-generator
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

For Windows:

```bash
venv\Scripts\activate
```

For macOS or Linux:

```bash
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file using `.env.example`.

Add the following configuration:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
MAX_RETRIES=2
```

Never upload your actual API key to GitHub.

### Step 5: Run the application

```bash
python -m src.main --topic "Introduction to RAG"
```

### Step 6: Run the tests

```bash
pytest -q
```

## 13. Expected Outputs

The completed application is designed to produce:

- Beginner-friendly lesson content
- Quality evaluation results
- Pass/fail decisions
- Rejection reasons
- Retry history
- Improvement instructions
- Final run report
- Persistent memory updates

## 14. Limitations

- Content quality depends partly on the selected language model.
- Automated evaluation cannot guarantee detection of every factual error.
- Live generation requires a valid API key and internet connection.
- Persistent memory is stored locally in JSON format.

## 15. Conclusion

This project demonstrates an Agentic AI workflow that generates educational content, evaluates quality, rejects unsuccessful outputs, and improves lessons through controlled retries and feedback.

The objective is to create reliable, beginner-friendly learning content and demonstrate how an AI system can evaluate and improve its own output.

## Author

GenAI Engineer – Content Systems Take-Home Assessment
