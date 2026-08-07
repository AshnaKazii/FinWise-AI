import streamlit as st


def page_header(title, emoji):

    st.title(f"{emoji} {title}")

    st.divider()


def success(message):

    st.success(message)


def warning(message):

    st.warning(message)


def info(message):

    st.info(message)


def metric(label, value):

    st.metric(label, value)


def money(amount):

    return f"₹ {amount:,.2f}"