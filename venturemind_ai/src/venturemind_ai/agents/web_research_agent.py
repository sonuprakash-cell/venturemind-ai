# web_research_agent.py

from tools.llm_tool import generate_response


def web_research(state):

    startup_idea = state.get("startup_idea")

    industry = state.get("industry")

    prompt = f"""
    You are a Web Research AI Agent.

    Analyze recent trends, market opportunities,
    and real-world startup ecosystem insights for:

    Startup Idea:
    {startup_idea}

    Industry:
    {industry}

    Provide:
    - Recent industry trends
    - Emerging competitors
    - Market opportunities
    - Industry risks
    """

    response = generate_response(prompt)

    state.update("web_research", response)

    return state