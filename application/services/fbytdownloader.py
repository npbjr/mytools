from flask import send_file, after_this_request
from typing import Callable, Any
import yt_dlp as video
import json
import os
from datetime import datetime
from ..util.response_handler import Error
from flask_socketio import SocketIO, emit

class FBYTDownloader:
    """
    please dont mind with the exagerating code, i need this to stay active on python :)
    """
    def __init__(self):...

    def __metadata__(self, f: Callable[[dict], Any]):
        f = f()
        return f['fn'], f['df']

    def download_mp3(self, link: str) -> json: ...
    def download_mp4_720p(self, link: str) -> json: ...
    def download_mp4_1024p(self, link: str) -> json: ...

    def download_mp4(self, meta: Callable[[dict], Any], link: str) -> json:

        filename, downloads_folder = self.__metadata__(meta)

        @after_this_request
        def clean_directory(response):
            """
            this is will remove the file in your linux system
            """
            os.remove(filename)

            print(f"---- Success Deleting of file {filename} --- ")

            return response
            
        def progress_hook(d):
            if d['status'] == 'downloading':
                percentage = d['downloaded_bytes'] / d['total_bytes'] * 100
                emit('download_progress', {'progress': percentage}, broadcast=True,  namespace="/video_downloader")
        try:

            with video.YoutubeDL({
                    'progress_hooks': [progress_hook],
                    "format": "best", 
                    "outtmpl": os.path.join(
                        downloads_folder,
                        filename,
                    ) 
                }) as vid:
                vid.download([link])

            info_d = vid.extract_info(link, download=False)
            filename = vid.prepare_filename(info_d)
            emit('download_complete', {'filename':filename}, broadcast=True,  namespace="/video_downloader")
            return send_file(filename, as_attachment=True)
            # return filename
        except Exception as e:
            print("ERROR DOWNLOAD ",e)
            return e
            # return Error(400)

