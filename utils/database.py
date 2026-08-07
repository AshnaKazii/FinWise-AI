import pandas as pd
import os
from datetime import datetime

DATA_FOLDER = "data"

FILES = {
    "expenses": "expenses.csv",
    "budget": "budget.csv",
    "history": "history.csv",
    "savings": "savings.csv"
}


def initialize_database():

    os.makedirs(DATA_FOLDER, exist_ok=True)

    defaults = {
        "expenses": ["Date", "Category", "Amount", "Description"],
        "budget": ["Month", "Income", "Budget", "Spent"],
        "history": ["Date", "Module", "Details"],
        "savings": ["Goal", "Current", "Target", "MonthlySaving"]
    }

    for key, filename in FILES.items():

        path = os.path.join(DATA_FOLDER, filename)

        if (not os.path.exists(path)) or os.path.getsize(path) == 0:

            pd.DataFrame(columns=defaults[key]).to_csv(
                path,
                index=False
            )


def load_data(filename):

    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        return pd.DataFrame()

    try:
        return pd.read_csv(path)

    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    except Exception:
        return pd.DataFrame()


def save_data(df, filename):

    path = os.path.join(DATA_FOLDER, filename)

    df.to_csv(path, index=False)


def append_data(row, filename):

    path = os.path.join(DATA_FOLDER, filename)

    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    df.to_csv(path, index=False)


def add_history(module, details):

    append_data(
        {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Module": module,
            "Details": details
        },
        FILES["history"]
    )