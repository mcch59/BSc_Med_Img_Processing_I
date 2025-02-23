import matplotlib.pyplot as plt
import numpy as np

from scipy.signal import correlate2d
import cv2

plt.close("all")


image = plt.imread("Saturn_1.jpg")

# image = np.sum(image[:,:,:3], axis = -1)/3

image = (image - image.min()) / image.max()


def rescale_image(image, rescale_factor):

    target_rows = int(image.shape[0] * rescale_factor)
    target_columns = int(image.shape[1] * rescale_factor)

    rescaled_image = cv2.resize(image, dsize=[target_columns, target_rows])

    return rescaled_image


resized_image = rescale_image(image, rescale_factor=0.5)


laplace_filter = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

binomial_vector = np.array([[1, 6, 15, 20, 15, 6, 1]])
# binomial_vector = np.array([[1, 2, 1]])
# binomial_vector = np.array([[1, 4, 6, 4, 1]])

gauss_filter = binomial_vector * binomial_vector.T
log_filter = correlate2d(gauss_filter, laplace_filter, mode="same")

log_edges = correlate2d(image, log_filter, mode="same")

log_edges_resized = correlate2d(resized_image, log_filter, mode="same")


# plt.figure()
# plt.imshow(image, cmap = "gray")
# plt.title("Original image")

# plt.figure()
# plt.imshow(resized_image, cmap = "gray")
# plt.title("Rescaled image")

plt.figure()
plt.imshow(log_edges, cmap="gray")
plt.title("LoG edges original image")

plt.figure()
plt.imshow(log_edges_resized, cmap="gray")
plt.title("Rescaled image LoG edges")

# =============================================================================
# Beurteilung
# =============================================================================

log_edges_flattened = log_edges.flatten()
log_edges_flattened = log_edges_flattened - log_edges_flattened.min()
log_edges_flattened = log_edges_flattened / log_edges_flattened.max()


log_edges_resized_flattened = log_edges_resized.flatten()
log_edges_resized_flattened = (
    log_edges_resized_flattened - log_edges_resized_flattened.min()
)
log_edges_resized_flattened = (
    log_edges_resized_flattened / log_edges_resized_flattened.max()
)

plt.figure()
_, _, _ = plt.hist(log_edges_flattened, bins=256)

plt.figure()
_, _, _ = plt.hist(log_edges_resized_flattened, bins=256)


print(f"Varianz Kanten Original-Bild: {np.std(log_edges_flattened)}")
print(f"Varianz Kanten Resized-Bild: {np.std(log_edges_resized_flattened)}")

plt.show()
