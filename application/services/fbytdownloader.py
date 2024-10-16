from flask import send_file, after_this_request, session, request
from typing import Callable, Any
import yt_dlp as video
import json
import os
from datetime import datetime
from ..util.response_handler import Error
import subprocess
import time


class FBYTDownloader:
    """
    please dont mind with the exagerating code, this for enhancing my python skills 
    """
    def __init__(self):...

    def __metadata__(self, f: Callable[[dict], Any]):
        f = f()
        return f['fn'], f['df']

    def __progress__(self, p: Callable[...,Any]): ...
        

    def download_mp3(self, link: str) -> json: ...
    def download_mp4_720p(self, link: str) -> json: ...
    def download_mp4_1024p(self, link: str) -> json: ...

    def download_mp4(self, socketio, meta: Callable[[dict], Any], link: str) -> json:

        filename, downloads_folder = self.__metadata__(meta)

        io_session_key = request.headers.get('IOSession-key', False)

        socketio.emit('download_progress', {'progress': 40},  
                namespace=io_session_key) if io_session_key else ...

        print(io_session_key)

        @after_this_request
        def clean_directory(response):
            """
            this is will remove the file in your linux system
            """
            os.remove(filename)

            print(f"---- Success Deleting of file {filename} --- ")

            return response
            
        def progress_hook(d):

            print("STATUS ", d['status'])

            if d['status'] == 'downloading':
                percentage = d['downloaded_bytes'] / d['total_bytes'] * 100
                print("percentage ", percentage)
                socketio.emit('download_progress', {'progress': percentage},  
                namespace=io_session_key) if io_session_key else ...
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

            socketio.emit('download_complete', {'filename':filename},  
                namespace=io_session_key) if io_session_key else ...

            return send_file(filename, as_attachment=True)

        except Exception as e:
            print("ERROR DOWNLOAD ",e)
            return e

