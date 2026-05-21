# helpers.py

"""Helper utility functions."""

import re


def clean_text(text):
    """
    Clean unnecessary spaces and newlines.
    """

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def format_section(title, content):
    """
    Format report section.
    """

    return f"""
# {title}

{content}

"""


def generate_swot_template():
    """
    Return SWOT analysis template.
    """

    return """
# SWOT Analysis

## Strengths
-

## Weaknesses
-

## Opportunities
-

## Threats
-
"""


def truncate_text(text, max_length=1000):
    """
    Truncate long text safely.
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."