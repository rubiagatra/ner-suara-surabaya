from pymongo import MongoClient
from ner_api.user import UserModel

def create_user():
    if UserModel.find_by_username('sandbox'):
        return None 
    client = MongoClient('mongo', 27017)
    db = client['ner-api']
    collection = db['user']
    collection.insert_one({'_id': 1, "username": "sandbox", "password": "sandbox"})
    client.close()