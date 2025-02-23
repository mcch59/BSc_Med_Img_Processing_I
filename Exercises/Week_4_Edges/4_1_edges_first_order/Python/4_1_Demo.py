import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate2d

image = plt.imread("Achteck.png")

image = (image - image.min()) / image.max()


x_filter_mask = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ]
)

y_filter_mask = np.array(
    [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ]
)


# =============================================================================
# Mittelwertfilter
# =============================================================================
mean_filter = np.ones(shape=[3, 3]) / 9
smoothed_image = correlate2d(image, mean_filter, mode="same")


x_edges = correlate2d(image, x_filter_mask, mode="same")
y_edges = correlate2d(image, y_filter_mask, mode="same")

gradient_magnitude = np.sqrt(x_edges**2 + y_edges**2)

binary_gradient_magnitude = gradient_magnitude > 1

gradient_orientation = np.arctan2(y_edges, x_edges) * (180 / 3.1415926)


plt.figure()
plt.imshow(image, cmap="gray")

plt.figure()
plt.imshow(x_edges, cmap="gray")

plt.figure()
plt.imshow(y_edges, cmap="gray")

plt.figure()
plt.imshow(gradient_magnitude, cmap="gray")

plt.figure()
plt.imshow(binary_gradient_magnitude, cmap="gray")

plt.figure()
plt.imshow(gradient_orientation, cmap="Spectral")

plt.show()
