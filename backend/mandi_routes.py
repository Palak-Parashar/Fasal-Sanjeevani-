from flask import Blueprint, request, jsonify
import random

mandi_bp = Blueprint("mandi", __name__)


@mandi_bp.route("/mandi-rate", methods=["GET"])
def mandi_rate():

    crop = request.args.get("crop", "wheat").lower()

    # ---------------- REALISTIC BASE MARKET DATA ----------------
    base_prices = {
        "wheat": 2400,
        "rice": 3000,
        "cotton": 6800,
        "sugarcane": 350
    }

    if crop not in base_prices:
        return jsonify({"error": "Crop not supported"}), 404

    base = base_prices[crop]

    # ---------------- LIVE-LIKE FLUCTUATION ----------------
    fluctuation = random.uniform(-0.08, 0.08)
    price = round(base * (1 + fluctuation), 2)

    # ---------------- MARKET LOGIC ----------------
    if price > 6000:
        trend = "high demand"
        decision = "SELL NOW"
    elif price > 3000:
        trend = "stable"
        decision = "WATCH MARKET"
    else:
        trend = "low demand"
        decision = "HOLD"

    return jsonify({
        "crop": crop,
        "mandi_price_per_quintal": price,
        "market_trend": trend,
        "decision": decision,
        "source": "simulated_realistic_market"
    })