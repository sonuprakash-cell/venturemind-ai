# app.py

import streamlit as st
from crew import run_venturemind_workflow


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="VentureMind AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown(
    """
    <style>

    /* -----------------------------------
       REMOVE STREAMLIT HEADER
    ----------------------------------- */

    header {
        visibility: hidden;
        height: 0px;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    [data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem;
    }

    footer {
        visibility: hidden;
    }

    /* -----------------------------------
       MAIN APP
    ----------------------------------- */

    .stApp {
        background: linear-gradient(to bottom right, #f8fafc, #eef2ff);
        color: #111827;
        font-family: 'Inter', sans-serif;
    }

    /* -----------------------------------
       SIDEBAR
    ----------------------------------- */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #05052e 0%,
            #0a0a4f 100%
        );

        min-width: 280px !important;
        max-width: 280px !important;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* -----------------------------------
       MAIN TITLE
    ----------------------------------- */

    .main-title {

        font-size: 72px;
        font-weight: 800;
        line-height: 1.05;

        margin-bottom: 12px;

        color: #111827;
    }

    .gradient-text {

        background: linear-gradient(
            90deg,
            #7c3aed,
            #2563eb
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* -----------------------------------
       SUBTITLE
    ----------------------------------- */

    .subtitle {

        font-size: 22px;

        color: #6b7280;

        margin-bottom: 40px;
    }

    

    /* -----------------------------------
       INPUTS
    ----------------------------------- */

    .stTextInput input,
    .stTextArea textarea {

        border-radius: 16px !important;

        border: 1px solid #d1d5db !important;

        padding: 16px !important;

        font-size: 16px !important;

        background: #ffffff !important;
    }

    /* -----------------------------------
       BUTTON
    ----------------------------------- */

    .stButton > button {

        background: linear-gradient(
            90deg,
            #7c3aed,
            #2563eb
        );

        color: white;

        border: none;

        border-radius: 14px;

        padding: 16px 28px;

        font-size: 18px;

        font-weight: 700;

        width: 100%;

        transition: 0.3s;
    }

    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0px 8px 25px rgba(99,102,241,0.35);
    }

    /* -----------------------------------
       FEATURE SECTION
    ----------------------------------- */

    .feature-card {

        background: white;

        padding: 30px 22px;

        border-radius: 24px;

        text-align: center;

        min-height: 360px;

        display: flex;

        flex-direction: column;

        justify-content: flex-start;

        align-items: center;

        box-shadow:
            0px 8px 24px rgba(0,0,0,0.05);

        transition: 0.3s ease;
    }

    .feature-card:hover {

        transform: translateY(-6px);

        box-shadow:
            0px 12px 30px rgba(0,0,0,0.08);
    }

    .feature-icon {

        font-size: 58px;

        margin-bottom: 18px;
    }

    .feature-title {

        font-size: 22px;

        font-weight: 700;

        color: #111827;

        margin-top: 10px;

        margin-bottom: 20px;

        line-height: 1.4;
    }

    .feature-desc {

        font-size: 16px;

        line-height: 1.8;

        color: #6b7280;

        margin-top: auto;
    }

    /* -----------------------------------
       SUCCESS / REPORT
    ----------------------------------- */

    .report-box {

        background: white;

        padding: 35px;

        border-radius: 24px;

        margin-top: 30px;

        box-shadow:
            0px 10px 30px rgba(0,0,0,0.06);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.markdown("# 🚀 VentureMind AI")

    st.markdown("---")

    st.markdown("🧠 AI Insights")
    st.markdown("🚀 Venture Hub")
    st.markdown("📊 Validation Studio")
    st.markdown("🌐 Live Market Signals")
    st.markdown("💰 Investor Intelligence")

    st.markdown("---")



# -----------------------------------
# HERO SECTION
# -----------------------------------

st.markdown(
    """
    <div class='main-title'>
        Validate <span class='gradient-text'>Smarter.</span><br>
        Build <span class='gradient-text'>Better.</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
        AI-powered startup validation using RAG and multi-agent workflows.
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------------
# MAIN FORM CARD
# -----------------------------------

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.subheader("💡 Enter Your Startup Idea")

startup_idea = st.text_area(
    "Startup Idea",
    height=180,
    placeholder="Example: AI platform that helps students build portfolios automatically"
)

col1, col2 = st.columns(2)

with col1:

    industry = st.text_input(
        "Industry / Domain",
        placeholder="Example: EdTech"
    )

with col2:

    target_audience = st.text_input(
        "Target Audience",
        placeholder="Example: College students"
    )


# -----------------------------------
# GENERATE REPORT BUTTON
# -----------------------------------

if st.button("✨ Generate Startup Report"):

    if not startup_idea.strip():

        st.warning("Please enter startup idea.")

    elif not industry.strip():

        st.warning("Please enter industry/domain.")

    elif not target_audience.strip():

        st.warning("Please enter target audience.")

    else:

        try:

            with st.spinner(
                "Generating startup validation report..."
            ):

                report = run_venturemind_workflow(
                    startup_idea=startup_idea,
                    industry=industry,
                    target_audience=target_audience
                )

            st.success("Report generated successfully!")

            st.markdown(report)

        except Exception as e:

            st.error(f"Application Error: {str(e)}")

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------
# FEATURES SECTION
# -----------------------------------

st.markdown("## ✨ Platform Features")

f1, f2, f3, f4 = st.columns(4)

with f1:

    st.markdown(
        """
        <div class='feature-card'>
            <h1>📊</h1>
            <div class='feature-title'>Market Research</div>
            <div class='feature-desc'>
                Analyze trends, demand, and market opportunities.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with f2:

    st.markdown(
        """
        <div class='feature-card'>
            <h1>🧠</h1>
            <div class='feature-title'>Competitor Analysis</div>
            <div class='feature-desc'>
                Identify competitors, strengths, and gaps.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with f3:

    st.markdown(
        """
        <div class='feature-card'>
            <h1>🎯</h1>
            <div class='feature-title'>GTM Strategy</div>
            <div class='feature-desc'>
                AI-generated go-to-market planning strategies.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with f4:

    st.markdown(
        """
        <div class='feature-card'>
            <h1>💰</h1>
            <div class='feature-title'>Investor Feedback</div>
            <div class='feature-desc'>
                Evaluate startup investment readiness instantly.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )