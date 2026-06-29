from flask import Blueprint

voice_bp = Blueprint(
    "voice",
    __name__
)

@voice_bp.route("/voice")
def voice():

    return {
        "message": "Voice Assistant API Working"
    }