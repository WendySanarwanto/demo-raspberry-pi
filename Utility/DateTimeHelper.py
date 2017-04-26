import time
import datetime


def get_current_timestamp():
    now = datetime.datetime.now()
    current_timestamp = current_timestamp = now.strftime("%A, %d. %B %Y %I:%M%p")
    return current_timestamp
                    