from config.configDB import db
from datetime import datetime
import json 

# Định nghĩa đối tượng collection trong MongoDB 
# Collection Object defined in MongoDB
class ObjectInfo(db.Document):
    object_name    = db.StringField(required=True, unique=True)
    object_content = db.StringField(required=True)
  
    
def createObject(payload):
    newObject = ObjectInfo(
        object_name=payload["object_name"],
        object_content=payload["object_content"]
    )
    newObject.save()


# Sau khi đã có đối tượng, ta sẽ thao tác với đối tượng đó 
def getObject():
    # print(ObjectInfo.objects()[0]['object_content'])
    return ObjectInfo.objects()

# def updateEmployee(self,payload):
#     pass #
# def deleteEmployee(payload):
#     id_ =  Employee.objects.get(employee_id = payload['id']).delete()
#     return id_ 
def getDetailObject(payload):
    result = ObjectInfo.objects.get(object_name = payload['object_name'])
    return result
# def updateEmployee(payload): 
#     result = Employee.objects.get(employee_id = payload["id"]).update(**payload["data"])
#     return result

def updateObject(payload):
    ObjectInfo.objects.get(object_name = payload['object_name']).update(**payload)
def deleteObject(payload):
    ObjectInfo.objects.get(object_name = payload['object_name']).delete()