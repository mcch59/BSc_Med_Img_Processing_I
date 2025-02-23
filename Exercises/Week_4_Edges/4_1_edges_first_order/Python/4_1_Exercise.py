import matplotlib.pyplot as plt
import numpy as np
import scipy

plt.close("all")

image = plt.imread("Zebrastreifen.jpg")

image = (image - image.min()) / image.max()


# =============================================================================
# image pre-processing
# =============================================================================
def mean_filter(image, mask_shape=(3, 3)):

    mask = np.ones(shape=mask_shape)
    mask = mask / np.sum(mask)
    smoothed_image = scipy.signal.correlate2d(image, mask, mode="same")

    return smoothed_image


def median_filter(image, filter_radius):

    smoothed_image = np.zeros(shape=image.shape)

    for row in range(filter_radius, image.shape[0] - filter_radius):
        for column in range(filter_radius, image.shape[1] - filter_radius):
            smoothed_image[row, column] = np.median(
                image[
                    row - filter_radius : row + filter_radius + 1,
                    column - filter_radius : column + filter_radius + 1,
                ]
            )

    return smoothed_image


image = mean_filter(image, mask_shape=[11, 11])
# image = median_filter(image, filter_radius = 5)
# =============================================================================
# Masken definieren
# =============================================================================
x_filter = np.array(
    [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ]
)

y_filter = np.array(
    [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ]
)

diagonal_filter = np.array(
    [
        [0, -1, -2, -3, 0],
        [-1, -2, -3, 0, 3],
        [-2, -3, 0, 3, 2],
        [-3, 0, 3, 2, 1],
        [0, 3, 2, 1, 0],
    ]
)

# =============================================================================
# Kanten detektieren
# =============================================================================
x_edges = scipy.signal.correlate2d(image, x_filter, mode="same")
y_edges = scipy.signal.correlate2d(image, y_filter, mode="same")

gm = np.sqrt(x_edges**2 + y_edges**2)

diagonal_edges = scipy.signal.correlate2d(image, diagonal_filter, mode="same")
diagonal_edges = np.sqrt(diagonal_edges**2)

# =============================================================================
# binarization
# =============================================================================

gm_binary = gm > 0.2
diagonal_edges_binary = diagonal_edges > 1.2

# =============================================================================
# Plotten
# =============================================================================
plt.figure()
plt.imshow(image, cmap="gray")
plt.title("original image")

plt.figure()
plt.imshow(gm, cmap="gray")
plt.title("gradient magnitude")

plt.figure()
plt.imshow(diagonal_edges, cmap="gray")
plt.title("Diagonal edges")

plt.figure()
plt.imshow(gm_binary, cmap="gray")
plt.title("Binary gradient magnitude edges")

plt.figure()
plt.imshow(diagonal_edges_binary, cmap="gray")
plt.title("Binary diagonal edges")

plt.show()
