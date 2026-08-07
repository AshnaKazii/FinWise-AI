import streamlit as st

from utils.calculations import savings_goal
from utils.database import append_data, add_history
from utils.helpers import money

st.set_page_config(page_title="Savings Goal", page_icon="🎯")

st.title("🎯 Savings Goal Planner")

st.divider()

goal = st.number_input(
    "Target Amount (₹)",
    min_value=0.0,
    value=100000.0,
    step=1000.0
)

current = st.number_input(
    "Current Savings (₹)",
    min_value=0.0,
    value=10000.0,
    step=1000.0
)

monthly = st.number_input(
    "Monthly Savings (₹)",
    min_value=1.0,
    value=5000.0,
    step=500.0
)

if st.button("Calculate Goal"):

    months = savings_goal(
        goal,
        current,
        monthly
    )

    st.metric(
        "Months Required",
        months
    )

    st.metric(
        "Remaining Amount",
        money(goal-current)
    )

    progress = min(current/goal,1.0) if goal>0 else 0

    st.progress(progress)

    append_data(
        {
            "Goal":"Financial Goal",
            "Current":current,
            "Target":goal,
            "MonthlySaving":monthly
        },
        "savings.csv"
    )

    add_history(
        "Savings Goal",
        f"Goal={goal}, Months={months}"
    )