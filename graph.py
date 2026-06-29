import os
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/history.csv"
GRAPH_FILE = "graphs/gold_rate_trend.png"


def generate_graph():
    """
    Generates a polished graph of the last 30 days of gold prices.
    """

    if not os.path.exists(CSV_FILE):
        print("No history file found.")
        return

    df = pd.read_csv(CSV_FILE)

    if df.empty:
        print("History is empty.")
        return

    df = df.tail(30).reset_index(drop=True)

    os.makedirs("graphs", exist_ok=True)

    # Find important points
    highest = df["Price"].idxmax()
    lowest = df["Price"].idxmin()
    today = len(df) - 1

    plt.figure(figsize=(12, 6))

    # Main trend line
    plt.plot(
        df["Date"],
        df["Price"],
        color="#4A90E2",
        linewidth=2.5,
        marker="o",
        markersize=5,
        label="22K Gold"
    )

    # Highest Price (Red)
    plt.scatter(
        df.loc[highest, "Date"],
        df.loc[highest, "Price"],
        color="red",
        s=140,
        zorder=5,
        label="Highest"
    )

    # Lowest Price (Green)
    plt.scatter(
        df.loc[lowest, "Date"],
        df.loc[lowest, "Price"],
        color="green",
        s=140,
        zorder=5,
        label="Lowest"
    )

    # Today's Price (Gold)
    plt.scatter(
        df.loc[today, "Date"],
        df.loc[today, "Price"],
        color="gold",
        edgecolor="black",
        linewidth=1,
        s=180,
        zorder=6,
        label="Today"
    )

    # Labels
    plt.text(
        df.loc[highest, "Date"],
        df.loc[highest, "Price"] + 30,
        f"₹{df.loc[highest, 'Price']:,.0f}",
        ha="center",
        fontsize=9,
        color="red"
    )

    plt.text(
        df.loc[lowest, "Date"],
        df.loc[lowest, "Price"] - 55,
        f"₹{df.loc[lowest, 'Price']:,.0f}",
        ha="center",
        fontsize=9,
        color="green"
    )

    plt.text(
        df.loc[today, "Date"],
        df.loc[today, "Price"] + 55,
        f"₹{df.loc[today, 'Price']:,.0f}",
        ha="center",
        fontsize=9,
        fontweight="bold",
        color="#B8860B"
    )

    plt.title(
        "22K Gold Price Trend (Last 30 Days)",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Date")
    plt.ylabel("Price (₹ / gram)")

    plt.xticks(rotation=45)

    plt.grid(
        linestyle="--",
        linewidth=0.5,
        alpha=0.5
    )

    plt.legend()

    # Clean look
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(GRAPH_FILE, dpi=300)
    plt.close()

    print(f"Graph saved to {GRAPH_FILE}")