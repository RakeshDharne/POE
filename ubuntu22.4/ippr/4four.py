import cv2
import numpy as np

def edge_detection(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Sobel operator for edge detection
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute the magnitude of gradients
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Normalize the magnitude to range [0, 255]
    magnitude = np.uint8(magnitude)
    
    return magnitude

# Load the color image
image = cv2.imread('input_image.jpg')

# Perform edge detection
segmented_image = edge_detection(image)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
