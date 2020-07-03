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

cv2.imshow("Flipped Horizontally", flipped)


# rotate 45 counter-cw
# grab the dimensions of the image and calculate the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
 
# rotate our image by 45 degrees
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(flipped, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# flip the image vertically
flipped_vert = cv2.flip(rotated, 0)
cv2.imshow("Flipped Vertically", flipped_vert)

# # flip the image along both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
(b, g, r) = flipped_vert[189, 441]
print( "blue", b, "green", g, "red", r)