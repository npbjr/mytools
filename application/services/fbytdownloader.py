from flask import send_file, after_this_request
from typing import Callable, Any
import yt_dlp
import json
import os
from datetime import datetime
from ..util.response_handler import Error

class FBYTDownloader:
    """
    please dont mind with the exagerating code, i need this to stay active on python :)
    """

    def __init__(self): ...

    def __metadata__(self, f: Callable[[dict], Any]):
        f = f()
        return f['fn'], f['df']

    def download_mp3(self, link: str) -> json: ...
    def download_mp4_720p(self, link: str) -> json: ...
    def download_mp4_1024p(self, link: str) -> json: ...
    def download_mp4(self, meta: Callable[[dict], Any], link: str) -> json:

        filename, downloads_folder = self.__metadata__(meta)

        @after_this_request
        def cleanup(response):
            """
            this is will remove the file in your linux system
            """
            os.remove(filename)
            print(f"---- Success Deleting of file {filename} --- ")
            
            return response

        ydl_opts = {
            "format": "best", 
            "outtmpl": os.path.join(
                downloads_folder,
                filename,
            ) 
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            info_d = ydl.extract_info(link, download=False)
            filename = ydl.prepare_filename(info_d)
            return send_file(filename, as_attachment=True)
        
        except Exception as e:
            return Error(400)

