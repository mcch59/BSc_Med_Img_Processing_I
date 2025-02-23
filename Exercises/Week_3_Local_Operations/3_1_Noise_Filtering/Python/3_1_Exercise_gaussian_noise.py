import matplotlib.pyplot as plt
import numpy as np

image = plt.imread("Saturn.jpg")

gaussian_noise = np.random.randn(image.shape[0], image.shape[1]) * 30

image = image.astype(float)

noisy_image = image + gaussian_noise

# Rauschen zieht Werte ausserhalb uint8-Wertebereich
noisy_image[noisy_image < 0] = 0
noisy_image[noisy_image > 255] = 255
noisy_image = noisy_image.astype("uint8")

# Filter definieren


def mean_filter(image, filter_radius):
    new_image = np.zeros(shape=image.shape)
    for row in range(filter_radius, image.shape[0] - filter_radius):
        for column in range(filter_radius, image.shape[1] - filter_radius):
            new_image[row, column] = np.mean(
                image[
                    row - filter_radius : row + filter_radius + 1,
                    column - filter_radius : column + filter_radius,
                ]
            )
    return new_image


def median_filter(image, filter_radius):
    new_image = np.zeros(shape=image.shape)
    for row in range(filter_radius, image.shape[0] - filter_radius):
        for column in range(filter_radius, image.shape[1] - filter_radius):
            new_image[row, column] = np.median(
                image[
                    row - filter_radius : row + filter_radius + 1,
                    column - filter_radius : column + filter_radius,
                ]
            )
    return new_image


mean_filtered_image = mean_filter(noisy_image, filter_radius=3)
median_filtered_image = median_filter(noisy_image, filter_radius=3)


# Plotten
plt.figure()
plt.imshow(noisy_image, cmap="gray")
plt.title("Noisy image")

plt.figure()
plt.imshow(mean_filtered_image, cmap="gray")
plt.title("Mean filtered image")

plt.figure()
plt.imshow(median_filtered_image, cmap="gray")
plt.title("Median filtered image")


plt.show()
