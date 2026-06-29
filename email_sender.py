import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
import os

from email_template import create_email_html


load_dotenv()


def send_email(stats):

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")


    html_content = create_email_html(stats)

    msg = EmailMessage()

    msg["Subject"] = f"🪙 Daily Gold Report - {stats['date']}"
    msg["From"] = sender_email
    msg["To"] = receiver_email


    msg.set_content(
        f"""
Daily Gold Report

Date: {stats['date']}
Gold Rate: ₹{stats['current']:,.0f}/g
Change: ₹{stats['change']:,.0f}
₹10,000 buys: {stats['grams']}g
"""
    )


    msg.add_alternative(
        html_content,
        subtype="html"
    )


    graph_path = Path("graphs/gold_rate_trend.png")

    print(graph_path.exists())

    if graph_path.exists():

        with open(graph_path, "rb") as img:

            image_data = img.read()

            html_part = msg.get_payload()[1]

            html_part.add_related(
                image_data,
                maintype="image",
                subtype="png",
                cid="gold_graph"
            )


    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(
            sender_email,
            sender_password
        )

        server.send_message(msg)


    print("Email sent successfully ✅")