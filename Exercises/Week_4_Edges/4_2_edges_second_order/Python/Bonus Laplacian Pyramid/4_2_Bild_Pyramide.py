import matplotlib.pyplot as plt
import numpy as np
import cv2

from scipy.signal import correlate2d

plt.close("all")

image = plt.imread("Saturn_1.jpg")
image = (image - image.min()) / image.max()


def rescale_image(image, rescale_factor):

    target_rows = int(image.shape[0] * rescale_factor)
    target_columns = int(image.shape[1] * rescale_factor)

    rescaled_image = cv2.resize(image, dsize=[target_columns, target_rows])

    return rescaled_image


# =============================================================================
# Maske erstellen
# =============================================================================

laplacian_mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])


binomial_vector = np.array([[1, 6, 15, 20, 15, 6, 1]])
gaussian_mask = binomial_vector * binomial_vector.T

log_filter = correlate2d(gaussian_mask, laplacian_mask, mode="same")
log_filter = log_filter / log_filter.sum()

# =============================================================================
# Main loop
# =============================================================================

stds = []
scale_factors = []


for denominator_power in range(0, 8):
    scale_factor = 1 / (2**denominator_power)

    resized_image = rescale_image(image, rescale_factor=scale_factor)

    log_edges_resized = correlate2d(resized_image, log_filter, mode="same")
    log_edges_resized = log_edges_resized - log_edges_resized.min()
    log_edges_resized = log_edges_resized / log_edges_resized.max()

    std_edges = np.std(log_edges_resized)

    stds.append(std_edges)
    scale_factors.append(scale_factor)

    plt.figure()
    plt.imshow(log_edges_resized, cmap="gray")
    plt.title(f"LoG-Kanten Skalierungs-Faktor {scale_factor}")

stds = np.array(stds)
scale_factors = np.array(scale_factors)


stds_standardised = stds / stds.min()
std_gains = stds_standardised - 1

scores = np.round(std_gains * scale_factors, 4)

for scale_factor, score in zip(scale_factors, scores):
    print(
        f"Bei Skalierungs-Faktor {scale_factor} ist der Kontrast-Gewinn-Score "
        + f"gegenüber dem Original-Bild {score}"
    )

best_scale = scale_factors[scores == scores.max()]

print()
print(
    f"Skalierungs-Faktor mit bestem Kontrast-Gewinn-Score gegenüber Original-Bild: {best_scale}"
)

plt.show()
