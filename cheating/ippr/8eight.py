# 8

import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_equalization(image):
    # Compute histogram 
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    
    # Compute cumulative distribution function
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # Equalize histogram
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    equalized_image = equalized_image.reshape(image.shape)
    
    return equalized_image

# Load input image
input_image = cv2.imread("input_image1.jpg", cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = histogram_equalization(input_image)

# Compute histograms
hist_original, _ = np.histogram(input_image.flatten(), 256, [0, 256])
hist_equalized, _ = np.histogram(equalized_image.flatten(), 256, [0, 256])

# Display original and equalized images and their histograms
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

plt.subplot(2, 2, 3)
plt.plot(hist_original, color='r')
plt.title('Original Histogram')

plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='b')
plt.title('Equalized Histogram')

plt.show()
