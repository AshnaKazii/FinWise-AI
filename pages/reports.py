import streamlit as st
import pandas as pd

from utils.database import load_data
from utils.helpers import money

st.set_page_config(
    page_title="Reports",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Financial Reports")

st.divider()

expenses = load_data("expenses.csv")
budget = load_data("budget.csv")
savings = load_data("savings.csv")

# ------------------------
# Expense Report
# ------------------------

st.header("💸 Expense Summary")

if expenses.empty:

    st.info("No Expense Data Available.")

else:

    total_expense = expenses["Amount"].sum()

    average = expenses["Amount"].mean()

    maximum = expenses["Amount"].max()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Expense",
        money(total_expense)
    )

    c2.metric(
        "Average Expense",
        money(average)
    )

    c3.metric(
        "Highest Expense",
        money(maximum)
    )

    st.subheader("Category-wise Expenses")

    category = (
        expenses
        .groupby("Category")["Amount"]
        .sum()
        .reset_index()
        .sort_values(
            "Amount",
            ascending=False
        )
    )

    st.dataframe(
        category,
        use_container_width=True
    )

st.divider()

# ------------------------
# Budget Report
# ------------------------

st.header("💰 Budget Report")

if budget.empty:

    st.info("No Budget Records.")

else:

    total_income = budget["Income"].sum()

    spent = budget["Spent"].sum()

    savings_amt = total_income - spent

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Income",
        money(total_income)
    )

    c2.metric(
        "Spent",
        money(spent)
    )

    c3.metric(
        "Savings",
        money(savings_amt)
    )

    st.dataframe(
        budget,
        use_container_width=True
    )

st.divider()

# ------------------------
# Savings Report
# ------------------------

st.header("🎯 Savings Goals")

if savings.empty:

    st.info("No Savings Goals.")

else:

    savings["Remaining"] = (
        savings["Target"]
        -
        savings["Current"]
    )

    st.dataframe(
        savings,
        use_container_width=True
    )

st.divider()

# ------------------------
# Financial Health
# ------------------------

st.header("📊 Financial Health")

score = 100

if not budget.empty and total_income > 0:

    ratio = spent / total_income

    if ratio > 1:
        score = 20

    elif ratio > 0.9:
        score = 40

    elif ratio > 0.75:
        score = 60

    elif ratio > 0.5:
        score = 80

st.metric(
    "Financial Health Score",
    f"{score}/100"
)

if score >= 80:

    st.success("Excellent")

elif score >= 60:

    st.info("Good")

elif score >= 40:

    st.warning("Needs Improvement")

else:

    st.error("Poor")

st.divider()

# ------------------------
# Download Reports
# ------------------------

st.header("⬇ Download Reports")

if not expenses.empty:

    st.download_button(
        "Download Expenses CSV",
        expenses.to_csv(index=False),
        "expenses_report.csv",
        "text/csv"
    )

if not budget.empty:

    st.download_button(
        "Download Budget CSV",
        budget.to_csv(index=False),
        "budget_report.csv",
        "text/csv"
    )

if not savings.empty:

    st.download_button(
        "Download Savings CSV",
        savings.to_csv(index=False),
        "savings_report.csv",
        "text/csv"
    )