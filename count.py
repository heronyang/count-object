#!/usr/bin/env python3
"""
This script counts the number of objects in red, blue, and green of an image.

The steps include:

    1. Split a color image into three images - reb, blue and green.
    2. Per each single color image:
        a) Convert to black and white image.
        b) Remove noises (small dots).
        c) Find contours and count them.

To run this script:

$ pip3 install opencv-python
$ python3 count.py
"""
import cv2
import numpy as np

INPUT_FILENAME = 'input.jpg'
SENSITIVITY_THRESHOLD = 100
NOISE_THRESHOLD = 1


def generate_blur_and_circled_image(name, image):
    _, binary_image = cv2.threshold(image, SENSITIVITY_THRESHOLD, 255,
                                    cv2.THRESH_OTSU)
    cnts = cv2.findContours(binary_image, cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]
    blur_image = cv2.medianBlur(binary_image, NOISE_THRESHOLD)
    circled_image = count_and_circle_objects(name, blur_image)

    # Saves images to disk.
    cv2.imwrite(name + ".jpg", image)
    cv2.imwrite(name + "_binary.jpg", binary_image)
    cv2.imwrite(name + "_blur.jpg", blur_image)
    cv2.imwrite(name + "_circled.jpg", circled_image)

    return blur_image, circled_image


def count_and_circle_objects(name, image):
    circled_image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_NONE)
    # Circles the objects.
    for contour in contours:
        cv2.drawContours(circled_image, [contour], 0, (0, 0, 255), 1)
    print('Found ' + str(len(contours)) + ' objects in ' + name + '.')

    return circled_image


def generate_overlap_image(image1, image2):
    overlapped_image = cv2.bitwise_and(image1, image2)
    cv2.imwrite("overlapped.jpg", overlapped_image)

    overlapped_circled_image = count_and_circle_objects(
        "overlapped", overlapped_image)
    cv2.imwrite("overlapped_circled.jpg", overlapped_circled_image)


def main():
    image = cv2.imread(INPUT_FILENAME)
    blue_image, _, red_image = cv2.split(image)

    blue_blur_image, _ = generate_blur_and_circled_image("blue", blue_image)
    red_blur_image, _ = generate_blur_and_circled_image("red", red_image)

    generate_overlap_image(blue_blur_image, red_blur_image)


if __name__ == "__main__":
    main()
