# -*- coding: utf-8 -*-
from flask import Response, request
from flask_restful import Resource,reqparse
from werkzeug.utils import secure_filename
from models.InformationModel import *
import json
import os
import subprocess
import base64

class InformationController(Resource):
    def post(self):
        payload = request.get_json()
        # print(getDetailObject(payload)['object_content'])
        return Response(
                json.dumps(
                    {"status": 200, 
                    "content": getDetailObject(payload)['object_content']
                    
                    }),
                mimetype="application/json",
                status=200)

class AddInformationController(Resource):
    def post(self):
        payload = request.get_json()
        createObject(payload)
        return Response(
                json.dumps(
                    {"status": 200, 
                    "message" : "Create information succeeded"
                    
                    }),
                mimetype="application/json",
                status=200)
    def put(self):
        payload = request.get_json()
        updateObject(payload)
        return Response(
            json.dumps({
               "status" : 200,
               "message" : "Update information succeeded"
            })
        )
    
    def delete(self):
        payload = request.get_json()
        deleteObject(payload)
        return Response(
            json.dumps({
               "status" : 200,
               "message" : "Delete information succeeded"
            })
        )