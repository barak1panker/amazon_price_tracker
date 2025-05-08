import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SMTP = os.getenv("SMTP_SERVER")
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_email(price, url):
    subject = "Price Drop Alert!"
    body = f"The product is now ${price}!\nBuy here: {url}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(SMTP, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=message.encode("utf-8")
        )
