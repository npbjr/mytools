from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
from application.api import blueprint
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


app.secret_key = 'secret'
# Check Configuration section for more details
app.register_blueprint(blueprint, url_prefix='')

@app.route("/")
def index():
    return render_template("ytdownloader.html")

if __name__ == "__main__":
    app.run(debug=True)
