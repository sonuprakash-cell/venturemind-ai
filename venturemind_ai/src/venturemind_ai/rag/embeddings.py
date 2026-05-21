# embeddings.py

"""Generate embeddings using OpenAI."""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Embedding model
EMBEDDING_MODEL = "text-embedding-3-small"


def get_embedding(text: str):
    """
    Generate embedding vector for text.
    """

    text = text.replace("\n", " ")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding