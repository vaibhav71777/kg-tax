import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Project KG Prototype — Backend is live!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Railway assigns a dynamic port
    app.run(host='0.0.0.0', port=port)
