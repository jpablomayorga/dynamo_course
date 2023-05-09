import boto3
from boto3.dynamodb.conditions import Key, Attr

class ManagePersonajes:
    def __init__(self) -> None:
        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table('Personajes')  

    def get_item_by_id(self, id):
        response = self.table.query(KeyConditionExpression=Key('Id').eq(id))
        return response

    def create_item(self):        
        self.table.put_item(
            Item = {
                'Id': 123,
                'Gender': 'F',
                'Status': 'Alive'
            }
        )

    def list_tables(self):        
        tables = []
        for table in self.db.tables.all():
            # print(table.name)
            tables.append(table.name)
        return tables
    
if __name__ == '__main__':
   p = ManagePersonajes()
   p.create_item()
   # print(p.get_item_by_id(123))
   print(p.list_tables())



