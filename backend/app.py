from flask import Flask
from flask_cors import CORS

from disease_routes import disease_bp
from weather_routes import weather_bp
from mandi_routes import mandi_bp
from scheme_routes import scheme_bp
from voice_routes import voice_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(disease_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(mandi_bp)
app.register_blueprint(scheme_bp)
app.register_blueprint(voice_bp)

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "Fasal Sanjeevani Backend Running"
    }
print(app.url_map)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)