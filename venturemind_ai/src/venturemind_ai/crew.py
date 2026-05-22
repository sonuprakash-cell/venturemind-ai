# crew.py

from graph.workflow import run_workflow


def run_venturemind_workflow(
    startup_idea,
    industry,
    target_audience
):

    state = run_workflow(
        startup_idea,
        industry,
        target_audience
    )

    return state.get("final_report")