import RPi.GPIO as GPIO


class PIR:
    """
        Provide services to read outputs from attached PIR Sensor
    """

    def __init__(self, gpio_mode, gpio_warnings):
        """ Constructor of this class """
        # initialise the GPIO
        GPIO.setwarnings(gpio_warnings)
        GPIO.setmode(gpio_mode)
        self.GPIO_PIR = 11  # GPIO Pin's number, attached to PIR's output rail.
        GPIO.setup(self.GPIO_PIR, GPIO.IN)  # Read output from PIR motion sensor

    def do_read(self):
        """ Reading value on GPIO pin, that is connector to PIR's output rail. """
        return GPIO.input(self.GPIO_PIR)

    def do_cleanup(self):
        """ de-initialise claimed GPIO's resources """
        GPIO.cleanup()
