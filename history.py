import os
import pandas as pd

CSV_FILE = "data/history.csv"


def save_rate(data):
    """
    Saves today's gold rate to history.csv.
    If today's date already exists, updates the price.
    """

    # Create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=["Date", "Price"])

    # Check if today's date already exists
    if data["date"] in df["Date"].values:
        df.loc[df["Date"] == data["date"], "Price"] = data["price_per_gram"]
    else:
        df.loc[len(df)] = [data["date"], data["price_per_gram"]]

    # Sort by date
    df = df.sort_values("Date")

    df.to_csv(CSV_FILE, index=False)

    return df