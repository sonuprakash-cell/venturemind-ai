# report_generator.py


def generate_final_report(state):

    startup_idea = state.get("startup_idea")

    industry = state.get("industry")

    target_audience = state.get("target_audience")

    market_analysis = state.get("market_analysis")

    competitor_analysis = state.get("competitor_analysis")

    gtm_strategy = state.get("gtm_strategy")

    investor_feedback = state.get("investor_feedback")

    report = f"""
# 🚀 VentureMind AI Startup Validation Report

---

## 🧠 Startup Overview

### Startup Idea
{startup_idea}

### Industry
{industry}

### Target Audience
{target_audience}

---

# 📊 Market Analysis

{market_analysis}

---

# 🥊 Competitor Analysis

{competitor_analysis}

---

# 🎯 Go-To-Market Strategy

{gtm_strategy}

---

# 💰 Investor Feedback

{investor_feedback}

---

# ✅ Final Recommendation

This startup idea demonstrates promising potential based on the analyzed market trends, competitive positioning, and scalability opportunities.

Recommended next steps:
- Build MVP quickly
- Validate with early users
- Focus on differentiation
- Improve customer acquisition strategy
- Gather continuous market feedback
"""

    return report