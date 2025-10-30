from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api')
def home():
    return {"message": "Welcome to Project KG Prototype — Backend is live!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
