import pycurl
import json
from StringIO import StringIO
# from io import StringIO


class InstaPush:
    """
        Provide access to push notification service, provided by InstaPush.
    """

    def __init__(self):
        """ Constructor of this class """
        self.app_id = ""  # Enter your instapush's app id
        self.app_secret = ""  # Enter your instapush's secret key
        self.push_event = "IntruderAlert"
        self.api_url = "https://api.instapush.im/v1/post"

    def request_push_notification(self, message_to_push):
        """
            Send request to Instapush, for sending alert notification
            to registered phones
        """
        response_buffer = StringIO()

        request = {}
        request['event'] = self.push_event
        request['trackers'] = {}
        request['trackers']['message'] = message_to_push
        postfields = json.dumps(request)

        curl = pycurl.Curl()
        curl.setopt(curl.URL, self.api_url)
        curl.setopt(curl.HTTPHEADER, ['x-instapush-appid: ' + self.app_id, 'x-instapush-appsecret: ' + self.app_secret, 'Content-Type: application/json'])
        curl.setopt(curl.POSTFIELDS, postfields)
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.setopt(curl.VERBOSE, True)

        curl.perform()

        response = response_buffer.getvalue()
        response_buffer.truncate(0)
        response_buffer.seek(0)

        curl.close()

        return response
