from flask import Flask
import sys
from flask_restful import Api
from api.routes import initialize_routes
from flask_cors import CORS
from config.configDB import initialize_db

app = Flask(__name__)

cors = CORS(app)

api  = Api(app)
initialize_routes(api)

app.config['MONGODB_SETTINGS'] = {
    'db' : 'dbalook',
    'host': 'localhost',
    'port': 27017
    
}
initialize_db(app)

HOST = sys.argv[1]
PORT = sys.argv[2]
if __name__ == '__main__':
    # app.run(host="192.168.0.104", port=5000)
    app.run(host=HOST, port=PORT,debug=True)