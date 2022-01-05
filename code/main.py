import mimetypes
import smtplib
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
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
    
    
    #Sending email logic
    from_mail = 'noreply-eli@gmail.com'
    to_mail = 'eliezerj8@gmail.com'

    s = smtplib.SMTP('172.17.0.1')
    subject = 'Eli Yaacov - Viz home test'

    message = f"""\
          Subject: {subject}
          To: {to_mail}
          From: {from_mail}
          {emailContent}"""
    result = s.sendmail(from_mail, to_mail, message)
    s.quit()
    logger.info(f'Sent email with content - {emailContent} , results are: {result}')
    context.done()
