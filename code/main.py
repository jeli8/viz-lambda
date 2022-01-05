def handler(event, context):
    sourceKey = event['Records'][0]['s3']['object']['key']
    print(sourceKey)
