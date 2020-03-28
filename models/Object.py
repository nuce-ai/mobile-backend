from config.configDB import db
from bson.json_util import loads,dumps
import json
class ObjectInfo(db.Document):
    object_name     = db.StringField(require=True,unique=True)
    object_info     = db.StringField()
    object_detail   = db.StringField()


def createObject(payload):
    newObject = ObjectInfo(
        object_name = payload['object_name'],
        object_info = payload['object_info'],
        object_detail = payload['object_detail']
    )
    newObject.save()


def getObjectAll():
    objectList = ObjectInfo.objects._collection.find(
            {},
            {
                "object_name" : True,
                "object_info":True,
                "object_detail" : True,
                "_id" : False,
            })
 
    return list(objectList)

def getObjectDetail(payload):
    objectList = ObjectInfo.objects._collection.find(
            {"object_name" : payload['object_name']},
            {
                "object_name" : True,
                "object_info":True,
                "object_detail" : True,
                "_id" : False,
            })
 
    return list(objectList)

def updateObject(payload):
    result = ObjectInfo.objects.get(object_name = payload["object_name"]).update(**payload["data"])
    return result

def deleteObject(payload):
    id_ = ObjectInfo.objects.get(object_name = payload['object_name']).delete()
    return id_
