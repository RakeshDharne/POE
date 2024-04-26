import cv2

def canny_edge_detection(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)  # Adjust thresholds as needed

    return edges

# Load the image
image = cv2.imread('input_image.jpg')

# Perform Canny edge detection
edges = canny_edge_detection(image)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
