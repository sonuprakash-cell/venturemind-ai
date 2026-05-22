from agents.market_agent import analyze_market
from agents.competitor_agent import analyze_competitors
from agents.gtm_agent import generate_gtm_strategy
from agents.investor_agent import evaluate_startup
from agents.web_research_agent import web_research


def web_research_node(state):
    return web_research(state)


def market_node(state):
    return analyze_market(state)


def competitor_node(state):
    return analyze_competitors(state)


def gtm_node(state):
    return generate_gtm_strategy(state)


def investor_node(state):
    return evaluate_startup(state)