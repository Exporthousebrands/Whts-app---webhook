
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "exporthouse123"

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
    elif request.method == 'POST':
        print("Webhook triggered")
        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run()
