import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the two grayscale images
image1 = cv2.imread('input_image2.png', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('input_image2.png', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded successfully
if image1 is None or image2 is None:
    print("Error: Failed to load images.")
else:
    # Resize images to the same dimensions if necessary
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    # Perform addition of two images
    add_result = cv2.add(image1, image2)

    # Perform subtraction of two images
    sub_result = cv2.subtract(image1, image2)

    # Display the original and arithmetic result images
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))

    # Original images
    axes[0, 0].imshow(image1, cmap='gray')
    axes[0, 0].set_title('Image 1')
    axes[0, 0].axis('off')

    axes[0, 1].imshow(image2, cmap='gray')
    axes[0, 1].set_title('Image 2')
    axes[0, 1].axis('off')

    # Addition result
    axes[1, 0].imshow(add_result, cmap='gray')
    axes[1, 0].set_title('Addition Result')
    axes[1, 0].axis('off')

    # Subtraction result
    axes[1, 1].imshow(sub_result, cmap='gray')
    axes[1, 1].set_title('Subtraction Result')
    axes[1, 1].axis('off')

    plt.tight_layout()
    plt.show()
