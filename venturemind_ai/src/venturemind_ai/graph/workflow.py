# workflow.py

from graph.state import WorkflowState

from graph.nodes import (
    web_research_node,
    market_node,
    competitor_node,
    gtm_node,
    investor_node
)

from tools.rag_tool import get_relevant_context
from tools.report_generator import generate_final_report


def run_workflow(
    startup_idea,
    industry,
    target_audience
):

    state = WorkflowState()

    # Store inputs
    state.update("startup_idea", startup_idea)
    state.update("industry", industry)
    state.update("target_audience", target_audience)

    # -----------------------------
    # SINGLE RAG RETRIEVAL
    # -----------------------------

    query = f"""
    Startup Idea: {startup_idea}

    Industry: {industry}

    Target Audience: {target_audience}
    """

    retrieved_context = get_relevant_context(query)

    state.update("retrieved_context", retrieved_context)

    # -----------------------------
    # AGENT EXECUTION
    # -----------------------------

    web_research_node(state) 
    
    market_node(state)

    competitor_node(state)

    investor_node(state)

    gtm_node(state)

    # -----------------------------
    # FINAL REPORT
    # -----------------------------

    final_report = generate_final_report(state)

    state.update("final_report", final_report)

    return state