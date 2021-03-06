# A sample that demonstrate Motion Detection
# through using PIR as the sensor, on Raspberry Pi
# Instructions:
# 1. Install pyCurl library: `sudo apt-get install python-pycurl
# 2. Run the program: `pyton pir*.py`
# 3. Start this program as a SystemD Daemon: See instructions in `daemon/lib/systemd/system/motion_detection.service`

import time
import RPi.GPIO as GPIO

from Alerts.Mailers import MailGun
from Sensors import PIR
from Utility import get_current_timestamp


def send_email():
    """ A helper for sending alert as email, via mailgun """

    # TODO: Get email's provider from configuration
    domain = ""  # TODO: Write down your mail gun's domain
    api_key = ""   # TODO: Write down the API key here
    sender_name = ""  # TODO: Write down sender's name (e.g. admin, john)
    sender_full_name = ""  # TODO: Write down sender's full name (e.g. my company's admin, John Doe)
    recipient_name = ""  # TODO: Write down recipient's name (e.g. Jane Doe)
    email_client = MailGun(domain, api_key)

    _from = "%s<%s@%s>" % (sender_full_name, sender_name, domain)
    to = "" # TODO: Write down the recipient's email address (e.g. john.doe@gmail.com)
    subject = "[Motion Detection] Intruders detected !"
    text = """ \
    Hello %s,

    One of your Motion Detection IoT Device has sensed movement of intruders within its sensory range, at: %s.

    Cheers.
    Next Research's Administrator
    """ % (recipient_name, get_current_timestamp())

    return email_client.send_mail(_from, to, subject, text)


def on_intruders_detected():
    """
        A helper for generating actions to execute,
        when intruders are detected
    """
    try:
        # Output to console terminal
        print(("Intruders Detected ! Timestamp: %s \n"
                % get_current_timestamp()))

        #TODO: send push notification to iOS / Android

        #send email alert
        response = send_email()
        print(("Sending alert's Response: %s" % response))
    except:
        print(("Unexpected error happened when sending alert at: " % get_current_timestamp()))


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
