import matplotlib.pyplot as plt
import numpy as np
import cv2

from skimage.feature import peak_local_max

image = plt.imread("X.png")[:, :, 0]

# =============================================================================
# Morphological cleaning
# =============================================================================
kernel = np.ones(shape=[3, 3])

clean_edges = cv2.erode(image, kernel, iterations=2)

# =============================================================================
# Hough
# =============================================================================

# Extract x and y coordinates
all_y, all_x = np.where(clean_edges == 1)

# prepare accumulator
max_b = 4500
b_off_set = int(max_b / 2)  # offset to allow negative b values
accumulator = np.zeros(shape=[max_b, 180])

# fill accumulator
for x, y in zip(all_x, all_y):
    for alpha in range(-90, 90, 1):
        alpha_rad = alpha * np.pi / 180

        b = (np.cos(alpha_rad) * y - np.sin(alpha_rad) * x) / np.cos(alpha_rad)
        b = np.round(b).astype("int64") + b_off_set  # b offset to allow negative values

        if 0 <= b < max_b:
            accumulator[b, alpha + 90] += 1

# find local peaks in accumulator
max_coordinates = peak_local_max(accumulator, min_distance=10, threshold_abs=80)

max_coordinates[:, 0] -= b_off_set  # correct for offset from accumulator
max_coordinates[:, 1] -= 90  # correct for offset from accumulator
print(max_coordinates)

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original Image")

plt.figure()
plt.imshow(clean_edges, cmap="gray")
plt.title("Eroded lines")

plt.figure()
plt.imshow(
    np.power(accumulator, 1 / 2), aspect=accumulator.shape[1] / accumulator.shape[0]
)
plt.title("3rd root of Accumulator (for better Visualization)")

plt.figure()

plt.imshow(image, cmap="gray")
column_end = image.shape[1] - 1
for b, angle in zip(max_coordinates[:, 0], max_coordinates[:, 1]):
    angle_rad = angle / 180 * np.pi

    row_start = b
    row_end = np.sin(angle_rad) / np.cos(angle_rad) * column_end + b

    plt.plot([0, column_end], [row_start, row_end])

    # xmin, xmax, ymin, ymax
plt.axis([0, column_end, image.shape[0] - 1, 0])
plt.title("Detected lines on original image")

plt.figure()
plt.imshow(clean_edges, cmap="gray")

for b, angle in zip(max_coordinates[:, 0], max_coordinates[:, 1]):
    angle_rad = angle / 180 * np.pi

    row_start = b
    row_end = np.sin(angle_rad) / np.cos(angle_rad) * column_end + b

    plt.plot([0, column_end], [row_start, row_end])

# xmin, xmax, ymin, ymax
plt.axis([0, column_end, image.shape[0] - 1, 0])
plt.title("Detected lines on eroded lines")

plt.show()
