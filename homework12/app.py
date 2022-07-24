import logging

from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

logging.basicConfig(filename='basic.log', level=logging.INFO)

@app.route("/upload/<path:path>")
def static_dir(path):
    return send_from_directory("upload", path)

if __name__ == '__main__':
    app.run(debug = True)