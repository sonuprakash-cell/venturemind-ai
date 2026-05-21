# rag_tool.py

"""RAG utility tool."""

from rag.retriever import retrieve_context


def get_relevant_context(query):
    """
    Retrieve relevant startup knowledge context.

    Args:
        query (str): User query

    Returns:
        str: Retrieved context
    """

    context = retrieve_context(query)

    return context