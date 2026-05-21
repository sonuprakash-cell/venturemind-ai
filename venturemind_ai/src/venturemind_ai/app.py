# app.py

"""Streamlit frontend for VentureMind AI."""

import streamlit as st

from crew import run_venturemind_workflow

# Page configuration
st.set_page_config(
    page_title="VentureMind AI",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 VentureMind AI")

st.subheader(
    "AI-powered startup validation using RAG and multi-agent workflows"
)

# User Inputs
startup_idea = st.text_area(
    "Enter your startup idea"
)

industry = st.text_input(
    "Industry / Domain"
)

target_audience = st.text_input(
    "Target Audience"
)

# Generate Button
if st.button("Generate Startup Report"):

    if not startup_idea or not industry or not target_audience:

        st.warning("Please fill all fields.")

    else:

        with st.spinner("Generating startup validation report..."):

            report = run_venturemind_workflow(
                startup_idea,
                industry,
                target_audience
            )

        st.success("Report generated successfully!")

        st.markdown(report)