# llm_tool.py

"""LLM utility tool for OpenAI responses."""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Chat model
CHAT_MODEL = "gpt-4o-mini"


def generate_response(prompt):
    """
    Generate response using OpenAI model.

    Args:
        prompt (str): Prompt input

    Returns:
        str: AI-generated response
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert startup business consultant "
                    "specialized in startup validation, "
                    "market research, competitor analysis, "
                    "and go-to-market strategies."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content