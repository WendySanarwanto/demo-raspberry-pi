import unittest
import mock
import smtplib

from Gmail import Gmail


class SmtpMock:
    def __init__(self, host, port):
        self.ehlo_is_called = False
        self.starttls_is_called = False
        self.login_is_called = False
        self.sendmail_is_called = False
        self.close_is_called = False

    def ehlo(self):
        self.ehlo_is_called = True

    def starttls(self):
        self.starttls_is_called = True

    def login(self, username, password):
        self.login_is_called = True

    def sendmail(self, sender_mail_address, recipient_mail_addree, email_text):
        self.sendmail_is_called = True

    def close(self):
        self.close_is_called = True

class FailingSmtpMock(SmtpMock):
    def sendmail(self, sender_mail_address, recipient_mail_addree, email_text):
        self.sendmail_is_called = False
        raise Exception("Sending Mail is failing")

# class ExecInfo:
def __getitem__(index):
    result = ["Sending Mail is failing"]
    return result

class GmailTestSuite(unittest.TestCase):
    
    def test_it_should_be_instatiable(self):
        # Arrange
        sender_email_address = "sender@gmail.com"
        destination_email_address = "recipient@gmail.com"
        expected_smtp_host = "smtp.gmail.com"
        expected_smtp_port = 587
        expected_smtp_username = "sender@gmail.com"
        expected_smtp_password = "password"
        expected_email_body_template = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """

        # Act
        gmail = Gmail(sender_email_address, destination_email_address, expected_smtp_username, expected_smtp_password)

        # Assert
        self.assertEqual(gmail.smtp_host, expected_smtp_host)
        self.assertEqual(gmail.smtp_port, expected_smtp_port)
        self.assertEqual(gmail.smtp_user, expected_smtp_username)
        self.assertEqual(gmail.smtp_password, expected_smtp_password)
        self.assertEqual(gmail.email_body_template, expected_email_body_template)
        self.assertEqual(gmail.sender_email_address, sender_email_address)
        self.assertEqual(gmail.destination_email_address, destination_email_address)

    # @patch('smtplib.SMTP')
    @mock.patch('smtplib.SMTP', side_effect=SmtpMock)
    def test_it_should_be_able_sending_alert_mail(self, smtp_mock):
        # Arrange
        sender_email_address = "sender@gmail.com"
        destination_email_address = "recipient@gmail.com"
        smtp_username = "sender@gmail.com"
        smtp_password = "password"
        gmail = Gmail(sender_email_address, destination_email_address, smtp_username, smtp_password)
        expected_response = "Email notification alert has been sent."

        # Act
        response = gmail.send_alert()

        # Assert
        self.assertEqual(response, expected_response)
        self.assertTrue(smtp_mock.ehlo_is_called)
        self.assertTrue(smtp_mock.starttls_is_called)
        self.assertTrue(smtp_mock.login_is_called)
        self.assertTrue(smtp_mock.sendmail_is_called)
        self.assertTrue(smtp_mock.close_is_called)
    
    @mock.patch('smtplib.SMTP', side_effect=FailingSmtpMock)
    @mock.patch('sys.exc_info', side_effect=__getitem__)
    def test_it_should_return_error_when_sending_mail_process_is_failing(self, smtp_mock, exec_info):
        # Arrange
        sender_email_address = "sender@gmail.com"
        destination_email_address = "recipient@gmail.com"
        smtp_username = "sender@gmail.com"
        smtp_password = "password"
        gmail = Gmail(sender_email_address, destination_email_address, smtp_username, smtp_password)
        # expected_response = smtp_mock.exception_message

        # Act
        response = gmail.send_alert()
        # print response 

        # Assert
        # self.assertEqual(response, expected_response)     
        self.assertNotEqual(response, "Email notification alert has been sent.")

# suite = unittest.TestLoader().loadTestsFromTestCase(GmailTestSuite)
# unittest.TextTestRunner(verbosity=2).run(suite)      
# if __name__ == '__main__':
#     unittest.main()