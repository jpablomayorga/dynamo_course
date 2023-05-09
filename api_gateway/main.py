import json
import boto3

dynamodb = boto3.resource('dynamodb')

personajesTable = dynamodb.Table("Personajes")

def lambda_handles(event, content):
   event['Id'] = int(event['Id'])
   personajesTable.put_item(Item=event)
   return {
      'statusCode': 200,
      'body': json.dumps('Evento Insertado')
   }

