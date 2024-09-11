from flask import Flask, jsonify, render_template, request, abort
from flask_cors import CORS
from application.api import blueprint
import os
import socket

app = Flask(__name__)

CORS(app)
app.secret_key = os.urandom(16)
AUTHORIZATION_KEY = "sample"


def get_server_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


whitelistips = [get_server_ip(), "127.0.0.1"]


@app.after_request
def after_request(response):

    response.headers["Access-Control-Allow-Origin"] = request.url_root
    return response


@app.before_request
def pre_checks():

    if "api" in request.url:
        print(request.url_root, request.host_url)
        if request.url_root != request.host_url:
            auth_key = request.headers.get("Authorization")
            if auth_key != AUTHORIZATION_KEY:
                return {"message": " Access Denied ", "status": 401}

        if request.url_root == request.host_url:
            request.data = {"link": request.form.get("youtube_url")}


app.register_blueprint(blueprint, url_prefix="")


@app.route("/")
def index():
    return render_template("ytdownloader.html", api_key=app.secret_key.hex())


if __name__ == "__main__":
    app.run(debug=True)
