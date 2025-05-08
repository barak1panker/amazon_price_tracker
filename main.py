import json
from scraper import get_price
from email_alert import send_email

with open("products.json", "r") as file:
    products = json.load(file)

for product in products:
    url = product["url"]
    max_price = product["max_price"]
    current_price = get_price(url)

    if current_price is None:
        print(f"Could not retrieve price for: {url}")
        continue

    print(f"Current price for {url} is ${current_price}")

    if current_price < max_price:
        print("Price is low enough! Sending email...")
        send_email(current_price, url)
    else:
        print("Price is too high.\n")
