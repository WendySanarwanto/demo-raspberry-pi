import smtplib
import sys
from Utility import get_current_timestamp


class Gmail:
    """
        Provide access to email notification service, provided by Gmail.
        See: http://stackabuse.com/how-to-send-emails-with-gmail-using-python/
    """    

    def __init__(self, sender_email_address, destination_email_address, user, password):
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587
        self.smtp_user = user
        self.smtp_password = password
        self.sender_email_address = sender_email_address
        self.destination_email_address = destination_email_address
        self.email_body_template = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """
    
    def send_alert(self):
        try:
            email_text = self._compose_email_text()

            server = smtplib.SMTP(self.smtp_host, self.smtp_port)    
            server.ehlo()
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.sender_email_address, self.destination_email_address, email_text)
            server.close()

            return "Email notification alert has been sent."
        except:
            return "Unexpected error occurs:", sys.exc_info[0]
        
    def _compose_email_text(self):
        email_body_message = """\
        Hello, 

        One of your IoT Motion Detection device has detected intruders that happened at: %s

        Cheers
        """

        email_body_message = email_body_message % get_current_timestamp()
        email_subject = "[Motion Detection] Intruders detected!"
        email_text = self.email_body_template % (self.sender_email_address, self.destination_email_address, email_subject, email_body_message)
        return email_text
    