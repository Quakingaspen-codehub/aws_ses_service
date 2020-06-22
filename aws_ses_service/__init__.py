import boto3
import os
from email.mime.multipart import MIMEMultipart


class Email:
    client = boto3.client('ses',region_name=os.environ['region_name'])

    def __init__(self, sender, receiver, subject, body=list(), attachments=list()):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.attachments = attachments

    def send(self):
        # Creat
        email = self.create_the_email()
        self.setup_email_body(email)
        self.setup_email_attachments(email)

        # Send
        Email.client.send_raw_email(Source=self.sender, Destinations=self.receiver,
                                    RawMessage={'Data': email.as_string()})

    def create_the_email(self):
        email = MIMEMultipart('mixed')
        email['Subject'] = self.subject
        email['From'] = self.sender

        return email

    def setup_email_body(self, email):
        email_body = MIMEMultipart('alternative')

        for body_obj in self.body:
            email_body.attach(body_obj.encode())

        email.attach(email_body)

    def setup_email_attachments(self, email):
        for attachment in self.attachments:
            email.attach(attachment.get_attachment_object())

# from aws_ses_service import Email
# from aws_ses_service.body import EmailTextBody
# from aws_ses_service.attachment import EmailPathAttachment
# from resource.email import EmailSenders
# text_body = EmailTextBody('It is done')
# path_attachment = EmailPathAttachment('D:\QA\[1] Utility\Comms Analysis\Code\dummy.jpg')
#
# email = Email(EmailSenders.team, ['samersallam92@gmail.com', 'samer@quakingaspen.net'], 'Hi From Sealr',
#               body=[text_body], attachments=[path_attachment])
# email.send()
