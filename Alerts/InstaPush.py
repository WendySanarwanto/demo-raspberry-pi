import pycurl
import json
from StringIO import StringIO
# from io import StringIO
from ..Utility import Curl

class InstaPush:
    """
        Provide access to push notification service, provided by InstaPush.
    """

    def __init__(self):
        """ Constructor of this class """
        self.app_id = ""  # Enter your instapush's app id
        self.app_secret = ""  # Enter your instapush's secret key
        self.push_event = "IntruderAlert"
        #self.api_url = "https://api.instapush.im/v1/post"
        self.api_url = "https://api.instapush.im/v1"
        self.push_notification_path = "/post"

    def request_push_notification(self, message_to_push):
        """
            Send request to Instapush, for sending alert notification
            to registered phones
        """
        request = {}
        request['event'] = self.push_event
        request['trackers'] = {}
        request['trackers']['message'] = message_to_push

        http_headers = ['x-instapush-appid: ' + self.app_id, 'x-instapush-appsecret: ' + self.app_secret, 'Content-Type: application/json']

        curl = Curl(api_url, True, True)

        return curl.do_post(request, http_headers, self.push_notification_path)
