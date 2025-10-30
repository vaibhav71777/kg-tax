from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

# Create Flask app
app = Flask(__name__, static_folder="static")
CORS(app)

# ---------- FRONTEND ----------
@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def serve_frontend(path):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    if path != "" and os.path.exists(os.path.join(static_dir, path)):
        return send_from_directory(static_dir, path)
    else:
        return send_from_directory(static_dir, 'index.html')

# ---------- BACKEND ----------
@app.route("/api")
def home():
    return jsonify({"message": "Welcome to Project KG Prototype — Backend is live!"})

# ---------- RUN ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
