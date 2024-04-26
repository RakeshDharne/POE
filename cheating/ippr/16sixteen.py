# 16

import numpy as np
import cv2

def normalize_image(image):
    # Convert image to floating point
    image = image.astype(np.float32)
    
    # Normalize image
    # image_normalized = 255* (image - np.min(image)) / (np.max(image) - np.min(image))

    image_normalized = (image - np.min(image)) / (np.max(image) - np.min(image))
     
    return image_normalized

# Load input image
input_image = cv2.imread("input_image1.jpg", cv2.IMREAD_GRAYSCALE) 
 
# Normalize image
normalized_image = normalize_image(input_image)
 
# Resize images to half of their original size
input_image_resized = cv2.resize(input_image, (0,0), fx=0.5, fy=0.5)
normalized_image_resized = cv2.resize(normalized_image, (0,0), fx=0.5, fy=0.5)

# Display input and normalized images in half-size windows
cv2.imshow("Input Image", input_image_resized)
cv2.imshow("Normalized Image", normalized_image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



