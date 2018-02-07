import spacy

class EntityRecognizer:
    def __init__(self, model):
        self.model = spacy.load(model)

    def get_entity(self, text):
        list_entitiy = []
        split = text.split('\n')
        
        for s in split:
            doc = self.model(s)
            entity = {}
            if doc.ents:
                entity['message'] = s
                entity['entities'] = [(ent.text, ent.label_) for ent in doc.ents]
                list_entitiy.append(entity)

        return list_entitiy