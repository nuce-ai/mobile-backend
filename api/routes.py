from controllers.uploadController import *
from controllers.infoController import *

def initialize_routes(api):
  api.add_resource(UploadImageController,'/api/analysis/image')
  api.add_resource(InformationController,'/api/object/info')
  api.add_resource(AddInformationController,'/api/object/action')

