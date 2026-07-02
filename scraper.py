import requests
from bs4 import BeautifulSoup
from datetime import date

URL = "https://www.goodreturns.in/gold-rates/hyderabad.html"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}


def get_gold_rate():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the 22K gold price
    price = soup.find("span", id="22k-price")

    if price is None:
        raise Exception(
            "Couldn't find the 22K gold price. The website structure may have changed."
        )

    value = (
        price.text.strip()
        .replace("₹", "")
        .replace(",", "")
    )

    return {
        "date": date.today().strftime("%Y-%m-%d"),
        "price_per_gram": float(value)
    }


if __name__ == "__main__":
    data = get_gold_rate()
    print(data)
