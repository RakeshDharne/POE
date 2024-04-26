# 3


import numpy as np
import cv2

def rgb_to_cmy(image):
    # Convert RGB to CMY 
    c = 1 - (image[:, :, 2] / 255.0)
    m = 1 - (image[:, :, 1] / 255.0)
    y = 1 - (image[:, :, 0] / 255.0)
    
    # Stack CMY channels
    cmy_image = np.stack((c, m, y), axis=-1)
    
    return cmy_image

# Load input RGB image
input_image = cv2.imread("input_image1.jpg")

# Convert RGB to CMY
cmy_image = rgb_to_cmy(input_image)

# Resize images to half of their original size
input_image_resized = cv2.resize(input_image, (0,0), fx=0.5, fy=0.5)
cmy_image_resized = cv2.resize((cmy_image * 255).astype(np.uint8), (0,0), fx=0.5, fy=0.5 )

# Display input RGB and CMY images in half-size windows
cv2.imshow("Input RGB Image", input_image_resized)
cv2.imshow("CMY Image", cmy_image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

