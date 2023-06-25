import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './bug-bounty-336417-705f60b605e4.json'
from google.cloud import language_v1
client = language_v1.LanguageServiceClient()


def parse_entities (entities):
    entities_list = []

    for entity in entities:
        entity_dict = {
            'name': entity.name,
            'type': entity.type_.name,
            'metadata': entity.metadata,
            'salience': entity.salience
        }

        entities_list.append(entity_dict)

    return entities_list


def entity_extraction (content, content_type):
    try:
        document = language_v1.Document(content=content, type=content_type)
        response = client.analyze_entities(request={'document': document})    
        entities = response.entities
        return {'success': True, 'entities': entities}

    except:
        print("something went wrong")
        return {'success': False}
    

def main (content, content_type):
    
    content_text = '\n'.join(content)
    response = entity_extraction(content_text, content_type=language_v1.Document.Type.PLAIN_TEXT)

    if response['success']:
        return parse_entities(response['entities'])

    return []

