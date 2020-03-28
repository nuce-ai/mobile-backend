from controllers.uploadController import *
from controllers.objectController import * 

def initialize_routes(api):
  api.add_resource(UploadImageController,'/api/analysis/image')

  api.add_resource(ObjectController,'/api/object')
  api.add_resource(ObjectDetailController,'/api/object/detail')

