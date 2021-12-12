# This is an example lambda handler that demonstrates using the en_core_web_sm spacy layer

import json
# this import requires https://github.com/Aleksandr-Gamble/pancakes/tree/main/spacy
import spacy
# this import requires https://github.com/Aleksandr-Gamble/pancakes/tree/main/en_core_web_sm
nlp = spacy.load("/opt/en_core_web_sm/en_core_web_sm-2.3.1")

def lambda_handler(event, context):
    text = event['text'] # Try an event like {"text" : "I visited Coffee Shop Bleu with my friend Fabio."}
    doc = nlp(text) 
    entities = []
    for ent in doc.ents:
        entities.append([ent.text, ent.label_])
    return {
        'statusCode': 200,
        'body': json.dumps({
            'text':text,
            'entities':entities
        })
    }
