from flask import Response, request
from flask_restful import Resource,reqparse
from models.Object import *
import json
import os

class ObjectDetailController(Resource):
    def post(self):
        payload = request.get_json()
        result = getObjectDetail(payload)
        return Response(json.dumps({"payload" : result,"status":200}),mimetype='application/json',status=200)
class ObjectController(Resource):
    # Get object all 
    def get(self):
        result = getObjectAll()
       
        return Response(json.dumps({"payload" : result,"status":200}),mimetype='application/json',status=200)

    # Update object 
    def put(self):  
        payload = request.get_json()
        updateObject(payload)
        return Response(json.dumps({"message" : "update succeeded","status":200}),mimetype='application/json',status=200)
    # Insert Object
    def post(self):
        payload = request.get_json()
        createObject(payload)
        return Response(json.dumps({"message" : "create succeeded","status":200}),mimetype='application/json',status=200)
    # Delete Object 
    def delete(self):
        payload = request.get_json()
        deleteObject(payload)
        return Response(json.dumps({"message" : "delete succeeded","status":200}),mimetype='application/json',status=200)
