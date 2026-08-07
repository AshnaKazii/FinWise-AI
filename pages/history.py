import streamlit as st
import pandas as pd

from utils.database import load_data

st.set_page_config(
    page_title="History",
    page_icon="📂",
    layout="wide"
)

st.title("📂 History Center")

st.divider()

history = load_data("history.csv")
expenses = load_data("expenses.csv")
budget = load_data("budget.csv")
savings = load_data("savings.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📜 Activity",
        "💰 Budget",
        "📊 Expenses",
        "🎯 Savings"
    ]
)

# ----------------------------------------------------

with tab1:

    st.subheader("Activity History")

    if history.empty:

        st.info("No Activity Found.")

    else:

        search = st.text_input(
            "Search Activity"
        )

        df = history.copy()

        if search:

            df = df[
                df.astype(str)
                .apply(
                    lambda x:
                    x.str.contains(
                        search,
                        case=False
                    )
                )
                .any(axis=1)
            ]

        st.dataframe(
            df,
            use_container_width=True
        )

        st.download_button(
            "Download Activity",
            df.to_csv(index=False),
            "activity_history.csv",
            "text/csv"
        )

# ----------------------------------------------------

with tab2:

    st.subheader("Budget History")

    if budget.empty:

        st.info("No Budget Records.")

    else:

        st.dataframe(
            budget,
            use_container_width=True
        )

        st.download_button(
            "Download Budget",
            budget.to_csv(index=False),
            "budget.csv",
            "text/csv"
        )

# ----------------------------------------------------

with tab3:

    st.subheader("Expense History")

    if expenses.empty:

        st.info("No Expense Records.")

    else:

        st.dataframe(
            expenses,
            use_container_width=True
        )

        st.download_button(
            "Download Expenses",
            expenses.to_csv(index=False),
            "expenses.csv",
            "text/csv"
        )

# ----------------------------------------------------

with tab4:

    st.subheader("Savings Goals")

    if savings.empty:

        st.info("No Savings Goals.")

    else:

        st.dataframe(
            savings,
            use_container_width=True
        )

        st.download_button(
            "Download Savings",
            savings.to_csv(index=False),
            "savings.csv",
            "text/csv"
        )

st.divider()

st.subheader("Danger Zone")

if st.button("🗑 Clear Activity History"):

    pd.DataFrame(
        columns=[
            "Date",
            "Module",
            "Details"
        ]
    ).to_csv(
        "data/history.csv",
        index=False
    )

    st.success(
        "History Cleared Successfully."
    )

    st.rerun()