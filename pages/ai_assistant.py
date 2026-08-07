import streamlit as st
from utils.ai import ask_ai
from utils.database import load_data, add_history

st.set_page_config(
    page_title="AI Financial Assistant",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------
# LOAD DATA
# ----------------------------------------

expenses = load_data("expenses.csv")
budget = load_data("budget.csv")
savings = load_data("savings.csv")

# ----------------------------------------
# SESSION STATE
# ----------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# ----------------------------------------
# HEADER
# ----------------------------------------

st.title("🤖 AI Financial Assistant")

st.caption(
    "Powered by OpenRouter • GPT OSS 20B"
)

st.divider()

# ----------------------------------------
# HERO
# ----------------------------------------

left, right = st.columns([3,1])

with left:

    st.markdown("""
### Ask Anything About Personal Finance

Examples:

- 💰 Budget Planning
- 📊 Expense Analysis
- 📈 SIP Investments
- 🏦 EMI Calculations
- 🎯 Savings Goals
- 💳 Money Management
- 📉 Financial Planning
""")

with right:

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

st.divider()

# ----------------------------------------
# QUICK PROMPTS
# ----------------------------------------

st.subheader("⚡ Quick Questions")

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("💸 Reduce my expenses"):
        st.session_state.prompt = "Analyze my expenses and tell me how to reduce unnecessary spending."

    if st.button("📊 Analyze my spending"):
        st.session_state.prompt = "Analyze all my financial data."

with c2:

    if st.button("📈 SIP Advice"):
        st.session_state.prompt = "Suggest the best SIP strategy for me."

    if st.button("🏦 Loan Advice"):
        st.session_state.prompt = "Should I prepay my loan?"

with c3:

    if st.button("🎯 Savings Plan"):
        st.session_state.prompt = "Help me achieve my savings goal."

    if st.button("💰 Monthly Budget"):
        st.session_state.prompt = "Create an ideal monthly budget."

st.divider()

# ----------------------------------------
# CHAT HISTORY
# ----------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])
# ----------------------------------------
# USER INPUT
# ----------------------------------------

default_prompt = st.session_state.get("prompt", "")

prompt = st.chat_input(
    "Ask FinWise AI anything about your finances..."
)

if default_prompt and not prompt:
    prompt = default_prompt
    st.session_state.prompt = ""

# ----------------------------------------
# AI CHAT
# ----------------------------------------

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ----------------------------------------
    # Build Financial Context
    # ----------------------------------------

    financial_context = f"""

You are FinWise AI, an expert personal financial advisor.

The following is the user's financial information.

========== BUDGET ==========
{budget.to_string(index=False)}

========== EXPENSES ==========
{expenses.to_string(index=False)}

========== SAVINGS ==========
{savings.to_string(index=False)}

Instructions:

1. Analyze the user's financial data whenever available.

2. Give practical financial advice.

3. Use bullet points whenever possible.

4. If expenses seem high, recommend areas to reduce spending.

5. If savings are low, suggest achievable saving strategies.

6. If investment related, explain SIPs in simple language.

7. Never mention that you're an AI model.

8. Keep answers beginner friendly.

"""

    final_prompt = financial_context + f"""

User Question:

{prompt}

"""

    with st.chat_message("assistant"):

        with st.spinner("🧠 Thinking..."):

            response = ask_ai(final_prompt)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    add_history(
        "AI Assistant",
        prompt
    )

st.divider()

# ----------------------------------------
# FINANCIAL SNAPSHOT
# ----------------------------------------

st.subheader("📊 Current Financial Snapshot")

col1, col2, col3 = st.columns(3)

total_expense = 0

if not expenses.empty and "Amount" in expenses.columns:
    total_expense = expenses["Amount"].sum()

total_income = 0

if not budget.empty and "Income" in budget.columns:
    total_income = budget["Income"].sum()

remaining = total_income - total_expense

with col1:

    st.metric(
        "Income",
        f"₹{total_income:,.0f}"
    )

with col2:

    st.metric(
        "Expenses",
        f"₹{total_expense:,.0f}"
    )

with col3:

    st.metric(
        "Savings",
        f"₹{remaining:,.0f}"
    )

st.divider()

# ----------------------------------------
# AI FINANCIAL TIPS
# ----------------------------------------

st.subheader("💡 Daily Financial Tips")

tips = [
    "💰 Follow the 50-30-20 budgeting rule whenever possible.",
    "📈 Invest consistently instead of trying to time the market.",
    "🏦 Build an emergency fund covering at least 6 months of expenses.",
    "💳 Avoid paying only the minimum amount on credit cards.",
    "📊 Review your monthly spending before creating a new budget.",
    "🎯 Track your savings goals every month.",
    "📉 Reduce impulse purchases by waiting 24 hours before buying.",
    "💵 Increase your SIP amount whenever your income increases."
]

tip_index = (
    len(expenses)
    + len(budget)
    + len(savings)
) % len(tips)

st.success(tips[tip_index])

st.divider()

# ----------------------------------------
# SIDEBAR
# ----------------------------------------

with st.sidebar:

    st.title("🤖 FinWise AI")

    st.caption("Personal Financial Assistant")

    st.divider()

    st.subheader("📊 Dataset")

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
        "Messages",
        len(st.session_state.messages)
    )

    st.divider()

    st.subheader("⚙ Chat")

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []
        st.session_state.prompt = ""

        st.rerun()

    st.divider()

    st.subheader("🚀 Suggested Questions")

    st.write("• Analyze my expenses")
    st.write("• Where can I save money?")
    st.write("• Create a monthly budget")
    st.write("• Explain SIP investment")
    st.write("• How much should I save?")
    st.write("• Should I prepay my loan?")
    st.write("• Give investment suggestions")

    st.divider()

    st.success("Model: GPT OSS 20B")

    st.caption("Powered by OpenRouter")

# ----------------------------------------
# FOOTER
# ----------------------------------------

st.divider()

st.caption(
    "💰 FinWise AI • AI Powered Personal Financial Assistant • Streamlit + OpenRouter + GPT OSS 20B"
)