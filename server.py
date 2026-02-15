from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

latest_data = {
    "hr": 0,
    "rr": 0,
    "status": "NO DATA",
    "time": ""
}

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>HLK Vital Monitor</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body { font-family: Arial; background: #111; color: white; text-align: center; }
        .box { background: #222; margin: 15px; padding: 20px; border-radius: 10px; display: inline-block; }
        h1 { color: #00ffcc; }
        .value { font-size: 40px; color: #00ff00; }
    </style>
</head>
<body>
    <h1>HLK Vital Monitor</h1>
    <div class="box">
        <h2>Heart Rate</h2>
        <div class="value">{{ hr }} bpm</div>
    </div>
    <div class="box">
        <h2>Respiration Rate</h2>
        <div class="value">{{ rr }} bpm</div>
    </div>
    <div class="box">
        <h2>Status</h2>
        <div class="value">{{ status }}</div>
    </div>
    <p>Last Update: {{ time }}</p>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(HTML_PAGE, **latest_data)

@app.route("/api/vitals", methods=["POST"])
def vitals():
    global latest_data
    data = request.get_json(force=True)

    latest_data["hr"] = data.get("hr", 0)
    latest_data["rr"] = data.get("rr", 0)
    latest_data["status"] = data.get("status", "UNKNOWN")
    latest_data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Received:", latest_data)
    return jsonify({"message": "OK"})

if __name__ == "__main__":
    app.run()
