from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
from services.ytdownloader import YTDownloader
from services.fbytdownloader import FBYTDownloader
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
VALID_API_KEY = "TEST"


def load_school_data():
    with open("school_data.json") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/myloves")
def index2():
    return render_template("index2.html")


@app.route("/ytdownloader")
def upload_template():
    return render_template("ytdownloader.html")


# @app.route("/mylove")
# def index():
#     return render_template("index2.html")


@app.route("/api/nearby-schools", methods=["GET"])
def get_nearby_schools():
    api_key = request.headers.get("X-API-Key")

    if api_key != VALID_API_KEY:
        return jsonify({"error": "Unauthorized access"}), 403

    school_data = load_school_data()
    return jsonify(school_data)


@app.route("/upload", methods=["POST"])
def upload() -> json:
    # pythonanywhere doesn't allow connection to yotube
    # link = request.form.get("youtube_url")
    # if not link:
    #     return {"mesasge": "No link found", "status": 200}
    # ytd = YTDownloader()
    # res = ytd.process_video_link(link)
    link = request.form.get("youtube_url")
    if not link:
        return {"mesasge": "No link found", "status": 200}
    ytd = FBYTDownloader()
    res = ytd.process_video_link(link)
    return res


import os

# Define the directory where your files are stored
DOWNLOAD_DIRECTORY = os.path.join(
    os.path.expanduser("~"), "downloads"
)  # Adjust as needed


@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
