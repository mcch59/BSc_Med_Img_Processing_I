import matplotlib.pyplot as plt
import numpy as np
import cv2
import scipy

image = plt.imread("Streifen.jpg")

image = np.sum(image, axis=-1) / 3


def mean_filtering(image, filter_shape):
    mean_filter = np.ones(shape=filter_shape)
    mean_filter = mean_filter / np.sum(mean_filter)

    smoothed_image = scipy.signal.fftconvolve(image, mean_filter, mode="same")

    return smoothed_image


# =============================================================================
# Resizing
# =============================================================================

resize_factor = 0.15

target_rows = int(resize_factor * image.shape[0])
target_columns = int(resize_factor * image.shape[1])


smoothed_image = mean_filtering(image, filter_shape=[7, 7])

resized_image = cv2.resize(smoothed_image, dsize=[target_columns, target_rows])
resized_image_moire = cv2.resize(image, dsize=[target_columns, target_rows])

# =============================================================================
# Plotting
# =============================================================================

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(resized_image, cmap="gray")
plt.title("Resized image with filtering")

plt.figure()
plt.imshow(resized_image_moire, cmap="gray")
plt.title("Resized image")

plt.show()
