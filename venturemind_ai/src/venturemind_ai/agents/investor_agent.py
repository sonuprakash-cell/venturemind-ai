# investor_agent.py

"""Investor Feedback Agent"""

from src.venturemind_ai.tools.rag_tool import get_relevant_context
from src.venturemind_ai.tools.llm_tool import generate_response


def evaluate_startup(startup_idea, industry):
    """
    Generate investor-style startup feedback.
    """

    query = f"""
    Startup Idea: {startup_idea}
    Industry: {industry}
    """

    context = get_relevant_context(query)

    prompt = f"""
    You are an Investor evaluating startup ideas.

    Analyze the startup and provide:
    1. Investment potential
    2. Scalability analysis
    3. Revenue potential
    4. Business risks
    5. Improvement suggestions

    Startup Idea:
    {startup_idea}

    Industry:
    {industry}

    Retrieved Knowledge:
    {context}
    """

    return generate_response(prompt)