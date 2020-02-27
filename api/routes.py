# from controllers.employeeController import EmployeesController,EmployeeController
# from controllers.homeController import HomeController
# from controllers.authController import *
# from controllers.roleController import *
from controllers.uploadController import *
# from controllers.scoreController import *
# from controllers.chatController import *
# from controllers.bookingRoomController import *
def initialize_routes(api):
#   --------- HomeController --------

  api.add_resource(UploadImageController,'/api/upload')

