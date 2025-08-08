import feedparser
import requests
import os

RSS_URL = os.getenv("RSS_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Parse RSS feed
feed = feedparser.parse(RSS_URL)
if feed.entries:
    latest = feed.entries[0]
    title = latest.title
    link = latest.link
    message = f"{title}\n{link}"

    # Send to Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHANNEL_ID, "text": message})
