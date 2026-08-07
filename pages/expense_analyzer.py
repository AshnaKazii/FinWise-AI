import streamlit as st
import pandas as pd
from datetime import date

from utils.database import load_data, save_data, append_data, add_history
from utils.helpers import money
from utils.charts import pie_chart, bar_chart, line_chart

st.set_page_config(
    page_title="Expense Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Expense Analyzer")

st.divider()

TAB1, TAB2, TAB3 = st.tabs(
    ["➕ Add Expense", "📂 Upload CSV", "📈 Analytics"]
)

# ------------------------
# TAB 1
# ------------------------

with TAB1:

    st.subheader("Add New Expense")

    col1, col2 = st.columns(2)

    with col1:

        expense_date = st.date_input(
            "Date",
            value=date.today()
        )

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Transport",
                "Shopping",
                "Bills",
                "Healthcare",
                "Entertainment",
                "Education",
                "Investment",
                "Others"
            ]
        )

    with col2:

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=100.0
        )

        description = st.text_input(
            "Description"
        )

    if st.button("Save Expense"):

        append_data(
            {
                "Date": expense_date,
                "Category": category,
                "Amount": amount,
                "Description": description
            },
            "expenses.csv"
        )

        add_history(
            "Expense Added",
            f"{category} - ₹{amount}"
        )

        st.success("Expense Added Successfully!")

# ------------------------
# TAB 2
# ------------------------

with TAB2:

    st.subheader("Upload Expense CSV")

    uploaded = st.file_uploader(
        "Choose CSV File",
        type="csv"
    )

    if uploaded is not None:

        df = pd.read_csv(uploaded)

        save_data(
            df,
            "expenses.csv"
        )

        st.success("CSV Uploaded Successfully!")

        st.dataframe(
            df,
            use_container_width=True
        )

# ------------------------
# TAB 3
# ------------------------

with TAB3:

    df = load_data("expenses.csv")

    if df.empty:

        st.info("No Expenses Found")

    else:

        st.subheader("Expense Data")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.plotly_chart(
                pie_chart(df),
                use_container_width=True
            )

        with c2:

            st.plotly_chart(
                bar_chart(df),
                use_container_width=True
            )

        st.plotly_chart(
            line_chart(df),
            use_container_width=True
        )

        st.divider()

        st.subheader("Summary")

        total = df["Amount"].sum()

        average = df["Amount"].mean()

        highest = df["Amount"].max()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Expense",
            money(total)
        )

        c2.metric(
            "Average Expense",
            money(average)
        )

        c3.metric(
            "Highest Expense",
            money(highest)
        )

        st.download_button(
            "⬇ Download CSV",
            df.to_csv(index=False),
            file_name="expenses.csv",
            mime="text/csv"
        )