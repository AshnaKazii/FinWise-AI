import streamlit as st

from utils.calculations import calculate_emi
from utils.database import add_history
from utils.helpers import money

st.set_page_config(page_title="EMI Calculator", page_icon="🏦")

st.title("🏦 EMI Calculator")

st.divider()

loan = st.number_input(
    "Loan Amount (₹)",
    min_value=0.0,
    value=500000.0,
    step=10000.0
)

rate = st.number_input(
    "Annual Interest Rate (%)",
    min_value=0.0,
    value=8.5
)

years = st.number_input(
    "Loan Tenure (Years)",
    min_value=1,
    value=5
)

if st.button("Calculate EMI"):

    emi, interest, total = calculate_emi(
        loan,
        rate,
        years
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Monthly EMI", money(emi))
    c2.metric("Total Interest", money(interest))
    c3.metric("Total Payment", money(total))

    add_history(
        "EMI Calculator",
        f"Loan={loan}, EMI={emi}"
    )