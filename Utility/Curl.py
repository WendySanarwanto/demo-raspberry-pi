import pycurl
import json
from StringIO import StringIO
# from io import StringIO


class Curl:
    """
        Provide methods for invoking REST API Resources through using Curl.
    """

    def __init__(self, api_url, verbose=True, enable_ipv4=False):
        """ Constructor of this class """
        self.api_url = api_url
        self.verbose = verbose
        self.enable_ipv4 = enable_ipv4

    def do_post(self, request, http_headers, resource_path):
        """ Invoke API Resource whose HTTP verb is POST. """
        response_buffer = StringIO()
        postfields = json.dumps(request)
        full_api_path = self.api_url + resource_path

        curl = pycurl.Curl()
        curl.setopt(curl.URL, full_api_path)
        curl.setopt(curl.HTTPHEADER, http_headers)
        curl.setopt(curl.POSTFIELDS, postfields)
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.setopt(curl.VERBOSE, self.verbose)
        if (self.enable_ipv4):
            curl.setopt(curl.IPRESOLVE, curl.IPRESOLVE_V4)

        curl.perform()

        response = response_buffer.getvalue()
        response_buffer.truncate(0)
        response_buffer.seek(0)

        curl.close()

        return response
