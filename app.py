from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "RADZ API",
        "creator": "RADO",
        "status": "ONLINE"
    })

@app.route("/api/data")
def data():
    return jsonify({
        "success": True,
        "message": "RADZ API berhasil!"
    })

@app.route("/api/send", methods=["POST"])
def send():
    data = request.get_json(silent=True) or {}
    return jsonify({"success": True, "received": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
