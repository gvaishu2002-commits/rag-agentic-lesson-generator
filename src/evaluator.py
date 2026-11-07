"""Evaluate lesson quality using a strict pass/fail rubric."""

import json
import os
from openai import OpenAI

from src.prompts import EVALUATOR_PROMPT


class LessonEvaluator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def evaluate(self, topic, lesson):
        prompt = EVALUATOR_PROMPT.format(
            topic=topic,
            lesson=lesson
        )

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        try:
            result = json.loads(response.output_text)
        except json.JSONDecodeError:
            return {
                "passed": False,
                "criteria": {},
                "failure_reasons": ["Evaluator returned invalid JSON"],
                "improvement_instructions": [
                    "Return valid JSON matching the required rubric."
                ]
            }

        required = [
            "accuracy",
            "beginner_friendly",
            "examples",
            "jargon_explained",
            "key_points",
            "logical_flow"
        ]

        criteria = result.get("criteria", {})
        failures = [
            name for name in required
            if criteria.get(name) is not True
        ]

        return {
            "passed": not failures,
            "criteria": criteria,
            "failure_reasons": failures,
            "improvement_instructions": result.get(
                "improvement_instructions", []
            )
        }
