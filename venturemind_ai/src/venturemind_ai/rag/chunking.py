# chunking.py

"""Text chunking utility."""


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into smaller chunks.

    Args:
        text (str): Input text
        chunk_size (int): Size of each chunk
        overlap (int): Overlap between chunks

    Returns:
        list: List of text chunks
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks