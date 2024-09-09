from flask import Blueprint
from .video_download_view import VIDEO_DOWNLOAD_VIEW

API = Blueprint('api', __name__)
API.add_url_rule('/upload', view_func=VIDEO_DOWNLOAD_VIEW)