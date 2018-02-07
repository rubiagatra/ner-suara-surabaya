from flask_restful import Resource
from flask_jwt import jwt_required


class HelloWorld(Resource):
    
    def get(self):
        return "Hello World"
