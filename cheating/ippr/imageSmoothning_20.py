import cv2

# Load the noisy image
noisy_image = cv2.imread('sample.jpeg')

# Apply Gaussian blur
smooth_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)  # You can adjust the kernel size (5, 5) for more or less smoothing

# Display the original and smoothed images
cv2.imshow('Noisy Image', noisy_image)
cv2.imshow('Smooth Image', smooth_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
