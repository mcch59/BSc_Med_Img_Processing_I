import matplotlib.pyplot as plt
import numpy as np

# define filters


def min_filter(image, filter_radius):
    new_image = np.zeros(shape=image.shape)
    for row in range(filter_radius, image.shape[0] - filter_radius):
        for column in range(filter_radius, image.shape[1] - filter_radius):
            new_image[row, column] = np.min(
                image[
                    row - filter_radius : row + filter_radius + 1,
                    column - filter_radius : column + filter_radius,
                ]
            )
    return new_image


def max_filter(image, filter_radius):
    new_image = np.zeros(shape=image.shape)
    for row in range(filter_radius, image.shape[0] - filter_radius):
        for column in range(filter_radius, image.shape[1] - filter_radius):
            new_image[row, column] = np.max(
                image[
                    row - filter_radius : row + filter_radius + 1,
                    column - filter_radius : column + filter_radius,
                ]
            )
    return new_image


image = plt.imread("Saturn.jpg")
print(image.shape)

# apply filters
image_min = min_filter(image, filter_radius=1)
image_max = max_filter(image, filter_radius=1)

# plotting
plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(image_min, cmap="gray")
plt.title("Minimum filtered image")

plt.figure()
plt.imshow(image_max, cmap="gray")
plt.title("Maximum filtered image")

plt.show()
