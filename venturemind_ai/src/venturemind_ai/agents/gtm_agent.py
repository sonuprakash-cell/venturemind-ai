# gtm_agent.py

from tools.rag_tool import get_relevant_context
from tools.llm_tool import generate_response


def generate_gtm_strategy(state):

    startup_idea = state.get("startup_idea")

    competitor_analysis = state.get("competitor_analysis")

    context = state.get("retrieved_context")

    prompt = f"""
    You are a Go-To-Market Strategy AI Agent.

    Startup Idea:
    {startup_idea}

    Competitor Analysis:
    {competitor_analysis}

    Context:
    {context}

    Generate:
    - Launch strategy
    - Marketing channels
    - Customer acquisition strategy
    - Growth plan
    """

    response = generate_response(prompt)

    state.update("gtm_strategy", response)

    return state