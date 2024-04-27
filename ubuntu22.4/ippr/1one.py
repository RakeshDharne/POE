
import cv2
import numpy as np

def get_negative(image):
    # Invert the pixel values
    negative_image = 255 - image
    return negative_image

# Load the grayscale image
image = cv2.imread('input_image2.png', cv2.IMREAD_GRAYSCALE)

# Get the negative of the image
negative_image = get_negative(image)

# Display the original and negative images
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
