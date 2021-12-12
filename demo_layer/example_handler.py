import json
# this import requires https://github.com/Aleksandr-Gamble/pancakes/tree/main/demo_layer
import my_layer

def lambda_handler(event, context):
    message = my_layer.greet("Amanda")
    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
