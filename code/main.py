import mimetypes


def send_email(emailContent)
    from_mail = 'noreply-eli@gmail.com'
    to_mail = 'eliezerj8@gmail.com'

    s = smtplib.SMTP('host.docker.internal')
    subject = 'Eli Yaacov - Viz home test'
    print("Sending mail to %s", to_mail)

    message = f"""\
          Subject: {subject}
          To: {to_mail}
          From: {from_mail}
          {emailContent}"""
    result = s.sendmail(from_mail, to_mail, message)
    s.quit()
    

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
    print("File results is: %s", res)
    send_email(res)
