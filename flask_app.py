from flask import Flask, jsonify, render_template, request, abort, current_app, session
from flask_cors import CORS
from application.api import create_blueprint
import os
from application.util.response_handler import Error
from dotenv import dotenv_values
from flask_socketio import SocketIO, emit, Namespace
app = Flask(__name__)

CORS(app)
app.secret_key = os.urandom(16)

socketio = SocketIO(app, cors_allowed_origins=['https://npbjr.pythonanywhere.com','http://127.0.0.1:5000'])

app.register_blueprint(create_blueprint(socketio), url_prefix="")


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

class MyNameSpace(Namespace):
    def on_connect(self):
        print("Client web connected")

@app.route('/get_key', methods=['GET'])
def get_key():
    key = os.urandom(16)
    socketio.on_namespace(MyNameSpace(f'/{key.hex()}'))

    session['iokey'] = f'/{key.hex()}'
    return jsonify({"key": f'/{key.hex()}'})

@app.route("/")
def index():
    return render_template("ytdownloader.html")

@app.route("/freesms")
def freesms():
    return render_template("freesms.html")

if __name__ == "__main__":
    socketio.run(app, debug=True)
