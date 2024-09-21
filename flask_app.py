from flask import Flask, jsonify, render_template, request, abort
from flask_cors import CORS
from application.api import blueprint
import os
import socket
from application.util.response_handler import Error

app = Flask(__name__)

CORS(app)
app.secret_key = os.urandom(16)
AUTHORIZATION_KEY = "sample"

ALLOWED_ORIGIN = ["127.0.0.1", "127.0.0.1:5000", "http://127.0.0.1:5000"]

@app.before_request
def pre_checks():
    origin = request.headers.get("Origin")
    print(origin, ALLOWED_ORIGIN, request.host_url[:-1])
    if "api" in request.url:
        if request.method == "POST":
            if origin in ALLOWED_ORIGIN or origin in [request.host_url[:-1]]:
                request.data = {"link": request.form.get("youtube_url")}
                pass
            else:
                auth_key = request.headers.get("Authorization")
                if auth_key == AUTHORIZATION_KEY:
                    pass
                else:
                    return Error(401)
        else:
            return Error(500)

app.register_blueprint(blueprint, url_prefix="")

@app.route("/")
def index():
    return render_template("ytdownloader.html")


if __name__ == "__main__":
    app.run(debug=True)
