import cv2
import numpy as np

# Load the grayscale image
gray_image = cv2.imread('grayscale_image.png', cv2.IMREAD_GRAYSCALE)

# Define the intensity range to be highlighted
low_intensity = 100
high_intensity = 200

# Apply intensity slicing while preserving the background
output_image_non_preserve_bg = np.zeros_like(gray_image, dtype=np.uint8)  # Initialize output image
foreground_mask = (gray_image >= low_intensity) & (gray_image <= high_intensity)
output_image_non_preserve_bg[foreground_mask] = 255  # Set intensity-sliced foreground pixels to 255

# Combine intensity-sliced foreground with original background
output_image_preserve_bg = cv2.addWeighted(gray_image, 0.5, output_image_non_preserve_bg, 0.5, 0)

# Display the original image, intensity sliced image, and combined image
cv2.imshow('Original Image', gray_image)
cv2.imshow('Intensity Sliced Image (Non-Preserve Background)', output_image_non_preserve_bg)
# cv2.imshow('Intensity Sliced Image (Preserve Background)', output_image_preserve_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
