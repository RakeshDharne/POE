import cv2
import pywt
import numpy as np

# Load the original image
original_image = cv2.imread('img.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply DWT
coeffs = pywt.dwt2(gray_image, 'haar')
cA, (cH, cV, cD) = coeffs

# Apply inverse DWT to retrieve the image
reconstructed_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')

# Convert reconstructed image back to uint8
reconstructed_image = np.uint8(reconstructed_image)

# Calculate PSNR
mse = np.mean((gray_image - reconstructed_image) ** 2)
psnr = 10 * np.log10((255 ** 2) / mse)

# Display original and reconstructed images along with PSNR value
cv2.imshow('Original Image', gray_image)
cv2.imshow('Reconstructed Image', reconstructed_image)
print(f"PSNR value: {psnr} dB")
cv2.waitKey(0)
cv2.destroyAllWindows()
