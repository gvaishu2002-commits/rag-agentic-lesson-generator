
"""Generate beginner-friendly lessons using the OpenAI API."""

import os
from openai import OpenAI

from src.prompts import GENERATOR_PROMPT


class LessonGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate(self, topic, feedback="", memory_guidance=""):
        prompt = GENERATOR_PROMPT.format(
            topic=topic,
            feedback=feedback or "No previous feedback.",
            memory_guidance=memory_guidance or "No previous memory guidance."
        )

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text
