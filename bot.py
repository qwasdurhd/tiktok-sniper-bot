import requests
import time
import random

# Telegram bot credentials
bot_token = '7522391832:AAG5LvTq1psG7KelaHM5oZosr_Vi3A3cxW8'
chat_id = '-4904445921'

# Username generator
def generate_username():
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    pos = random.choice([1, 2])
    name = ''.join(random.choices(characters, k=3))
    return name[:pos] + '.' + name[pos:]

# Check TikTok availability
def is_available(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        return "Couldn't find this account" in response.text or response.status_code == 404
    except:
        return False

# Start sniping
while True:
    user = generate_username()
    if is_available(user):
        message = f"✅ AVAILABLE: @{user}"
        print(message)
        requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            data={'chat_id': chat_id, 'text': message}
        )
    else:
        print(f"❌ TAKEN: @{user}")
    time.sleep(0.1)
