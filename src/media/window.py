#!/usr/bin/env python3
"""
A small curses window to display images and ascii videos.
"""
import time

from media.images import ImageParser
from PIL import Image, ImageShow
import cv2
from cv2 import VideoCapture
from time import sleep
import datetime as dt


def print_ascii(ascii_string):
    print(ascii_string)


def read_camera(cam):
    return cam.read()


def main():
    cam = VideoCapture(0)
    sleep(0.1)  # The webcam take a small time interval to warm up, else it returns black images.
    start = dt.datetime.now()
    # for i in range(10):
    while (dt.datetime.now() - start < dt.timedelta(seconds=5)):
        successful, image_array = read_camera(cam)
        assert successful, "We were unable to capture the image from the camera."
        parser = ImageParser(image=image_array)
        parser.resize(abs_width=100)
        ascii_string = parser.as_ascii(border=" ", invert=True)
        print_ascii(ascii_string)
    cam.release()


if __name__ == "__main__":
    main()
