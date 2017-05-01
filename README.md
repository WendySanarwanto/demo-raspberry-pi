# demo-raspberry-pi
A collection of raspberry pi's sample programs, taken from internet (e.g. youtube), which demonstrate PI's features such as taking inputs from attached sensors and camera.

## List of samples
* `pir-motion-detection.py` - Python code sample which demonstrate motion detection through using a PIR Sensor that is attached to one of Raspberry Pi's GPIO pins. Reference: https://www.youtube.com/watch?v=cpR4VxnGzew. Below are prerequisites & steps of how to run this demo in your Raspberry Pi:
    * Ensure that you have connected the PIR Sensor to you Raspberry Pi's GPIO pins as folow (see Raspbery PI GPIO's Reference in  http://pi4j.com/pins/model-2b-rev1.html ):
        * Wire PIR Sensor's VCC pin to GPIO's Pin #4
        * Wire PIR sensor's GND pin to GPIO's Pin #6
        * Wire PIR Sensor's OUT pin to GPIO's Pin #11
    * Install `requests` library: `sudo pip install -U requests`.
    * Clone this repository: `git clone https://github.com/WendySanarwanto/demo-raspberry-pi.git`
    * Change directory to location of the cloned repository then run `python pir_motion_detection.py` to start the program.


