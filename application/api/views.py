from flask import Blueprint
from flask.views import MethodView
from .video_download_view import VIDEO_DOWNLOAD_VIEW

class NotSupported(MethodView):
    not_supported:str = lambda *args: f"Not Supported yet{args}"
    def post(self): ...
    def get(self):
        return not_supported
NOT_SUPPORTED = NotSupported.as_view("not_supported")

API = Blueprint("api", __name__)

API.add_url_rule("/api/uploadvideo", view_func=VIDEO_DOWNLOAD_VIEW)
API.add_url_rule("/api/converttopng", view_func=NOT_SUPPORTED)
API.add_url_rule("/api/convertto", view_func=NOT_SUPPORTED)
