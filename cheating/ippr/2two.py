import cv2
import numpy as np

def get_negative(image):
    # Invert each color channel separately
    negative_image = 255 - image
    return negative_image

# Load the color image
image = cv2.imread('input_image.jpg')

# Get the negative of the image
negative_image = get_negative(image)

# Display the original and negative images
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
