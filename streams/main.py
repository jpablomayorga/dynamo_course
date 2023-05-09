
def lambda_handler(event, context):
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                manejar_insert()
            if record['eventName'] == 'MODIFY':
                manejar_update()
            if record['eventName'] == 'REMOVE':
                manejar_delete()
    except Exception as e:
        print(e)
        return 'Error'
    return 'Listo!'
    
    def manejar_insert(record):
        print('llego un evento insert')
        print(record)
        
    def manejar_update(record):
        print('llego un evento update')
        print(record)
        
    def manejar_delete(record):
        print('llego un evento delete')
        print(record)