import streamlit as st
import pandas as pd

from utils.calculations import budget_summary
from utils.database import append_data, add_history
from utils.helpers import money

st.set_page_config(page_title="Budget Planner", page_icon="💰")

st.title("💰 Budget Planner")

st.divider()

month = st.selectbox(
    "Select Month",
    [
        "January","February","March","April",
        "May","June","July","August",
        "September","October","November","December"
    ]
)

income = st.number_input(
    "Monthly Income (₹)",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)

st.subheader("Expenses")

rent = st.number_input("Rent", 0.0, value=10000.0)

food = st.number_input("Food", 0.0, value=5000.0)

transport = st.number_input("Transport", 0.0, value=2000.0)

shopping = st.number_input("Shopping", 0.0, value=3000.0)

bills = st.number_input("Bills", 0.0, value=4000.0)

others = st.number_input("Others", 0.0, value=1000.0)

total_expense = (
    rent
    + food
    + transport
    + shopping
    + bills
    + others
)

if st.button("Generate Budget"):

    savings, percent = budget_summary(
        income,
        total_expense
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Income", money(income))

    c2.metric("Expenses", money(total_expense))

    c3.metric("Savings", money(savings))

    st.progress(
        min(total_expense / income, 1.0)
        if income > 0
        else 0
    )

    if savings >= 0:

        st.success(
            f"Estimated Savings : {money(savings)}"
        )

    else:

        st.error(
            f"Overspent by {money(abs(savings))}"
        )

    st.info(
        f"Savings Percentage : {percent:.2f}%"
    )

    append_data(
        {
            "Month": month,
            "Income": income,
            "Budget": income,
            "Spent": total_expense
        },
        "budget.csv"
    )

    add_history(
        "Budget Planner",
        f"{month} | Income={income} | Expense={total_expense}"
    )