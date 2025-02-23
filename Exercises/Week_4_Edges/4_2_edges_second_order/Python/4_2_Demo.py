import matplotlib.pyplot as plt 
import numpy as np
import cv2

from scipy.signal import correlate2d



image = plt.imread("Saturn_1.jpg")

resized_image = cv2.resize(image, dsize=[400, 200])


# =============================================================================
# Filter erstellen
# =============================================================================
laplace_filter = np.array([[-1, -1, -1], 
                           [-1,  8, -1], 
                           [-1, -1, -1]])

binomial_vector = np.array([[1, 6, 15, 20, 15, 6, 1]])

binomial_filter = binomial_vector * binomial_vector.T
binomial_filter = binomial_filter/binomial_filter.sum()

log_filter = correlate2d(binomial_filter, laplace_filter, mode = "same")


# =============================================================================
# Kanten detektieren
# =============================================================================
laplace_edges = correlate2d(image, laplace_filter, mode = "same")
log_edges = correlate2d(image, log_filter, mode = "same")

laplace_edges_resized = correlate2d(resized_image, laplace_filter, mode = "same")
log_edges_resized = correlate2d(resized_image, log_filter, mode = "same")

# =============================================================================
# Plotting
# =============================================================================
plt.figure()
plt.imshow(laplace_edges, cmap = "gray")
plt.title("Original size, laplace edges")

plt.figure()
plt.imshow(log_edges, cmap = "gray")
plt.title("Original size, LoG edges")

plt.figure()
plt.imshow(laplace_edges_resized, cmap = "gray")
plt.title("Resized image, laplace edges")

plt.figure()
plt.imshow(log_edges_resized, cmap = "gray")
plt.title("Resized image, LoG edges")


plt.show()

