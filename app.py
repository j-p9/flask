from flask import Flask, request
import requests

app = Flask(__name__)

# Token et chat_id pour le bot de retransmission
TOKEN_RETRANSMISSION_BOT = '6012111885:AAECD2tq1UUSnghefem9p_BAUSQLQb4a3UM'
CHAT_ID_RETRANSMISSION = '-983438332'

def send_message_to_retransmission_bot(message):
    url = f'https://api.telegram.org/bot{TOKEN_RETRANSMISSION_BOT}/sendMessage'
    payload = {
        'chat_id': CHAT_ID_RETRANSMISSION,
        'text': message
    }
    requests.post(url, data=payload)

@app.route('/webhook_bot1', methods=['POST'])
def webhook_bot1():
    update = request.get_json()
    if 'message' in update:
        message = update['message']['text']
        send_message_to_retransmission_bot(f'Bot 1: {message}')
    return 'ok'

@app.route('/webhook_bot2', methods=['POST'])
def webhook_bot2():
    update = request.get_json()
    if 'message' in update:
        message = update['message']['text']
        send_message_to_retransmission_bot(f'Bot 2: {message}')
    return 'ok'

if __name__ == '__main__':
    app.run(port=8080)
