
from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "exporthouse123"
ACCESS_TOKEN = "EAAlZCqkmWexoBOw7Xaa4ZA0CtBygvhWcmaVvpLEY9xqI8CKSrJFy9HaI6mkcaGVKZCDppMBZBntz0WN984LTxm6QotIM7NAZBJFb760ahhOUUmspgqJw6LMz0zbTHfaiD5SuZBYcbopstO4OtXo89ZAZB9Cc0dPSh8KZCebek3Ww6m1FXbK7MnB5KEyjh6opY80zzBF7k8QVGmppuVoAGMLZCeg7ELEgApRmUoW6N3PTpe3F8ZD"
PHONE_NUMBER_ID = "583152571555105"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verification failed', 403

    if request.method == 'POST':
        data = request.json
        try:
            phone_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
            send_auto_reply(phone_number)
        except Exception as e:
            print("Error:", e)
        return 'EVENT_RECEIVED', 200

def send_auto_reply(to_number):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {
            "body": "👋 Thanks for messaging Export House! We'll get back to you shortly."
        }
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print("Reply sent:", response.text)

if __name__ == '__main__':
    app.run()
