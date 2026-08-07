import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def pie_chart(df):

    if df.empty:
        return go.Figure()

    fig = px.pie(
        df,
        values="Amount",
        names="Category",
        hole=0.45,
        title="Expense Distribution"
    )

    fig.update_layout(template="plotly_dark")

    return fig


def bar_chart(df):

    if df.empty:
        return go.Figure()

    grouped = df.groupby("Category")["Amount"].sum().reset_index()

    fig = px.bar(
        grouped,
        x="Category",
        y="Amount",
        color="Category",
        title="Expenses by Category"
    )

    fig.update_layout(template="plotly_dark")

    return fig


def line_chart(df):

    if df.empty:
        return go.Figure()

    df["Date"] = pd.to_datetime(df["Date"])

    monthly = df.groupby("Date")["Amount"].sum().reset_index()

    fig = px.line(
        monthly,
        x="Date",
        y="Amount",
        markers=True,
        title="Expense Trend"
    )

    fig.update_layout(template="plotly_dark")

    return fig