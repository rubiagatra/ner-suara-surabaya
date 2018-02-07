import datetime
from flask import Flask
from flask_restful import Api
from resources.hello_world import HelloWorld
from resources.ner import Ner 
from flask_jwt import JWT
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'kasih-tau-gak-ya'
app.config['BUNDLE_ERRORS'] = True
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60)

jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(Ner, '/api/ner')
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)
