from pymongo import MongoClient
import spacy

MONGO_URI = 'mongo'
model = spacy.load('ner_api/ner/resources/trafizap_example_model')


class NerModel:

    def __init__(self, post_id, created_time, message):
        self.post_id = post_id
        self.created_time = created_time
        self.message = message
        self.list_entitiy = []

    def save_to_db(self):

        if self.list_entitiy:
            client = MongoClient(MONGO_URI, 27017)
            db = client['ner-api']
            collection = db['ner']
            collection.insert({'post_id': self.post_id,
                               'created_time': self.created_time,
                               'ner': self.list_entitiy, 'message': self.message})
            client.close()
        else:
            return "Entity still empty"

    def get_entity(self):
        split = self.message.split('\n')

        for s in split:
            doc = model(s)
            entity = {}
            if doc.ents:
                entity['message'] = s
                entity['entities'] = {ent.text: ent.label_ for ent in doc.ents}
                self.list_entitiy.append(entity)

        return self.list_entitiy
