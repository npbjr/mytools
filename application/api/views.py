from flask import Blueprint
from flask.views import MethodView
from .video_download_view import VideoDownloadView


class NotSupported(MethodView):
    not_supported:str = lambda *args: f"Not Supported yet{args}"
    
    def post(self): ...
    def get(self):
        return not_supported

NOT_SUPPORTED = NotSupported.as_view("not_supported")

def create_blueprint(socketio):


    API = Blueprint("api", __name__)

    API.add_url_rule("/api/uploadvideo", view_func=VideoDownloadView.as_view("video_download_view", socketio=socketio))
    API.add_url_rule("/api/converttopng", view_func=NOT_SUPPORTED)
    API.add_url_rule("/api/sendsms", view_func=NOT_SUPPORTED)

    return API
