import streamlit as st
from utils.database import initialize_database, load_data
from utils.styles import load_css


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="FinWise AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_database()
load_css()


# -----------------------------
# LOAD DATA
# -----------------------------

expenses = load_data("expenses.csv")
budget = load_data("budget.csv")
history = load_data("history.csv")
savings = load_data("savings.csv")


# -----------------------------
# CALCULATIONS
# -----------------------------

total_income = 0
total_budget = 0
total_spent = 0
total_expenses = 0
total_goals = 0

if not budget.empty:

    if "Income" in budget.columns:
        total_income = budget["Income"].sum()

    if "Budget" in budget.columns:
        total_budget = budget["Budget"].sum()

    if "Spent" in budget.columns:
        total_spent = budget["Spent"].sum()


if not expenses.empty:

    if "Amount" in expenses.columns:
        total_expenses = expenses["Amount"].sum()


if not savings.empty:
    total_goals = len(savings)


remaining = total_income - total_spent


# -----------------------------
# HERO
# -----------------------------

st.markdown("""
# 💰 FinWise AI

### 🤖 LLM Powered Personal Financial Assistant

Manage Budgets • Analyze Expenses • Plan Investments • Get AI Financial Advice
""")


st.divider()


# -----------------------------
# KPI CARDS
# -----------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "💰 Income",
        f"₹{total_income:,.0f}"
    )


with c2:

    st.metric(
        "💸 Expenses",
        f"₹{total_expenses:,.0f}"
    )


with c3:

    st.metric(
        "🏦 Savings",
        f"₹{remaining:,.0f}"
    )


with c4:

    st.metric(
        "🎯 Goals",
        total_goals
    )


st.divider()


# -----------------------------
# QUICK ACTIONS
# -----------------------------

st.subheader("🚀 Available Modules")

col1, col2, col3 = st.columns(3)


with col1:

    st.success("""
    🤖 AI Financial Assistant

    Ask financial questions using GPT-OSS 20B.
    """)

    st.success("""
    💰 Budget Planner

    Create and manage monthly budgets.
    """)

    st.success("""
    📊 Expense Analyzer

    Track and visualize spending.
    """)


with col2:

    st.info("""
    📈 SIP Calculator

    Estimate investment growth.
    """)

    st.info("""
    🏦 EMI Calculator

    Calculate monthly loan payments.
    """)

    st.info("""
    🎯 Savings Planner

    Plan future financial goals.
    """)


with col3:

    st.warning("""
    📋 Reports

    Generate downloadable reports.
    """)

    st.warning("""
    📂 History Center

    View previous activities.
    """)

    st.warning("""
    📊 Dashboard

    Interactive financial insights.
    """)


st.divider()


# -----------------------------
# FINANCIAL OVERVIEW
# -----------------------------

st.subheader("📈 Financial Overview")

left, right = st.columns([2, 1])


with left:

    if total_budget > 0:

        progress = min(total_spent / total_budget, 1.0)

        st.progress(progress)

        st.caption(
            f"Budget Used : ₹{total_spent:,.0f} / ₹{total_budget:,.0f}"
        )

        if progress < 0.5:

            st.success(
                "Excellent! Your spending is well under budget."
            )

        elif progress < 0.8:

            st.info(
                "You're on track. Keep monitoring your expenses."
            )

        elif progress < 1:

            st.warning(
                "You're close to your budget limit."
            )

        else:

            st.error(
                "You've exceeded your budget."
            )

    else:

        st.info(
            "Create a budget to start tracking your finances."
        )


with right:

    score = 100

    if total_income > 0:

        ratio = total_expenses / total_income

        if ratio > 1:
            score = 20

        elif ratio > 0.9:
            score = 40

        elif ratio > 0.75:
            score = 60

        elif ratio > 0.5:
            score = 80


    st.metric(
        "📊 Financial Health",
        f"{score}/100"
    )


st.divider()


# -----------------------------
# SMART INSIGHTS
# -----------------------------

st.subheader("🧠 AI Financial Insights")


if expenses.empty:

    st.info(
        "Add some expenses to receive personalized financial insights."
    )

