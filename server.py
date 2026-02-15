from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

latest_data = {
    "deviceId": "NONE",
    "hr": 0,
    "rr": 0,
    "status": "NO DATA",
    "time": ""
}

@app.route("/")
def home():
    return "✅ HLK Cloud Server Running"

@app.route("/api/vitals", methods=["POST"])
def vitals():
    global latest_data

    data = request.get_json(force=True)

    latest_data["deviceId"] = data.get("deviceId", "ESP32_01")
    latest_data["hr"] = int(data.get("hr", 0))
    latest_data["rr"] = int(data.get("rr", 0))
    latest_data["status"] = data.get("status", "NORMAL")
    latest_data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("📥 Received:", latest_data)

    return jsonify({"message": "OK", "received": latest_data})

@app.route("/api/latest", methods=["GET"])
def latest():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
