from flask import Flask, jsonify, render_template, request, abort, current_app
from flask_cors import CORS
from application.api import blueprint
import os
from application.util.response_handler import Error
from dotenv import dotenv_values
from flask_socketio import SocketIO, emit, Namespace
app = Flask(__name__)

CORS(app)
app.secret_key = os.urandom(16)

app.register_blueprint(blueprint, url_prefix="")
socketio = SocketIO(app, cors_allowed_origins="*")

class MyNameSpace(Namespace):
    def on_connect(self):
        print("Client web connected")


socketio.on_namespace(MyNameSpace('/video_downloader'))

config = dict(dotenv_values("system/.env"))
print(config)

ALLOWED_ORIGIN = ["127.0.0.1", "127.0.0.1:5000", "http://127.0.0.1:5000"]
AUTHORIZATION_KEY = config.get("API_KEY")

@app.before_request
def pre_checks():
    origin = request.headers.get("Origin")

    print(origin, ALLOWED_ORIGIN, request.host_url[:-1])
    
    if "api" in request.url:
        if request.method == "POST":
            # if origin in ALLOWED_ORIGIN or origin in [request.host_url[:-1]]:
            #     request.data = {"link": request.form.get("youtube_url")}
            #     pass
            # else:
            auth_key = request.headers.get("Authorization")
            print(request.data)
            if auth_key == AUTHORIZATION_KEY:
                pass
            else:
                pass
                # return Error(401)
        else:
            pass
            # return Error(500)



@app.route("/")
def index():
    return render_template("ytdownloader.html")

@app.route("/freesms")
def freesms():
    return render_template("freesms.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
