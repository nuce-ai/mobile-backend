from flask import Response, request
from flask_restful import Resource,reqparse
from werkzeug.utils import secure_filename

import json
import os
import subprocess
import base64


ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif','pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadImageController(Resource):
    
    def post(self):
       file = request.files['file']
       filename = secure_filename(file.filename)
       # image_string = base64.b64encode(file.read())
       # print(image_string)
       # print(file.filename)
       # print(filename)
       if file and allowed_file(file.filename):
              upload = os.path.join('./upload/',filename)
              file.save(upload)
              stringProc = "python object_detection/main.py " + filename
              proc = subprocess.Popen(stringProc, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
              ret  = proc.communicate()[0]
              proc.wait()
              IMAGE_FILE_NAME = filename.split(".")[0]
              with open("assets/"+IMAGE_FILE_NAME+'.txt') as f:
                     etJson = json.load(f)
              return Response(json.dumps({"payload": etJson,"status":"200"}), mimetype="application/json", status=200)
       else:
              return Response(json.dumps({"message": "upload image failed","status":"400"}), mimetype="application/json", status=400)
