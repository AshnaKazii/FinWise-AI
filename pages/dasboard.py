import streamlit as st
import pandas as pd

from utils.database import load_data
from utils.helpers import money
from utils.charts import pie_chart, bar_chart, line_chart

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Dashboard")

st.caption("Track your finances with real-time insights")

st.divider()

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

expenses = load_data("expenses.csv")
budget = load_data("budget.csv")
history = load_data("history.csv")
savings = load_data("savings.csv")

# --------------------------------------------------
# CALCULATIONS
# --------------------------------------------------

total_income = 0
total_budget = 0
budget_spent = 0
expense_total = 0

if not budget.empty:

    if "Income" in budget.columns:
        total_income = budget["Income"].sum()

    if "Budget" in budget.columns:
        total_budget = budget["Budget"].sum()

    if "Spent" in budget.columns:
        budget_spent = budget["Spent"].sum()

if not expenses.empty:

    if "Amount" in expenses.columns:
        expense_total = expenses["Amount"].sum()

remaining = total_income - budget_spent

budget_percent = 0

if total_budget > 0:
    budget_percent = (budget_spent / total_budget) * 100

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "💰 Income",
        money(total_income)
    )

with k2:
    st.metric(
        "💸 Expenses",
        money(expense_total)
    )

with k3:
    st.metric(
        "🏦 Savings",
        money(remaining)
    )

with k4:
    st.metric(
        "🎯 Budget Used",
        f"{budget_percent:.1f}%"
    )

st.divider()

# --------------------------------------------------
# BUDGET STATUS
# --------------------------------------------------

st.subheader("💰 Budget Utilization")

if total_budget > 0:

    progress = min(budget_percent / 100, 1.0)

    st.progress(progress)

    left, right = st.columns([3,1])

    with left:

        st.write(
            f"Spent **{money(budget_spent)}** out of **{money(total_budget)}**"
        )

    with right:

        st.metric(
            "Remaining",
            money(total_budget-budget_spent)
        )

else:

    st.info("No budget available.")

st.divider()

# --------------------------------------------------
# CHARTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🥧 Expense Distribution")

    if expenses.empty:

        st.info("No expense records.")

    else:

        st.plotly_chart(
            pie_chart(expenses),
            use_container_width=True
        )

with right:

    st.subheader("📊 Category Analysis")

    if expenses.empty:

        st.info("No expense records.")

    else:

        st.plotly_chart(
            bar_chart(expenses),
            use_container_width=True
        )

st.divider()
# --------------------------------------------------
# MONTHLY EXPENSE TREND
# --------------------------------------------------

st.subheader("📈 Expense Trend")

if expenses.empty:

    st.info("No expense data available.")

else:

    try:

        expenses["Date"] = pd.to_datetime(expenses["Date"])

        trend = (
            expenses
            .groupby("Date")["Amount"]
            .sum()
            .reset_index()
        )

        st.plotly_chart(
            line_chart(trend),
            use_container_width=True
        )

    except Exception:

        st.info("Unable to generate trend chart.")

st.divider()

