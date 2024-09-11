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


WHITELISTED_IPS = ["127.0.0.1", "127.0.0.1:5000"]


@app.after_request
def after_request(response):

    response.headers["Access-Control-Allow-Origin"] = request.url_root
    return response


@app.before_request
def pre_checks():
    # try:
    #     print(request.environ["HTTP_HOST"], get_server_ip())
    #     print(request.environ["HTTP_ORIGIN"])
    # except Exception as e:
    #     print(e)
    if "api" in request.url:
        server_ip = get_server_ip()
        print(server_ip, WHITELISTED_IPS)
        if server_ip not in WHITELISTED_IPS:
            auth_key = request.headers.get("Authorization")
            if auth_key != AUTHORIZATION_KEY:
                return {"message": " Access Denied ", "status": 401}
        else:
            request.data = {"link": request.form.get("youtube_url")}


app.register_blueprint(blueprint, url_prefix="")


@app.route("/")
def index():
    return render_template("ytdownloader.html", api_key=app.secret_key.hex())


if __name__ == "__main__":
    app.run(debug=True)
