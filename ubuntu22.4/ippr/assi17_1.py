import cv2
import numpy as np

# Load the grayscale image
gray_image = cv2.imread('grayscale_image.png', cv2.IMREAD_GRAYSCALE)

# Define the intensity range to be highlighted
low_intensity = 100
high_intensity = 200

# Apply intensity slicing while preserving the background
output_image_preserve_bg = np.copy(gray_image)
output_image_preserve_bg[(gray_image >= low_intensity) & (gray_image <= high_intensity)] = 255

# Display the original and sliced images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Intensity Sliced Image (Preserve Background)', output_image_preserve_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
