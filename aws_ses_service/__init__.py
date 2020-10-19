import boto3
import os
from email.mime.multipart import MIMEMultipart
import email.utils as EmailUtils


class Email:
    client = boto3.client('ses', region_name=os.environ['AWS_REGION_NAME'])

    def __init__(self, sender_email, sender_name, receiver, subject, body=list(), attachments=list()):
        self.sender_email = sender_email
        self.sender_name = sender_name
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
        Email.client.send_raw_email(Source=self.sender_email, Destinations=self.receiver,
                                    RawMessage={'Data': email.as_string()})

    def create_the_email(self):

        email = MIMEMultipart('mixed')
        email['Subject'] = self.subject
        email['From'] = EmailUtils.formataddr((self.sender_name,
                                               self.sender_email))

        # email = MIMEMultipart('mixed')
        # email['Subject'] = self.subject
        # email['From'] = self.sender

        return email

    def setup_email_body(self, email):
        email_body = MIMEMultipart('alternative')

        for body_obj in self.body:
            email_body.attach(body_obj.encode())

        email.attach(email_body)

    def setup_email_attachments(self, email):
        for attachment in self.attachments:
            email.attach(attachment.get_attachment_object())


class SingleEmail(Email):

    def create_the_email(self):
        email = super().create_the_email()

        email['To'] = self.receiver[0]

        return email


class BroadcastEmail(Email):
    pass

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
