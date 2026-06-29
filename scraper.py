import requests
from bs4 import BeautifulSoup
from datetime import date

URL = "https://www.goodreturns.in/gold-rates/hyderabad.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_gold_rate():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    label = soup.find(
        "span",
        class_="label",
        string=lambda s: s and "22k Gold" in s
    )

    value = label.find_next("span", class_="value").text.strip()

    value = (
        value.replace("₹", "")
             .replace("/gm", "")
             .replace(",", "")
             .strip()
    )

    return {
        "date": date.today().strftime("%Y-%m-%d"),
        "price_per_gram": float(value)
    }


if __name__ == "__main__":
    data = get_gold_rate()

    print(data)