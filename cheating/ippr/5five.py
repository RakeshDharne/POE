import cv2
import numpy as np

def prewitt_edge_detection(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Prewitt kernels for horizontal and vertical edges
    kernel_x = np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])

    # Convolve kernels with the image
    edges_x = cv2.filter2D(gray_image, -1, kernel_x)
    edges_y = cv2.filter2D(gray_image, -1, kernel_y)

    # Combine horizontal and vertical edges
    edges = cv2.addWeighted(edges_x, 0.5, edges_y, 0.5, 0)

    # Normalize the edges to make them in the range [0, 255]
    edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)

    return edges

# Load the image
image = cv2.imread('input_image.jpg')

# Perform Prewitt edge detection
edges = prewitt_edge_detection(image)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Prewitt Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
