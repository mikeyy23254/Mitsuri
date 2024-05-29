from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL

app = Flask(__name__)

# Set the port to the $PORT environment variable
port = int(os.environ.get('PORT', 5000))

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
