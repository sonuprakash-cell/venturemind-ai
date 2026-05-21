# report_generator.py

"""Generate final startup validation report."""


def generate_final_report(
    startup_idea,
    industry,
    target_audience,
    market_analysis,
    competitor_analysis,
    gtm_strategy,
    investor_feedback=None
):
    """
    Generate structured startup validation report.
    """

    report = f"""
# VentureMind AI - Startup Validation Report

## Startup Idea
{startup_idea}

## Industry
{industry}

## Target Audience
{target_audience}

---

# Market Research Analysis
{market_analysis}

---

# Competitor Analysis
{competitor_analysis}

---

# Go-To-Market Strategy
{gtm_strategy}
"""

    if investor_feedback:
        report += f"""

---

# Investor Feedback
{investor_feedback}
"""

    report += """

---

# SWOT Analysis

## Strengths
- Innovative startup concept
- Potential market opportunity
- AI-driven business strategy

## Weaknesses
- Early-stage validation challenges
- Market competition risks

## Opportunities
- Growing industry demand
- Expansion and scalability potential

## Threats
- Competitive market landscape
- Customer acquisition challenges

---

# Final Recommendation

The startup idea demonstrates promising potential.
Further customer validation, MVP testing,
and market experimentation are recommended
before large-scale development.

"""

    return report