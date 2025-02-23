import matplotlib.pyplot as plt
import numpy as np
import cv2

from skimage.feature import peak_local_max

image = plt.imread("Kantenmaske_Zebrastreifen.png")

# =============================================================================
# Pre-processing
# =============================================================================
kernel = np.ones(shape=[3, 3])
clean_edges = cv2.erode(image, kernel=kernel, iterations=1)

# =============================================================================
# Hough
# =============================================================================
# Extract coordinates
all_y, all_x = np.where(clean_edges == 1)

# Accumulator

accumulator = np.zeros(shape=[2000, 180])


for x, y in zip(all_x, all_y):
    for alpha in range(-90, 90, 1):
        alpha_rad = alpha * np.pi / 180

        b = y - (np.sin(alpha_rad) / np.cos(alpha_rad) * x)
        b = int(np.round(b))

        if 0 <= b < accumulator.shape[0]:
            accumulator[b, alpha + 90] += 1  # off-set damit alpha positiv

# Find clusters in accumulator
max_coordinates = peak_local_max(accumulator, min_distance=20, threshold_abs=50)

max_coordinates[:, 1] -= 90  # off-set rausnehmen

# =============================================================================
# Plotting
# =============================================================================
plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original Bild")

plt.figure()
plt.imshow(clean_edges, cmap="gray")
plt.title("Erodierte Kanten")

plt.figure()
plt.imshow(accumulator, aspect=accumulator.shape[1] / accumulator.shape[0])

plt.figure()
plt.imshow(image, cmap="gray")

last_column = image.shape[1] - 1
for b, angle in zip(max_coordinates[:, 0], max_coordinates[:, 1]):

    angle_rad = angle * np.pi / 180

    y_end = (np.sin(angle_rad) / np.cos(angle_rad) * last_column) + b

    plt.plot([0, last_column], [b, y_end])

plt.axis([0, last_column, image.shape[0] - 1, 0])

plt.show()
