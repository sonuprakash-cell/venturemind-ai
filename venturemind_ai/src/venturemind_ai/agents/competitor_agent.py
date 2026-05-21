# competitor_agent.py

"""Competitor Analysis Agent"""

from src.venturemind_ai.tools.rag_tool import get_relevant_context
from src.venturemind_ai.tools.llm_tool import generate_response


def analyze_competitors(startup_idea, industry):
    """
    Analyze competitors, differentiation, and risks.
    """

    query = f"""
    Startup Idea: {startup_idea}
    Industry: {industry}
    """

    context = get_relevant_context(query)

    prompt = f"""
    You are a Competitor Analysis Expert.

    Analyze the startup idea and provide:
    1. Possible competitors
    2. Existing market solutions
    3. Differentiation opportunities
    4. Competitive risks
    5. Market challenges

    Startup Idea:
    {startup_idea}

    Industry:
    {industry}

    Retrieved Knowledge:
    {context}
    """

    return generate_response(prompt)