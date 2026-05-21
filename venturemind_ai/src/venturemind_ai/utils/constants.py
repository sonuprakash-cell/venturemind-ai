# constants.py

"""Project constants."""

# OpenAI Models
CHAT_MODEL = "gpt-4o-mini"
EMBEDDING_MODEL = "text-embedding-3-small"

# ChromaDB
COLLECTION_NAME = "venturemind_knowledge"
CHROMA_DB_PATH = "chroma_db"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval
TOP_K_RESULTS = 3

# Temperature
TEMPERATURE = 0.7