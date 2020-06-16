import os
from abc import ABCMeta, abstractmethod
from email.mime.application import MIMEApplication
from aws_s3_resource.s3_object import S3Object


class EmailAttachment(metaclass=ABCMeta):
    def __init__(self, attachment):
        self.attachment = attachment

    @abstractmethod
    def get_attachment_object(self):
        pass


class EmailPathAttachment(EmailAttachment):
    def get_attachment_object(self):
        # attachment is a file path in this case

        with open(self.attachment, 'rb') as f:
            att = MIMEApplication(f.read())
            att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.attachment))

        return att


class EmailS3ObjectAttachment(EmailAttachment):
    bucket_name = 'test-test'
    file_path = 'test'

    @classmethod
    def change_bucket_path_name(cls, new_bucket_name):
        cls.bucket_name = new_bucket_name

    def get_attachment_object(self):
        # attachment is an s3_object in this case
        object_key = f'{EmailS3ObjectAttachment.file_path}\{self.attachment}'
        file_bytes = S3Object.download(EmailS3ObjectAttachment.bucket_name, object_key)
        att = MIMEApplication(file_bytes)
        att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.attachment))
        return att



