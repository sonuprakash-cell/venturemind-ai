# main.py

"""Entry point for VentureMind AI."""

from crew import run_venturemind_workflow


def main():

    startup_idea = input("Enter Startup Idea: ")

    industry = input("Enter Industry: ")

    target_audience = input("Enter Target Audience: ")

    print("\nGenerating Startup Validation Report...\n")

    report = run_venturemind_workflow(
        startup_idea,
        industry,
        target_audience
    )

    print(report)


if __name__ == "__main__":
    main()