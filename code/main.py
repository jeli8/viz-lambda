import mimetypes

def handler(event, context):
    sourceKey = event['Records'][0]['s3']['object']['key']
    (guessedType, encoding) = mimetypes.guess_type(sourceKey)
    res = "Type is: "
    if guessedType is None:
        res += "UNKNOWN"
    else:
        res += guessedType
    res += ", And file encoding is: "
    if encoding is None:
        res += "UNKONWN"
    else:
        res += encoding
    print(res)
