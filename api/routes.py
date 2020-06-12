from controllers.uploadController import *


def initialize_routes(api):
  api.add_resource(UploadImageController,'/api/analysis/image')


