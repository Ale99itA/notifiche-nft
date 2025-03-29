import os
import telebot
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Recupera i dati dalle variabili d'ambiente
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

bot = telebot.TeleBot(TOKEN)

@app.route('/api/send_nfc', methods=['GET'])
def send_nfc():
    # Ottieni il parametro 'device_id' dall'URL; se non presente, usa un valore di default
    device_id = request.args.get('device_id', 'Dispositivo sconosciuto')
    
    # Ottieni la data e l'ora correnti
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crea un messaggio personalizzato utilizzando il device_id
    message = f"{device_id} è arrivato sano e salvo alle {current_time} <3"
    
    # Invia il messaggio tramite il bot Telegram
    bot.send_message(CHAT_ID, message)
    
    # Rispondi "OK" alla richiesta (utile per il debug)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
