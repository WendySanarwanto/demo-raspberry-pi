# A sample that demonstrate Motion Detection
# through using PIR as the sensor, on Raspberry Pi

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO_PIR = 11
GPIO.setup(GPIO_PIR, GPIO.IN)     # Read output from PIR motion sensor

current_state = 0
previous_state = 0


# A helper for reading value on GPIO pin that is connected to PIR's output PIN
def read_pir():
    return GPIO.input(GPIO_PIR)

# Main program
try:
    print("Waiting for PIR to settle ...")
    while read_pir() == 1:
        current_state = 0
        print("	Ready")

    while True:
        current_state = read_pir()
        #print "D current_state= " + str(current_state)
        if current_state == 1 and previous_state == 0:
            print("	Intruders detected!")
            # TODO: Do alerts or other actions here, for some time
            previous_state = 1
        elif current_state == 0 and previous_state == 1:
            print("	Ready")
            previous_state = 0
            time.sleep(0.001)

except KeyboardInterrupt:
    print("	Quit")
    GPIO.cleanup()
