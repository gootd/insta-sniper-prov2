
import requests
import json

with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config["bot_token"]
CHAT_ID = config["chat_id"]

def send_to_telegram(username):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"🎯 متاح للتسجيل: @{username}"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("فشل الإرسال:", e)
