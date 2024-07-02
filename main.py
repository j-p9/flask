from flask import Flask, request
import telegram
import requests

# Tokens pour les bots à surveiller
TOKEN_BOT_1 = '7175360207:AAFJjC-Jxidd6wZTZRM0Z9WwIlPBj-HIjgs'
TOKEN_BOT_2 = '6141264696:AAExleZanVD6I6VLom5TP2M1zXhWO2qXeCM'

# Token et chat_id pour le bot de retransmission
TOKEN_RETRANSMISSION_BOT = '6012111885:AAECD2tq1UUSnghefem9p_BAUSQLQb4a3UM'
CHAT_ID_RETRANSMISSION = '-983438332'

# Bots
bot1 = telegram.Bot(token=TOKEN_BOT_1)
bot2 = telegram.Bot(token=TOKEN_BOT_2)
retransmission_bot = telegram.Bot(token=TOKEN_RETRANSMISSION_BOT)

app = Flask(__name__)

def send_message_to_retransmission_bot(message):
    url = f'https://api.telegram.org/bot{TOKEN_RETRANSMISSION_BOT}/sendMessage'
    payload = {
        'chat_id': CHAT_ID_RETRANSMISSION,
        'text': message
    }
    requests.post(url, data=payload)

@app.route('/webhook_bot1', methods=['POST'])
def webhook_bot1():
    update = telegram.Update.de_json(request.get_json(force=True), bot1)
    if update.message:
        message = update.message.text
        send_message_to_retransmission_bot(f'Bot 1: {message}')
    return 'ok'

@app.route('/webhook_bot2', methods=['POST'])
def webhook_bot2():
    update = telegram.Update.de_json(request.get_json(force=True), bot2)
    if update.message:
        message = update.message.text
        send_message_to_retransmission_bot(f'Bot 2: {message}')
    return 'ok'

if __name__ == '__main__':
    app.run(port=8443)
