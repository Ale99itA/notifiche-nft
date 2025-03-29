import telebot
from flask import Flask, request

TOKEN = "TUO_TOKEN"
CHAT_ID = "987654321"  # ID del gruppo o della persona che riceverà la notifica
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/send_nfc', methods=['GET'])
def send_nfc():
    user_agent = request.headers.get('User-Agent')
    bot.send_message(CHAT_ID, f"Un dispositivo ({user_agent}) ha scansionato il Tag NFC!")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
