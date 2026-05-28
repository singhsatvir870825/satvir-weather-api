from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ONLINE",
        "made_by": "Satvir"
    })

@app.route("/weather")
def weather():

    city = request.args.get("city", "Delhi")

    data = {
        "city": city,
        "temperature": f"{random.randint(20,40)} °C",
        "weather": random.choice([
            "Sunny",
            "Cloudy",
            "Rainy"
        ]),
        "humidity": f"{random.randint(40,90)}%"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
