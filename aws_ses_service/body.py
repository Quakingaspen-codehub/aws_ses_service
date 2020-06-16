from abc import ABCMeta, abstractmethod
from email.mime.text import MIMEText


class EmailBody(metaclass=ABCMeta):
    def __init__(self, body_content):
        self.body_content = body_content

    @abstractmethod
    def encode(self):
        pass


class EmailTextBody(EmailBody):
    def encode(self):
        return MIMEText(self.body_content.encode("utf-8"), 'plain', "utf-8")


class EmailHTMLBody(EmailBody):
    def encode(self):
        return MIMEText(self.body_content.encode("utf-8"), 'html', "utf-8")
