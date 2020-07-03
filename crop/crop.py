# USAGE
# python crop.py

# import the necessary packages
import cv2

# load the image and show it
image = cv2.imread("florida_trip.png")
cv2.imshow("Original", image)

# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
# crop from Y start: y finish, x start: x finish
face = image[173:235, 13:81]
cv2.imshow("Face", face)
cv2.waitKey(0)

face = image[124:212, 225:380]
cv2.imshow("Face", face)
cv2.waitKey(0)

face = image[90:450, 0:290]
cv2.imshow("Face", face)
cv2.waitKey(0)

# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)