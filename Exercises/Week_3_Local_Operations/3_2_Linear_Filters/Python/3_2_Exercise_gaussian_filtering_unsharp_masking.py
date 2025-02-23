import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate2d

image = plt.imread("Saturn_1.jpg").astype(float)

# Filter erstellen
binomial_vector = np.array([[1, 6, 15, 20, 15, 6, 1]])

gaussian_filter_mask = binomial_vector * binomial_vector.T
gaussian_filter_mask = gaussian_filter_mask / np.sum(gaussian_filter_mask)

# Filter anwenden
filtered_image = correlate2d(image, gaussian_filter_mask, mode="same")

# Unsharp masking
sharpness = image - filtered_image

sharpened_image = image + 2 * sharpness

plt.figure()
plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Original image")

plt.figure()
plt.imshow(filtered_image, cmap="gray", vmin=0, vmax=255)
plt.title("Filtered image")

plt.figure()
plt.imshow(sharpness, cmap="gray")
plt.title("Sharpness")

plt.figure()
plt.imshow(sharpened_image, cmap="gray", vmin=0, vmax=255)
plt.title("Sharpened image")

plt.show()
