# USAGE
# python simple_thresholding.py --image coins01.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)

# apply basic thresholding -- the first parameter is the image
# we want to threshold, the second value is is our threshold
# check; if a pixel value is greater than our threshold (in this
# case, 200), we set it to be BLACK, otherwise it is WHITE.


# (T, thresh) = cv2.threshold(blurred, 95, 0, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Bin for T = {}".format, thresh)

thresh_vars = [95, 15, 50, 10]
for i in thresh_vars:
    (T, thresh) = cv2.threshold(blurred, i, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold Bin for T = {}".format(i), thresh)
cv2.waitKey(0)

