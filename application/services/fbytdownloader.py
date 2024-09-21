from flask import send_file, after_this_request
import yt_dlp
import json
import os
from datetime import datetime
from ..util.response_handler import Error

class FBYTDownloader:
    def __init__(self): ...
    def process_video_link(self, link: str) -> json:
        current_timestamp = datetime.now()

        milliseconds = int(current_timestamp.timestamp() * 1000)

        downloads_folder = os.path.join(os.path.expanduser("~"), "downloads")
        filename = "{title}.%(ext)s".format(title=milliseconds)

        @after_this_request
        def cleanup(response):
            os.remove(filename)
            print(f"---- Success Deleting of file {filename} --- ")
            return response

        ydl_opts = {
            "format": "best",  # Download the best quality available
            "outtmpl": os.path.join(
                downloads_folder,
                filename,
            )  # Save to Downloads folder
        }
        try:
            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            info_d = ydl.extract_info(link, download=False)
            filename = ydl.prepare_filename(info_d)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return Error(400)
