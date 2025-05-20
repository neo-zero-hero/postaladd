
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("372904251:mqpb3vHqA9Mn2F81APkLl92r3gJoZLbudACML5VL")
API_URL = f"https://tapi.bale.ai/bot{TOKEN}/"

def send_welcome_with_button(chat_id):
    data = {
        "chat_id": chat_id,
        "text": "سلام! به ربات خوش اومدی. 👇",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "ورود به سایت NCR",
                        "url": "http://ncr.ir"
                    }
                ]
            ]
        }
    }
    requests.post(API_URL + "sendMessage", json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        send_welcome_with_button(chat_id)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
