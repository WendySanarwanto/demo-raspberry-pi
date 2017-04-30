# Unit tests of MailGun class
import mock
import requests
import uuid
from Alerts.Mailers import MailGun

# Shared test variables
success_response = "<Response [200]>"
domain = "mydomain.com"
api_key_part = str(uuid.uuid4()).strip('-')
api_key = "key-%s" % api_key_part
_from = "Admin<admin@%s>" % domain
to = "mymail@gmail.com"
subject = "Test mail"
text = """ \
Hello, \n

This mail is sent from a python program through MailGun API. \n
Therefore, no need to reply this mail. \n

Cheers.\n
My Domain's Administrator
"""
email_client = MailGun(domain, api_key)

def test_should_be_able_sending_email_successfully(monkeypatch):
    # Arrange
    def mocked_send_email_return(url, auth, data):
        return success_response

    monkeypatch.setattr(requests, 'post', mocked_send_email_return)
        
    # Act
    response = email_client.send_mail(_from, to, subject, text)

    # Assert
    assert response == success_response

def test_should_return_error_response_when_sending_email_is_failing(monkeypatch):
    # Arrange
    def mocked_send_email_return(url, auth, data):
        raise Exception("Sending email is failing")

    monkeypatch.setattr(requests, 'post', mocked_send_email_return)

    # Act
    response = email_client.send_mail(_from, to, subject, text)

    # Assert
    assert response != success_response