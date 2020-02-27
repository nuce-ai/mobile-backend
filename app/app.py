from flask import Flask

import os

app  = Flask(__name__)

APP_ROOT        = os.path.join(os.path.dirname(__file__),'.')
UPLOAD_FOLDER   = os.path.join(APP_ROOT,'upload')


app.config.update(DEBUG = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER