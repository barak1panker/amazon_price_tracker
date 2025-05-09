


## 📄 `README.md`

```markdown
# 🛍️ Amazon Price Tracker

A simple Python project that monitors prices of multiple products on Amazon and sends you an email alert when any of them drops below your desired price.

---

## 📦 Features

- ✅ Track multiple Amazon products
- ✅ Define your target prices per product
- ✅ Automatic email alert when a product goes below your desired price
- ✅ Clean modular code structure

---

## 🗂️ Project Structure

```

price\_alert/
├── products.json         # List of products to track
├── price\_alert.py        # Main script to run the price check
├── scraper.py            # Module for scraping product prices
├── email\_alert.py        # Module for sending email notifications
├── .env                  # Contains email and SMTP credentials
└── README.md             # This file

````

---

## 📋 Requirements

- Python 3.7+
- Amazon product URLs
- SMTP email account (e.g., Gmail, Outlook)
- Internet access

---

## 🔧 Setup

### 1. Clone the repository or copy the files

```bash
git clone https://github.com/yourusername/price-alert.git
cd price-alert
````

### 2. Install dependencies

```bash
pip install beautifulsoup4 requests python-dotenv
```

### 3. Create a `.env` file

```env
SMTP_SERVER=smtp.example.com
MY_EMAIL=your_email@example.com
PASSWORD=your_email_password
```

*If you're using Gmail, you might need to generate an "App Password" instead of using your real one.*

---

## 🛒 Add Products

Edit the `products.json` file to include the URLs and target prices:

```json
[
    {
        "url": "https://www.amazon.com/dp/B092VJXGJ6",
        "max_price": 15.0
    },
    {
        "url": "https://www.amazon.com/dp/B07FZ8S74R",
        "max_price": 25.0
    }
]
```

---

## 🚀 Run the Tracker

```bash
python price_alert.py
```

You will see logs in your terminal and get an email alert if the current price is lower than your defined max.

---

## 🛑 Notes

* This script uses web scraping and might break if Amazon changes its page structure.
* Use it moderately to avoid being blocked.
* Make sure your email settings allow access by third-party apps (if using Gmail/Outlook).

---

