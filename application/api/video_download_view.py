from flask.views import MethodView
from flask import Flask, jsonify, render_template, request, send_from_directory
from ..services.fbytdownloader import FBYTDownloader
import json
import os
from yt_dlp import YoutubeDL
from datetime import datetime

VIDEO_TITLE_LIMIT:int = 50
ytd = FBYTDownloader()

class VideoDownloadView(MethodView):
    
    def post(self):

        if type(request.data) == str:
            data = json.loads(request.data)
        else:
            data = request.data

        link = data.get("link")
        
        """
        get the filename and update
        """

        with YoutubeDL() as ydl:
            info_d = ydl.extract_info(link, download=False)

        filename = ydl.prepare_filename(info_d)

        return ytd.download_mp4(
            lambda *args : dict(fn = "{name}.%(ext)s".format(
                        name=f"{filename[:VIDEO_TITLE_LIMIT]}..."+str(int(datetime.now().timestamp() * 1000))),
                df = os.path.join(os.path.expanduser("~"), "downloads")), 
                link)
        

VIDEO_DOWNLOAD_VIEW = VideoDownloadView.as_view("video_download_view")
