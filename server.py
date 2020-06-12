from flask import Flask
import sys
from flask_restful import Api
from api.routes import initialize_routes
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

api  = Api(app)
initialize_routes(api)

app.config.update(DEBUG = True)



if __name__ == '__main__':
    
    app.run()