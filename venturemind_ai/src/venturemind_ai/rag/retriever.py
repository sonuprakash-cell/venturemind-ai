# retriever.py

"""Retrieve relevant context using FAISS."""

import pickle
import faiss
import numpy as np

from rag.embeddings import get_embedding

# Paths
FAISS_INDEX_PATH = "faiss_index.index"
DOCUMENTS_PATH = "documents.pkl"

# Load FAISS index
index = faiss.read_index(FAISS_INDEX_PATH)

# Load document chunks
with open(DOCUMENTS_PATH, "rb") as f:
    documents = pickle.load(f)


def retrieve_context(query, top_k=3):
    """
    Retrieve relevant knowledge chunks.

    Args:
        query (str): User query
        top_k (int): Number of results

    Returns:
        str: Combined retrieved context
    """

    # Generate query embedding
    query_embedding = get_embedding(query)

    query_array = np.array([query_embedding]).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_array, top_k)

    retrieved_chunks = []

    for idx in indices[0]:

        if idx < len(documents):
            retrieved_chunks.append(documents[idx])

    context = "\n\n".join(retrieved_chunks)

    return context