import cv2
import numpy as np

# Load the original image
original_image = cv2.imread('img.jpg')

# Convert the image to YUV color space (DCT is typically applied to luminance channel)
yuv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2YUV)

# Apply DCT to the Y channel (luminance)
dct_y_channel = cv2.dct(np.float32(yuv_image[:,:,0]))

# Apply inverse DCT to retrieve the image
idct_image = cv2.idct(dct_y_channel)

# Clip values to valid range (0-255)
reconstructed_image = np.clip(idct_image, 0, 255)

# Convert back to 8-bit unsigned integer
reconstructed_image = np.uint8(reconstructed_image)

# Convert to BGR color space
reconstructed_image_bgr = cv2.cvtColor(reconstructed_image, cv2.COLOR_GRAY2BGR)

# Calculate PSNR
mse = np.mean((original_image - reconstructed_image_bgr) ** 2)
psnr = 10 * np.log10((255 ** 2) / mse)

# Display original and reconstructed images along with PSNR value
cv2.imshow('Original Image', original_image)
cv2.imshow('Reconstructed Image', reconstructed_image_bgr)
print(f"PSNR value: {psnr} dB")
cv2.waitKey(0)
cv2.destroyAllWindows()
