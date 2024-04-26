import cv2
import numpy as np

def translate_image(image, x_shift, y_shift):
    # Define translation matrix
    M = np.float32([[1, 0, x_shift], [0, 1, y_shift]])

    # Apply translation
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return translated_image

# Load the image
image = cv2.imread('input_image1.jpg')

# Shift the image to the right by 20 units
translated_image_right = translate_image(image, 20, 0)

# Shift the image downwards by 10 units
translated_image_down = translate_image(image, 0, 10)

# Display the original and translated images
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image Right', translated_image_right)
cv2.imshow('Translated Image Down', translated_image_down)
cv2.waitKey(0)
cv2.destroyAllWindows()
