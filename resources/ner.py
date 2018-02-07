from flask_restful import Resource, reqparse
from models.ner import NerModel 
from flask_jwt import jwt_required


class Ner(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('created_time', required=True,
                        type=str, help="created_time cannot be blank")
    parser.add_argument('message', required=True,
                        type=str, help="message cannot be blank")
    parser.add_argument('post_id', required=True,
                        type=str, help="post_id cannot be blank")

    @jwt_required()
    def post(self):
        data = Ner.parser.parse_args()
        ner = NerModel(data['post_id'], data['created_time'], data['message'])
        ner_data = ner.get_entity()
        ner.save_to_db()
        return {'success': True, 'ner':ner_data}, 201