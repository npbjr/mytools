from flask.views import MethodView
from flask import Flask, jsonify, render_template, request, send_from_directory
from ..services.fbytdownloader import FBYTDownloader
import json


class VideoDownloadView(MethodView):

    def post(self):

        if type(request.data) == str:
            data = json.loads(request.data)
        else:
            data = request.data
        link = data.get("link")
        ytd = FBYTDownloader()
        res = ytd.process_video_link(link)
        return res


VIDEO_DOWNLOAD_VIEW = VideoDownloadView.as_view("video_download_view")
