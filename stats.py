import calendar
from datetime import datetime
import pandas as pd

CSV_FILE = "data/history.csv"


def get_stats():
    df = pd.read_csv(CSV_FILE)

    df = df.sort_values("Date")

    today = df.iloc[-1]
    yesterday = df.iloc[-2] if len(df) > 1 else today

    current = today["Price"]
    previous = yesterday["Price"]

    change = current - previous

    grams = round(10000 / current, 4)

    now = datetime.now()

    last_day = calendar.monthrange(now.year, now.month)[1]
    days_left = last_day - now.day

    return {
        "date": today["Date"],
        "current": current,
        "previous": previous,
        "change": change,
        "grams": grams,
        "days_left": days_left,
    }