else:

    highest = (
        expenses.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    top_category = highest.index[0]
    top_amount = highest.iloc[0]

    average = expenses["Amount"].mean()

    col1, col2 = st.columns(2)


    with col1:

        st.success(
            f"🏆 Highest spending category: **{top_category}**"
        )

        st.write(
            f"Total spent: **₹{top_amount:,.0f}**"
        )

        st.write(
            f"Average expense: **₹{average:,.2f}**"
        )


    with col2:

        if total_income > 0:

            saving_rate = (
                max(total_income - total_expenses, 0)
                / total_income
            ) * 100

            st.metric(
                "💹 Saving Rate",
                f"{saving_rate:.1f}%"
            )

            if saving_rate >= 30:

                st.success(
                    "Excellent saving habits!"
                )

            elif saving_rate >= 20:

                st.info(
                    "Good saving habits."
                )

            else:

                st.warning(
                    "Consider reducing discretionary spending."
                )


st.divider()


# -----------------------------
# RECENT ACTIVITY
# -----------------------------

st.subheader("📜 Recent Activity")


if history.empty:

    st.info(
        "No recent activity found."
    )

else:

    st.dataframe(
        history.tail(5),
        use_container_width=True,
        hide_index=True
    )


st.divider()


# -----------------------------
# WHY FINWISE AI?
# -----------------------------

st.subheader("⭐ Why FinWise AI?")

c1, c2, c3 = st.columns(3)


with c1:

    st.markdown("""
    ### 🤖 AI Powered

    - GPT-OSS 20B
    - OpenRouter API
    - Personalized Advice
    - Natural Language Chat
    """)


with c2:

    st.markdown("""
    ### 📈 Smart Planning

    - Budget Planner
    - SIP Calculator
    - EMI Calculator
    - Savings Planner
    """)


with c3:

    st.markdown("""
    ### 📊 Powerful Analytics

    - Expense Dashboard
    - Reports
    - History Tracking
    - Interactive Charts
    """)


st.divider()


# -----------------------------
# PROJECT INFORMATION
# -----------------------------

left, right = st.columns([2, 1])


with left:

    st.subheader("🚀 About")

    st.write("""
    FinWise AI is an **LLM-Based Personal Financial Assistant**
    built using **Python, Streamlit, OpenRouter AI and GPT-OSS 20B**.

    It helps users:

    - 💰 Track expenses
    - 📊 Analyze spending
    - 🎯 Achieve savings goals
    - 📈 Estimate SIP returns
    - 🏦 Calculate loan EMIs
    - 🤖 Receive AI-powered financial guidance

    Everything is stored locally using CSV databases, making the
    application lightweight and easy to deploy.
    """)


with right:

    st.subheader("📌 Tech Stack")

    st.write("🐍 Python")
    st.write("🎈 Streamlit")
    st.write("🤖 OpenRouter AI")
    st.write("🧠 GPT OSS 20B")
    st.write("📊 Plotly")
    st.write("🐼 Pandas")
    st.write("📄 CSV Database")


st.divider()


# -----------------------------
# SIDEBAR INFO
# -----------------------------

with st.sidebar:

    st.title("💰 FinWise AI")

    st.caption("LLM Based Personal Financial Assistant")

    st.divider()

    st.metric(
        "Expenses",
        len(expenses)
    )

    st.metric(
        "Budgets",
        len(budget)
    )

    st.metric(
        "Goals",
        len(savings)
    )

    st.metric(
        "Activities",
        len(history)
    )

    st.divider()

    st.success("✅ Project Status")

    st.write("✔ AI Assistant")
    st.write("✔ Budget Planner")
    st.write("✔ Expense Analyzer")
    st.write("✔ Dashboard")
    st.write("✔ SIP Calculator")
    st.write("✔ EMI Calculator")
    st.write("✔ Savings Planner")
    st.write("✔ Reports")
    st.write("✔ History")

    st.divider()

    st.info("👈 Select a module from the sidebar to begin.")


st.divider()


# -----------------------------
# FOOTER
# -----------------------------

st.markdown("""
### 💰 FinWise AI

**An LLM-Based Personal Financial Assistant**

Built using **Python • Streamlit • OpenRouter • GPT OSS 20B • Plotly**

© 2026 FinWise AI | Developed by Ashna Kazi
""")