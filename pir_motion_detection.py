# A sample that demonstrate Motion Detection
# through using PIR as the sensor, on Raspberry Pi
# Instructions:
# 1. Install pyCurl library: `sudo apt-get install python-pycurl
# 2. Run the program: `pyton pir*.py`
# 3. Start this program as a SystemD Daemon: See instructions in `daemon/lib/systemd/system/motion_detection.service`

import time
import datetime
import RPi.GPIO as GPIO

from Alerts import InstaPush
from Sensors import PIR


def compose_alert_message():
    """ A helper for composing messages to displays in sent alerts """
    now = datetime.datetime.now()
    current_timestamp = now.strftime("%A, %d. %B %Y %I:%M%p")
    message = "\n Intruders detected  !\n Timestamp: " + current_timestamp
    message += "\n"
    return message


def push_notification(alert_message):
    """ A helper for pushing alert to registered iOS/Android devices """
    insta_push = InstaPush()
    response = insta_push.request_push_notification(alert_message)
    print(("D push notification's response = " + str(response)))


def on_intruders_detected():
    """
        A helper for generating actions to execute,
        when intruders are detected
    """
    alert_message = compose_alert_message()
    print(alert_message)

    try:
        #send push notification to iOS / Android
        push_notification(alert_message)
    except:
        print("Unexpected error when sending alert.")


    # TODO: Do alerts or other actions here, for some time

    # TODO: Implement actions against intruders.
    #   Options:
    #       1. Send push notification to iOS / Android phone.
    #       2. Send email
    #       3. Tweet
    #       4. Turn on camera module, then capture picture/short video against
    #          the intruders and sent it to iOS/Android Phones
    #       5. Many more

# Main program
def main():
    sensor = PIR(GPIO.BOARD, False)
    try:
        current_state = 0
        previous_state = 0
        ready_message = "\n Ready ...\n"

        print("\n Waiting for PIR to settle ...\n")
        while sensor.do_read() == 1:
            current_state = 0
            print(ready_message)

        while True:
            current_state = sensor.do_read()
            #print "D current_state= " + str(current_state)
            if current_state == 1 and previous_state == 0:
                on_intruders_detected()
                previous_state = 1
            elif current_state == 0 and previous_state == 1:
                print(ready_message)
                previous_state = 0
                time.sleep(0.001)

    except KeyboardInterrupt:
        print("\n Quit")
        sensor.do_cleanup()

if __name__ == '__main__':
    main()
