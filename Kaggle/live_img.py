from flask import Flask
app = Flask(__name__)

@app.route('/')

def liveImg():
    return 'The server is intended to host images online'