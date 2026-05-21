# gtm_agent.py

"""Go-To-Market Strategy Agent"""

from src.venturemind_ai.tools.rag_tool import get_relevant_context
from src.venturemind_ai.tools.llm_tool import generate_response


def generate_gtm_strategy(startup_idea, target_audience):
    """
    Generate go-to-market strategy and customer acquisition plan.
    """

    query = f"""
    Startup Idea: {startup_idea}
    Target Audience: {target_audience}
    """

    context = get_relevant_context(query)

    prompt = f"""
    You are a Go-To-Market Strategy Consultant.

    Generate:
    1. Product positioning
    2. Customer acquisition channels
    3. Launch strategy
    4. Pricing suggestions
    5. Marketing recommendations

    Startup Idea:
    {startup_idea}

    Target Audience:
    {target_audience}

    Retrieved Knowledge:
    {context}
    """

    return generate_response(prompt)