import cv2

# Load the grayscale image
gray_image = cv2.imread('grayscale_image.png', cv2.IMREAD_GRAYSCALE)

# Define the threshold value
threshold_value = 127  # You can adjust this value as needed

# Apply binary thresholding
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the original and binary images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
