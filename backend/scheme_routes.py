from flask import Blueprint, request, jsonify

scheme_bp = Blueprint("scheme", __name__)


@scheme_bp.route("/scheme-check", methods=["GET"])
def scheme_check():

    land_size = float(request.args.get("land_size", 0))
    income = int(request.args.get("income", 0))
    farmer_type = request.args.get("farmer_type", "small").lower()

    eligible_schemes = []

    # ---------------- PM-KISAN ----------------
    pm_kisan_eligible = land_size <= 5 and farmer_type in ["small", "marginal"]

    if pm_kisan_eligible:
        eligible_schemes.append("PM Kisan Samman Nidhi")

    # ---------------- OTHER SCHEMES ----------------
    eligible_schemes.append("PM Fasal Bima Yojana")
    eligible_schemes.append("Soil Health Card Scheme")

    if income < 200000:
        eligible_schemes.append("Kisan Credit Card (Low-interest loan)")

    # ---------------- RESPONSE ----------------
    return jsonify ({ 
        "input": {
            "land_size": land_size,
            "income": income,
            "farmer_type": farmer_type
        },

        "pm_kisan": {
            "eligible": pm_kisan_eligible,
            "official_website": "https://pmkisan.gov.in",
            "how_to_check": [
                "Open PM-Kisan official website",
                "Click on 'Beneficiary Status'",
                "Enter Aadhaar or Mobile Number",
                "Verify OTP",
                "View status"
            ]
        },

        "eligible_schemes": eligible_schemes
    })