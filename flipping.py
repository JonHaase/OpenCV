# USAGE
# python flipping.py --image florida_trip.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# read pixel value


# flip the image horizontally
flipped = cv2.flip(image, 1)
# read pixel value
(b, g, r) = image[259, 235]
cv2.imshow("Flipped Horizontally", flipped, "blue", b, "green", g, "red", r)



# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)