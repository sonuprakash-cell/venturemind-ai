# market_agent.py

from tools.rag_tool import get_relevant_context
from tools.llm_tool import generate_response


def analyze_market(state):

    startup_idea = state.get("startup_idea")
    industry = state.get("industry")
    target_audience = state.get("target_audience")

    query = f"""
    Startup Idea: {startup_idea}

    Industry: {industry}

    Target Audience: {target_audience}
    """

    context = state.get("retrieved_context")

    prompt = f"""
    You are a Market Research AI Agent.

    Analyze the following startup idea.

    Startup Idea:
    {startup_idea}

    Industry:
    {industry}

    Target Audience:
    {target_audience}

    Context:
    {context}

    Provide:
    - Market trends
    - Market demand
    - Opportunities
    - Risks
    """

    response = generate_response(prompt)

    state.update("market_analysis", response)

    return state