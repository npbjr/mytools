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
config = dict(dotenv_values("system/.env"))

print("[\033[92m BUILD \033[0m] config .. :", config)    

ALLOWED_ORIGINS = config.get('ALLOWED_ORIGINS').split(',')

socketio = SocketIO(app, cors_allowed_origins=ALLOWED_ORIGINS)

app.register_blueprint(create_blueprint(socketio), url_prefix="")

AUTHORIZATION_KEY = config.get("API_KEY")

@app.before_request
def pre_checks():
    origin = request.headers.get("Origin")

    print(origin, ALLOWED_ORIGINS, request.host_url[:-1])
    
    if "api" in request.url:
        if request.method == "POST":
            if origin in ALLOWED_ORIGINS or origin in [request.host_url[:-1]]:
                print("[\033[92m PRECHECKS \033[0m]--- allowed client auto pass --- ")    
                pass
            else:

                print("[\033[92m PRECHECKS \033[0m]--- auth is required for external clients --- ")

                auth_key = request.headers.get("Authorization")
                
                if auth_key == AUTHORIZATION_KEY:
                    pass
                else:
                    return {"Error":"Unauthorized"}
            # else:
            #     return {"Error":"Unauthorized"}
                # return Error(401)
        else:
            return {"Error":"Unauthorized"}
            
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
    socketio.run(app, host='0.0.0.0', port=5000)
