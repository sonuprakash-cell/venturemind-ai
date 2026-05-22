# ingest.py

"""Ingest knowledge documents into FAISS vector store."""

import os
import pickle
import faiss
import numpy as np

from rag.chunking import chunk_text
from rag.embeddings import get_embedding

# Paths
KNOWLEDGE_PATH = "knowledge"
FAISS_INDEX_PATH = "faiss_index.index"
DOCUMENTS_PATH = "documents.pkl"


def load_documents():
    """
    Load all text documents from knowledge folder.
    """

    documents = []

    for root, _, files in os.walk(KNOWLEDGE_PATH):

        for file in files:

            if file.endswith(".txt"):

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                documents.append({
                    "file_name": file,
                    "content": text
                })

    return documents


def ingest_documents():
    """
    Chunk documents, generate embeddings,
    and store in FAISS.
    """

    documents = load_documents()

    all_chunks = []
    all_embeddings = []

    for doc in documents:

        chunks = chunk_text(doc["content"])

        for chunk in chunks:

            embedding = get_embedding(chunk)

            all_chunks.append(chunk)
            all_embeddings.append(embedding)

    # Convert embeddings to numpy array
    embeddings_array = np.array(all_embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings_array.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings_array)

    # Save index
    faiss.write_index(index, FAISS_INDEX_PATH)

    # Save chunks
    with open(DOCUMENTS_PATH, "wb") as f:
        pickle.dump(all_chunks, f)

    print("Documents successfully ingested into FAISS.")


if __name__ == "__main__":
    ingest_documents()