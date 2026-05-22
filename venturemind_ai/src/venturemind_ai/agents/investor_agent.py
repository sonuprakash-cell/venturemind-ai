# investor_agent.py

from tools.rag_tool import get_relevant_context
from tools.llm_tool import generate_response


def evaluate_startup(state):

    startup_idea = state.get("startup_idea")

    market_analysis = state.get("market_analysis")

    competitor_analysis = state.get("competitor_analysis")

    context = state.get("retrieved_context")

    prompt = f"""
    You are an Investor AI Agent.

    Startup Idea:
    {startup_idea}

    Market Analysis:
    {market_analysis}

    Competitor Analysis:
    {competitor_analysis}

    Context:
    {context}

    Evaluate:
    - Investment potential
    - Scalability
    - Business risks
    - Funding readiness
    """

    response = generate_response(prompt)

    state.update("investor_feedback", response)

    return state