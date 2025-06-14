
import threading
import http.server
import socketserver
from username_generator import generate_all_usernames
from signup_checker import is_username_available
from telegram_bot import send_to_telegram

def run_fake_server():
    PORT = 10000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

# تشغيل الخادم الوهمي
threading.Thread(target=run_fake_server, daemon=True).start()

print("🚀 Insta Sniper Pro v4 - Full Mode Activated")

usernames = generate_all_usernames()
for username in usernames:
    print(f"🔎 Checking: {username}")
    if is_username_available(username):
        print(f"✅ Available: {username}")
        send_to_telegram(username)
