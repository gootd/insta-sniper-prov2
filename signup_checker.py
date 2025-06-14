
import requests
import random

def is_username_available(username):
    session = requests.Session()
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
        ]),
        "X-IG-App-ID": "936619743392459",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "email": "test@example.com",
        "username": username,
        "first_name": "test",
        "opt_into_one_tap": False
    }

    try:
        response = session.post("https://www.instagram.com/accounts/web_create_ajax/attempt/", headers=headers, data=data)
        if response.status_code == 200 and ""username_suggestions"" in response.text:
            return True
    except Exception as e:
        print("Error:", e)
    return False
