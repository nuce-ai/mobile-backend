from app.app import app
import sys
from flask_restful import Api
from api.routes import initialize_routes
from flask_cors import CORS

cors = CORS(app)

api  = Api(app)
initialize_routes(api)


HOST = sys.argv[1]
PORT = sys.argv[2]
if __name__ == '__main__':
    # app.run(host="192.168.0.104", port=5000)
    app.run(host=HOST, port=PORT,debug=True)