# market_agent.py

"""Market Research Agent"""

from src.venturemind_ai.tools.rag_tool import get_relevant_context
from src.venturemind_ai.tools.llm_tool import generate_response


def analyze_market(startup_idea, industry, target_audience):
    """
    Analyze market trends, opportunities, and audience potential.
    """

    query = f"""
    Startup Idea: {startup_idea}
    Industry: {industry}
    Target Audience: {target_audience}
    """

    context = get_relevant_context(query)

    prompt = f"""
    You are a Market Research Analyst.

    Analyze the following startup idea and provide:
    1. Industry trends
    2. Market opportunities
    3. Target audience insights
    4. Potential demand
    5. Growth potential

    Startup Idea:
    {startup_idea}

    Industry:
    {industry}

    Target Audience:
    {target_audience}

    Retrieved Knowledge:
    {context}
    """

    return generate_response(prompt)