import cv2
import numpy as np

# Load the original image
original_image = cv2.imread('input_image.jpg')

# Save the original image dimensions
height, width = original_image.shape[:2]

# Define the compression quality factor (0-100)
quality_factor = 90  # You can adjust this value as needed

# Encode and save the image with JPEG compression
cv2.imwrite('compressed_image.jpg', original_image, [int(cv2.IMWRITE_JPEG_QUALITY), quality_factor])

# Decode the compressed image
decompressed_image = cv2.imread('compressed_image.jpg')

# Calculate PSNR
mse = np.mean((original_image - decompressed_image) ** 2)
psnr = 10 * np.log10((255 ** 2) / mse)

# Display original and decompressed images along with PSNR value
cv2.imshow('Original Image', original_image)
cv2.imshow('Decompressed Image', decompressed_image)
print(f"PSNR value: {psnr} dB")
cv2.waitKey(0)
cv2.destroyAllWindows()
