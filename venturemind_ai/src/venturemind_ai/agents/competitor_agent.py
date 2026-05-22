# competitor_agent.py

from tools.rag_tool import get_relevant_context
from tools.llm_tool import generate_response


def analyze_competitors(state):

    startup_idea = state.get("startup_idea")

    market_analysis = state.get("market_analysis")

    context = state.get("retrieved_context")

    prompt = f"""
    You are a Competitor Analysis AI Agent.

    Startup Idea:
    {startup_idea}

    Market Analysis:
    {market_analysis}

    Context:
    {context}

    Analyze:
    - Existing competitors
    - Competitive advantages
    - Market gaps
    - Differentiation strategy
    """

    response = generate_response(prompt)

    state.update("competitor_analysis", response)

    return state