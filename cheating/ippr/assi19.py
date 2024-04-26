import cv2
import numpy as np

# Load the RGB image
rgb_image = cv2.imread('img.jpg')

# Check if the image is loaded successfully
if rgb_image is None:
    print("Error: Unable to load the RGB image.")
else:
    # Split the image into color channels
    blue_channel, green_channel, red_channel = cv2.split(rgb_image)

    # Choose the color channel to enhance (e.g., blue channel)
    channel_to_enhance = blue_channel  # Change this to green_channel or red_channel as needed

    # Define the enhancement factor
    enhancement_factor = 1.5  # Adjust this factor as needed

    # Enhance the chosen color channel by multiplying with the enhancement factor
    enhanced_channel = np.clip(channel_to_enhance * enhancement_factor, 0, 255).astype(np.uint8)

    # Merge the enhanced channel with the original green and red channels
    enhanced_image = cv2.merge((blue_channel, enhanced_channel, red_channel))

    # Save the enhanced image
    cv2.imwrite('enhanced_image.jpg', enhanced_image)

    print("Enhanced image saved as enhanced_image.jpg")
