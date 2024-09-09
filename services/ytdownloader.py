from pytubefix import YouTube
from pytubefix.cli import on_progress
import json
import os
import datetime


class YTDownloader:
    def __init__(self) -> None:
        pass

    def process_video_link(self, link: str) -> json:
        youtubeObject = YouTube(link, on_progress_callback=on_progress)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        try:
            now = datetime.datetime.now()
            d = int(now.timestamp() * 1000)
            youtubeObject.download(
                output_path=downloads_folder, filename="ytdt{d}.mp4".format(d=d)
            )

        except:
            print("An error has occurred")
            return {"message": "An error has occurred", "status": 400}
        print("Download is completed successfully")
        return {
            "message": "Download is completed successfully, please see Downloads Folder",
            "status": 200,
        }
