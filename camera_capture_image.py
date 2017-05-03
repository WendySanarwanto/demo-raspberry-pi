# -*- coding: utf-8 -*-

import os
import time

from Utility import DateTimeHelper
from picamera import PiCamera

###############
## Constants ##
###############

rotation = 180
resolution = (400, 300)
warm_up_time = 2
brightness = 60
captured_image_folder_name = "Pictures"

##################
# Helper methods #
##################


def get_captured_image_path(captured_image_folder_name):
    """Build the path of captured image file. The path will be under \
       $HOME directory and the captured image file will be named as \
       timestamp of when the image was captured. """
    home_location = os.environ['HOME']
    filename = DateTimeHelper.get_current_timestamp()
    images_location = \
        "%s/%s/%s.jpg"
    return images_location % (home_location,
        captured_image_folder_name, filename)


# Main Program
# def main():

# Instantiate piCamera object
camera = PiCamera()
camera.rotation = rotation
camera.resolution = resolution
camera.brightness = brightness
#camera.exposure_mode = "night"

# Define captured image's path
captured_image_path = get_captured_image_path(captured_image_folder_name)

# Perform image capture
try:
    print("Start capturing image ...")
    camera.start_preview()
    time.sleep(warm_up_time)
    camera.capture(captured_image_path)

    print("Done. Closing camera.")
finally:
    camera.close()
    print("Camera is closed.")

#if __name__ == '__main__':
#    main()