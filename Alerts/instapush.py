import pycurl, json
from StringIO import StringIO

"""
    Provide access to push notification service, provided by InstaPush.
"""
class InstaPush:    
    def __init__(self):
        """ Constructor of this class """
        self.app_id = ""
        self.app_secret = ""
        self.push_event = "IntruderAlert"
        self.api_url = "https://api.instapush.im/v1/post"
    

    def request_push_notification(self, message_to_push):
        """ Send request to Instapush, for sending alert notification to registered phones """
        buffer = StringIO()

        request = {}
        request['event'] = self.push_event
        request['trackers'] = {}
        request['trackers']['message'] = message_to_push
        postfields = json.dumps(request)

        curl = pycurl.Curl()
        curl.setopt(curl.URL, self.api_curl)
        curl.setopt(curl.HTTPHEADER, ['x-instapush-appid: ' + self.app_id, 'x-instapush-appsecret: ' + self.app_secret, 'Content-Type: application/json'])
        curl.setopt(curl.POSTFIELDS, postfields)
        curl.setopt(curl.WRITEFUNCTION, buffer.write)
        curl.setopt(curl.VERBOSE, true)       

        curl.perform()

        response = buffer.getvalue()        
        buffer.truncate(0)
        buffer.seek(0)

        curl.cleanup()

        return response
