# A sample that demonstrate Motion Detection
# through using PIR as the sensor, on Raspberry Pi

import time
import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO_PIR = 11
GPIO.setup(GPIO_PIR, GPIO.IN)     # Read output from PIR motion sensor


# A helper for reading value on GPIO pin that is connected to PIR's output PIN
def read_pir():
    return GPIO.input(GPIO_PIR)


# A helper for composing messages to displays in sent alerts
def compose_alert_message():
    current_timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    return "Intruders detected  ! Timestamp: " + current_timestamp


# A helper for generating 
# Actions to execute when intruders are detected
def on_intruders_detected():        
    alert_message = compose_alert_message();
    print(alert_message)
    
    # TODO: Do alerts or other actions here, for some time
    
    # TODO: Implement actions against intruders.
    #   Options:
    #       1. Send push notification to iOS / Android phone.
    #       2. Send email
    #       3. Tweet
    #       4. Turn on camera module, then capture picture/short video against
    #          the intruders and sent it to iOS/Android Phones
    #       5. Many more
    return "Implement this"

# Main program
try:
    current_state = 0
    previous_state = 0

    print("Waiting for PIR to settle ...")
    while read_pir() == 1:
        current_state = 0
        print("	Ready")

    while True:
        current_state = read_pir()
        #print "D current_state= " + str(current_state)
        if current_state == 1 and previous_state == 0:
            on_intruders_detected()
            previous_state = 1
        elif current_state == 0 and previous_state == 1:
            print("	Ready")
            previous_state = 0
            time.sleep(0.001)

except KeyboardInterrupt:
    print("	Quit")
    GPIO.cleanup()
