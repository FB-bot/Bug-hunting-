from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Alive ✅"

def start_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
