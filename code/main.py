import mimetypes
import logging
import json
import boto3
from botocore.exceptions import ClientError


RECEIVER = 'arthur@viz.ai'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    SENDER = 'arthur@viz.ai'
    
    sourceKey = event['Records'][0]['s3']['object']['key']
    (guessedType, encoding) = mimetypes.guess_type(sourceKey)
    emailContent = "Type is: "
    if guessedType is None:
        emailContent += "UNKNOWN"
    else:
        emailContent += guessedType
    emailContent += ", And file encoding is: "
    if encoding is None:
        emailContent += "UNKONWN"
    else:
        emailContent += encoding

    logger.info(f'Sending email with content - {emailContent}')

    ### Sending email logic
    DESTINATION = {
                        'ToAddresses': [
                            RECEIVER,
                        ],
                        'BccAddresses': [
                        ]
                    }
    AWS_REGION = "us-east-1"
    SUBJECT = 'Eli Yaacov - Viz home test'
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    response = ""
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination = DESTINATION,
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': emailContent,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            #ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
    else:
        logger.info("Email sent! Message ID:")
        logger.info(response['MessageId'])
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
