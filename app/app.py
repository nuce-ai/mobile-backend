from flask import Flask,send_from_directory

import os

app  = Flask(__name__,static_folder=None)

APP_ROOT        = os.path.join(os.path.dirname(__file__),'.')
UPLOAD_FOLDER   = os.path.join(APP_ROOT,'upload')
# print(os.path.dirname(__file__))
# assets_folder   = os.path.join("C:/Users/peaco/Desktop/mobile-backend/",'assets')
# print(assets_folder)
# @app.route('/assets/<path:filename>')
# def assets(filename):
#   # Add custom handling here.
#   # Send a file download response.
#   return send_from_directory(assets_folder, filename)

app.config.update(DEBUG = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER