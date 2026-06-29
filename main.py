from scraper import get_gold_rate
from history import save_rate
from graph import generate_graph
from stats import get_stats
from email_sender import send_email


def main():
    data = get_gold_rate()

    save_rate(data)

    generate_graph()

    stats = get_stats()

    send_email(stats)

    print("\nDaily Report\n")

    print(f"Date       : {stats['date']}")
    print(f"Gold Rate  : ₹{stats['current']:,.0f}/g")

    if stats["change"] > 0:
        print(f"Change     : ↑ ₹{abs(stats['change']):,.0f}")
    elif stats["change"] < 0:
        print(f"Change     : ↓ ₹{abs(stats['change']):,.0f}")
    else:
        print("Change     : No Change")

    print(f"₹10,000 = {stats['grams']} g")
    print(f"Days Left  : {stats['days_left']}")


if __name__ == "__main__":
    main()