from flask import Blueprint, request, jsonify
import os

from model_predict import predict_disease
from disease_data import disease_info
import database

disease_bp = Blueprint("disease", __name__)

UPLOAD_FOLDER = "uploads"


@disease_bp.route("/predict", methods=["POST"])
def predict():

    # ---------------- CHECK IMAGE ----------------
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    # ---------------- SAVE IMAGE ----------------
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)

    # ---------------- PREDICT DISEASE ----------------
    result = predict_disease(filepath)
    disease = result["disease"]

    # ---------------- GET DISEASE INFO ----------------
    info = disease_info.get(disease, {})

    # ---------------- SAVE TO HISTORY ----------------
    database.cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disease TEXT,
            symptoms TEXT,
            treatment TEXT,
            prevention TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    database.conn.commit()

    database.cursor.execute("""
        INSERT INTO history (disease, symptoms, treatment, prevention)
        VALUES (?, ?, ?, ?)
    """, (
        disease,
        info.get("symptoms", "Not available"),
        info.get("treatment", "Not available"),
        info.get("prevention", "Not available")
    ))

    database.conn.commit()

    # ---------------- RESPONSE ----------------
    return jsonify({
        "disease": disease,
        "treatment": info.get("treatment", "Not available"),
        "prevention": info.get("prevention", "Not available"),
        "symptoms": info.get("symptoms", "Not available")
    })


# ---------------- HISTORY API ----------------
@disease_bp.route("/history", methods=["GET"])
def history():

    database.cursor.execute("""
        SELECT disease, symptoms, treatment, prevention, created_at
        FROM history
        ORDER BY id DESC
    """)

    rows = database.cursor.fetchall()

    data = []

    for r in rows:
        data.append({
            "disease": r[0],
            "symptoms": r[1],
            "treatment": r[2],
            "prevention": r[3],
            "time": r[4]
        })

    return jsonify(data)