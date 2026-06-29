from flask import Blueprint, request, jsonify
import requests

weather_bp = Blueprint("weather", __name__)

API_KEY = "78d7739aecfced63bf50f5ca23eb3f9f"

@weather_bp.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "Delhi")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather"}), 500

    data = response.json()

    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    })