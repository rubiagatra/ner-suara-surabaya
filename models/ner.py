from pymongo import MongoClient
import json

with open('config/mongo_uri.json') as json_data:
    data =  json.load(json_data)


class NerModel:

    def __init__(self, post_id, created_time, message, ner):
        self.post_id = post_id
        self.created_time = created_time
        self.message = message
        self.ner = ner
    
    def save_to_db(self):
        client = MongoClient(data['MONGO_URI'])
        db = client['demo']
        collection = db['ner']
        collection.insert({'post_id': self.post_id, 
                          'created_time': self.created_time,
                          'ner': self.ner, 'message': self.message})
        client.close()
