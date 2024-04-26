import cv2
import numpy as np

def enhance_yellow(image, enhancement_factor):
    # Split the image into individual channels
    channels = list(cv2.split(image))

    # Apply enhancement to the red and green channels (to increase yellow)
    channels[0] = np.clip(channels[0] * enhancement_factor, 0, 255).astype(np.uint8)  # Red channel
    channels[1] = np.clip(channels[1] * enhancement_factor, 0, 255).astype(np.uint8)  # Green channel

    # Merge the enhanced red and green channels with the original blue channel
    enhanced_image = cv2.merge(channels)

    return enhanced_image

# Load the 24-bit RGB image
image = cv2.imread('input_image.jpg')

# Define the enhancement factor (adjust as needed)
enhancement_factor = 1.5  # Example enhancement factor

# Enhance the yellow color in the image
enhanced_image = enhance_yellow(image, enhancement_factor)

# Display the original and enhanced images
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
