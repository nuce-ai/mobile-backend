from flask import Response, request
from flask_restful import Resource,reqparse


import json
import os
import subprocess



ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif','pdf'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadImageController(Resource):
    
    def post(self):
       file = request.files['file']
       print(file)
       if file and allowed_file(file.filename):
              upload = os.path.join('./upload/',"target.png")
              file.save(upload)
              proc = subprocess.Popen("python object_detection/main.py", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
              ret  = proc.communicate()[0]
              proc.wait()
              with open("result.txt") as f:
                     etJson = json.load(f)
              return Response(json.dumps({"payload": etJson,"status":"200"}), mimetype="application/json", status=200)
       else:
              return Response(json.dumps({"message": "upload image failed","status":"400"}), mimetype="application/json", status=400)
