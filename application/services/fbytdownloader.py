from flask import send_file
import yt_dlp
import json
import os
from datetime import datetime


class FBYTDownloader:
    def __init__(self) -> None:
        pass

    def process_video_link(self, link: str) -> json:

        current_timestamp = datetime.now()

        milliseconds = int(current_timestamp.timestamp() * 1000)

        downloads_folder = os.path.join(os.path.expanduser("~"), "downloads")
        ydl_opts = {
            "format": "best",  # Download the best quality available
            "outtmpl": os.path.join(
                downloads_folder,
                "{title}.%(ext)s".format(title=milliseconds),
            ),  # Save to Downloads folder
        }
        try:
            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            info_d = ydl.extract_info(link, download=False)
            filename = ydl.prepare_filename(info_d)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return {"message": "An error has occurred", "status": 400}