# --------------------------------------------------
# TOP SPENDING CATEGORIES
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("🏆 Top Spending Categories")

    if expenses.empty:

        st.info("No expenses available.")

    else:

        top = (
            expenses
            .groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        st.dataframe(
            top,
            use_container_width=True,
            hide_index=True
        )

with right:

    st.subheader("💡 Spending Insights")

    if expenses.empty:

        st.info("No insights available.")

    else:

        highest = top.iloc[0]

        average = expenses["Amount"].mean()

        st.success(
            f"Highest spending category: **{highest['Category']}**"
        )

        st.write(
            f"Amount Spent: **{money(highest['Amount'])}**"
        )

        st.write(
            f"Average Transaction: **{money(average)}**"
        )

        if total_income > 0:

            saving_rate = (
                max(total_income - expense_total, 0)
                / total_income
            ) * 100

            st.metric(
                "Saving Rate",
                f"{saving_rate:.1f}%"
            )

            if saving_rate >= 30:

                st.success("Excellent saving habit.")

            elif saving_rate >= 20:

                st.info("Good financial discipline.")

            else:

                st.warning(
                    "Reduce discretionary spending."
                )

st.divider()

# --------------------------------------------------
# BUDGET TABLE
# --------------------------------------------------

st.subheader("📋 Budget Summary")

if budget.empty:

    st.info("No budget records found.")

else:

    budget_view = budget.copy()

    if (
        "Budget" in budget_view.columns
        and "Spent" in budget_view.columns
    ):

        budget_view["Remaining"] = (
            budget_view["Budget"]
            -
            budget_view["Spent"]
        )

    st.dataframe(
        budget_view,
        use_container_width=True,
        hide_index=True
    )

st.divider()
# --------------------------------------------------
# SAVINGS GOALS
# --------------------------------------------------

st.subheader("🎯 Savings Goals")

if savings.empty:

    st.info("No savings goals found.")

else:

    savings_view = savings.copy()

    if (
        "Target" in savings_view.columns
        and "Current" in savings_view.columns
    ):

        savings_view["Remaining"] = (
            savings_view["Target"]
            -
            savings_view["Current"]
        )

        savings_view["Progress (%)"] = (
            (
                savings_view["Current"]
                /
                savings_view["Target"]
            ) * 100
        ).round(1)

    st.dataframe(
        savings_view,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# --------------------------------------------------
# RECENT EXPENSES
# --------------------------------------------------

left, right = st.columns([3,2])

with left:

    st.subheader("🧾 Recent Expenses")

    if expenses.empty:

        st.info("No expense records.")

    else:

        latest = expenses.sort_values(
            "Date",
            ascending=False
        ).head(10)

        st.dataframe(
            latest,
            use_container_width=True,
            hide_index=True
        )

with right:

    st.subheader("📜 Recent Activity")

    if history.empty:

        st.info("No activity available.")

    else:

        st.dataframe(
            history.tail(10),
            use_container_width=True,
            hide_index=True
        )

st.divider()

# --------------------------------------------------
# FINANCIAL HEALTH
# --------------------------------------------------

st.subheader("💚 Financial Health")

score = 100

if total_income > 0:

    ratio = expense_total / total_income

    if ratio > 1:

        score = 20

    elif ratio > 0.90:

        score = 40

    elif ratio > 0.75:

        score = 60

    elif ratio > 0.50:

        score = 80

health1, health2 = st.columns([1,3])

with health1:

    st.metric(
        "Health Score",
        f"{score}/100"
    )

with health2:

    if score >= 80:

        st.success(
            "Excellent! Your finances are in great shape."
        )

    elif score >= 60:

        st.info(
            "Good. Keep monitoring your monthly spending."
        )

    elif score >= 40:

        st.warning(
            "You should reduce unnecessary expenses."
        )

    else:

        st.error(
            "Your expenses are very high compared to your income."
        )

st.divider()
# --------------------------------------------------
# AI RECOMMENDATIONS
# --------------------------------------------------

st.subheader("🤖 AI Financial Recommendations")

if expenses.empty and budget.empty:

    st.info("Start using FinWise AI to receive personalized recommendations.")

else:

    recommendations = []

    if total_income > 0:

        expense_ratio = expense_total / total_income

        if expense_ratio > 0.80:
            recommendations.append(
                "⚠️ Your expenses are above 80% of your income. Consider reducing discretionary spending."
            )

        elif expense_ratio > 0.60:
            recommendations.append(
                "💡 Your spending is moderate. Try increasing your monthly savings."
            )

        else:
            recommendations.append(
                "✅ Great! Your spending is under control."
            )

    if not expenses.empty:

        category_total = (
            expenses.groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        top_category = category_total.index[0]
        top_amount = category_total.iloc[0]

        recommendations.append(
            f"🏆 Highest spending category: **{top_category}** ({money(top_amount)})."
        )

    if not savings.empty:

        recommendations.append(
            f"🎯 You currently have **{len(savings)}** active savings goal(s). Keep contributing every month."
        )

    for rec in recommendations:
        st.success(rec)

st.divider()

# --------------------------------------------------
# QUICK STATISTICS
# --------------------------------------------------

st.subheader("📌 Quick Statistics")

s1, s2, s3, s4 = st.columns(4)

s1.metric(
    "Transactions",
    len(expenses)
)

s2.metric(
    "Budgets",
    len(budget)
)

s3.metric(
    "Savings Goals",
    len(savings)
)

s4.metric(
    "Activities",
    len(history)
)

st.divider()

# --------------------------------------------------
# OVERALL SUMMARY
# --------------------------------------------------

st.subheader("📊 Overall Summary")

summary = {
    "Metric": [
        "Total Income",
        "Total Expenses",
        "Budget Allocated",
        "Budget Spent",
        "Remaining Savings"
    ],
    "Value": [
        money(total_income),
        money(expense_total),
        money(total_budget),
        money(budget_spent),
        money(remaining)
    ]
}

summary_df = pd.DataFrame(summary)

st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "💰 FinWise AI Dashboard • Real-time Financial Insights • Powered by Streamlit + Plotly"
)