# Count Object

This repo contains a python script, `count.py`, that counts red, blue, and green
objects in an image.

## Demo

1. Split a color image into three images - reb, blue and green.

For example, here's the image for blue:

![](https://raw.githubusercontent.com/heronyang/count-object/main/blue.jpg)

2. Per each single color image:

a) Convert to black and white image.

![](https://raw.githubusercontent.com/heronyang/count-object/main/blue_binary.jpg)

b) Remove noises (small dots).

![](https://raw.githubusercontent.com/heronyang/count-object/main/blue_blur.jpg)

c) Find contours and count them.

![](https://raw.githubusercontent.com/heronyang/count-object/main/blue_circled.jpg)
