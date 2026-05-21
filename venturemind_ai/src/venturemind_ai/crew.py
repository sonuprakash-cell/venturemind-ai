# crew.py

"""Main workflow orchestration for VentureMind AI."""

from agents.market_agent import analyze_market
from agents.competitor_agent import analyze_competitors
from agents.gtm_agent import generate_gtm_strategy
from agents.investor_agent import evaluate_startup

from src.venturemind_ai.agents.market_agent import analyze_market 
from tools.report_generator import generate_final_report


def run_venturemind_workflow(
    startup_idea,
    industry,
    target_audience
):
    """
    Execute complete VentureMind AI workflow.
    """

    # Run Market Research Agent
    market_analysis = analyze_market(
        startup_idea,
        industry,
        target_audience
    )

    # Run Competitor Analysis Agent
    competitor_analysis = analyze_competitors(
        startup_idea,
        industry
    )

    # Run GTM Strategy Agent
    gtm_strategy = generate_gtm_strategy(
        startup_idea,
        target_audience
    )

    # Run Investor Feedback Agent
    investor_feedback = evaluate_startup(
        startup_idea,
        industry
    )

    # Generate Final Report
    final_report = generate_final_report(
        startup_idea=startup_idea,
        industry=industry,
        target_audience=target_audience,
        market_analysis=market_analysis,
        competitor_analysis=competitor_analysis,
        gtm_strategy=gtm_strategy,
        investor_feedback=investor_feedback
    )

    return final_report