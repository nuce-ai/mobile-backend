from flask import Flask
import sys
from flask_restful import Api
from api.routes import initialize_routes
from flask_cors import CORS
from config.configDB import initialize_db
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db' : 'alook',
    'host': 'mongodb+srv://alook:alook12345678@object-information.i7udl.mongodb.net/alook?retryWrites=true&w=majority'
    }
cors = CORS(app)
initialize_db(app)
api  = Api(app)
initialize_routes(api)

app.config.update(DEBUG = True)



if __name__ == '__main__':
    
    app.run()