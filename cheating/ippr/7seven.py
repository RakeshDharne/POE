import cv2
import matplotlib.pyplot as plt

def plot_rgb_histogram(image):
    # Split the image into individual channels
    channels = cv2.split(image)

    # Compute histograms for each channel
    hist_r = cv2.calcHist([channels[0]], [0], None, [256], [0,256])
    hist_g = cv2.calcHist([channels[1]], [0], None, [256], [0,256])
    hist_b = cv2.calcHist([channels[2]], [0], None, [256], [0,256])

    # Plot histograms
    plt.figure(figsize=(10, 5))
    plt.subplot(3, 1, 1)
    plt.plot(hist_r, color='r')
    plt.title('Red Channel Histogram')
    plt.xlim([0, 256])

    plt.subplot(3, 1, 2)
    plt.plot(hist_g, color='g')
    plt.title('Green Channel Histogram')
    plt.xlim([0, 256])

    plt.subplot(3, 1, 3)
    plt.plot(hist_b, color='b')
    plt.title('Blue Channel Histogram')
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()

# Load the image
image = cv2.imread('input_image.jpg')

# Display histograms for individual RGB channels
plot_rgb_histogram(image)

