import cv2

def scale_image(image, scale_factor):
    # Calculate new dimensions
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)

    # Resize the image
    scaled_image = cv2.resize(image, (new_width, new_height))

    return scaled_image

# Load the image
image = cv2.imread('input_image.jpg')

# Scale the image by a factor of 2
scaled_image_2x = scale_image(image, 2)

# Scale the image by a factor of 0.5
scaled_image_05x = scale_image(image, 0.5)

# Display the original and scaled images
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Image 2x', scaled_image_2x)
cv2.imshow('Scaled Image 0.5x', scaled_image_05x)
cv2.waitKey(0)
cv2.destroyAllWindows()

