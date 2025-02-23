import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import correlate2d

plt.close("all")

image = plt.imread("Zebra.jpg")

# =============================================================================
# Filtermaske definieren
# =============================================================================

# mean_filter = np.array([[1,1,1],
#                         [1,1,1],
#                         [1,1,1]])

mean_filter = np.ones(shape=[5, 5])
mean_filter = mean_filter / mean_filter.sum()


binomial_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

binomial_filter = binomial_filter / binomial_filter.sum()

mean_image = correlate2d(image, mean_filter, mode="same")

binomial_filtered_image = correlate2d(image, binomial_filter, mode="same")

# =============================================================================
# Unscharf Maskierung
# =============================================================================

sharpness = image - mean_image

sharpened_image = image + sharpness * 2

plt.figure()
plt.imshow(image, cmap="gray")

plt.figure()
plt.imshow(mean_image, cmap="gray")
plt.title("Mean filter")

plt.figure()
plt.imshow(binomial_filtered_image, cmap="gray")
plt.title("Binomial filter")

plt.figure()
plt.imshow(sharpness, cmap="gray")
plt.title("Sharpness")

plt.figure()
plt.imshow(sharpened_image, cmap="gray", vmin=0, vmax=255)
plt.title("Unscharf Maskierung")

plt.show()
