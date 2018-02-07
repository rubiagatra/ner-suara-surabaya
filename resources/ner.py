from utils.entity_recognizer import EntityRecognizer
from flask_restful import Resource, reqparse
from models.ner import NerModel 
from flask_jwt import jwt_required

ent_recog = EntityRecognizer('utils/example_model')

class Ner(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('created_time', required=True,
                            type=str, help="created_time cannot be blank" )
    parser.add_argument('message', required=True,
                            type=str, help="message cannot be blank" )
    parser.add_argument('post_id', required=True,
                            type=str, help="post_id cannot be blank" )

    @jwt_required()
    def post(self):
        data = Ner.parser.parse_args()
        ner_data = ent_recog.get_entity(data['message'])
        ner = NerModel(data['post_id'], data['created_time'], data['message'], ner_data) 
        ner.save_to_db()
        return {'success': True, 'ner':ner}, 201