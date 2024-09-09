from flask.views import MethodView
from flask import Flask, jsonify, render_template, request, send_from_directory
from ..services.fbytdownloader import FBYTDownloader
class VideoDownloadView(MethodView):

    
    def post(self):
            
        link = request.form.get("youtube_url")
        if not link:
            return {"mesasge": "No link found", "status": 200}
        ytd = FBYTDownloader()
        res = ytd.process_video_link(link)
        return res

VIDEO_DOWNLOAD_VIEW = VideoDownloadView.as_view('video_download_view')