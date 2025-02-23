import matplotlib.pyplot as plt
import numpy as np

from median_mean_filter import median_filter, mean_filter

plt.close("all")

image = plt.imread("cameraman.bmp")


# =============================================================================
# Generate noise and apply it
# =============================================================================

noise = np.random.randint(-20, 30, size=image.shape)

noisy_image = image + noise


# =============================================================================
# Filtering
# =============================================================================

median_image = median_filter(noisy_image, filter_radius=1)
mean_image = mean_filter(noisy_image, filter_radius=1)


# =============================================================================
# Plotting
# =============================================================================

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("original image")

plt.figure()
plt.imshow(noisy_image, cmap="gray")
plt.title("Noisy image")

plt.figure()
plt.imshow(median_image, cmap="gray")
plt.title("Median Filter")

plt.figure()
plt.imshow(mean_image, cmap="gray")
plt.title("Mittelwert Filter")


plt.show()
