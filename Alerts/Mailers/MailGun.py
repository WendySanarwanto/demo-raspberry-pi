import requests


class MailGun:
    """
        Provide methods for accessing mailing services provided by MailGun (https://www.mailgun.com/)
    """

    def __init__(self, domain, api_key):
        """ Constructor of 'MailGunClient' class"""
        self.api_url = "https://api.mailgun.net/v3/%s" % domain
        # print "api_url = %s" % self.api_url
        self.messages_resource_path = "/messages"
        self.api_key = api_key

    def send_mail(self, _from, to, subject, text):
        """
            Compose email message by specified 'from' email address, recipient's email address(es), subject and text
        """
        response = ""
        try:
            response = requests.post(
                        self.api_url + self.messages_resource_path,
                        auth=("api", self.api_key),
                        data={"from": _from,
                            "to": to,
                            "subject": subject,
                            "text": text})
        except Exception, exception:
            response = exception.message
        return response
