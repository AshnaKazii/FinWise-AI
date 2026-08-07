import streamlit as st

from utils.calculations import calculate_sip
from utils.database import add_history
from utils.helpers import money

st.set_page_config(page_title="SIP Calculator", page_icon="📈")

st.title("📈 SIP Calculator")

st.divider()

investment = st.number_input(
    "Monthly Investment (₹)",
    min_value=0.0,
    value=5000.0,
    step=500.0
)

rate = st.number_input(
    "Expected Annual Return (%)",
    min_value=1.0,
    value=12.0
)

years = st.number_input(
    "Investment Period (Years)",
    min_value=1,
    value=10
)

if st.button("Calculate SIP"):

    invested, wealth, future = calculate_sip(
        investment,
        rate,
        years
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Invested Amount", money(invested))
    c2.metric("Wealth Gained", money(wealth))
    c3.metric("Future Value", money(future))

    add_history(
        "SIP Calculator",
        f"Future Value={future}"
    )