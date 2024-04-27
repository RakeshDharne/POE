import cv2
import numpy as np

# Load the two grayscale images
image1 = cv2.imread('grayscale_image.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('grayscale_image2.png', cv2.IMREAD_GRAYSCALE)

# Check if the images are loaded successfully
if image1 is None or image2 is None:
    print("Error: Unable to load one or both of the images.")
else:
    # Resize the images to have the same dimensions
    height, width = min(image1.shape[0], image2.shape[0]), min(image1.shape[1], image2.shape[1])
    image1_resized = cv2.resize(image1, (width, height))
    image2_resized = cv2.resize(image2, (width, height))

    # Perform addition of two images
    addition_result = cv2.add(image1_resized, image2_resized)

    # Perform subtraction of two images
    subtraction_result = cv2.subtract(image1_resized, image2_resized)

    # Display the original images and the results
    cv2.imshow('Image 1', image1_resized)
    cv2.imshow('Image 2', image2_resized)
    cv2.imshow('Addition Result', addition_result)
    cv2.imshow('Subtraction Result', subtraction_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
