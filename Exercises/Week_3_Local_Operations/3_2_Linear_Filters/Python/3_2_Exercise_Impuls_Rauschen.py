import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import correlate2d

lower_threshold = -0.995
upper_threshold = 0.995

noise = (np.random.rand(100, 100) - 0.5) * 2  # von 0 bis 1

noise_mask_lower_threshold = noise > lower_threshold  # binary mask
noise_mask_upper_threshold = noise < upper_threshold  # binary mask

# binary mask, only values between thresholds
noise_mask_zero = noise_mask_lower_threshold * noise_mask_upper_threshold

# mask for values to be turned into negative impulses
noise_mask_negative = noise < lower_threshold

# mask for values to be turned into positive impulses
noise_mask_positive = noise > upper_threshold

noise[noise_mask_zero] = 0
noise[noise_mask_negative] = -1
noise[noise_mask_positive] = 1


# Filters


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


mean_filtered_noise = mean_filter(noise, filter_radius=1)
median_filtered_noise = median_filter(noise, filter_radius=1)

# binomial filter as approximation to gauss filter
binomial_filter = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
binomial_filter = binomial_filter / binomial_filter.sum()
binomial_filtered_noise = correlate2d(noise, binomial_filter)

plt.figure()
plt.imshow(noise, cmap="gray", vmin=-1, vmax=1)

plt.figure()
plt.imshow(mean_filtered_noise, cmap="gray", vmin=-1, vmax=1)
plt.title("Mean filtered Impulse Noise")

plt.figure()
plt.imshow(median_filtered_noise, cmap="gray", vmin=-1, vmax=1)
plt.title("Median filtered Impulse Noise")

plt.figure()
plt.imshow(binomial_filtered_noise, cmap="gray", vmin=-1, vmax=1)
plt.title("Gaussian filtered Impulse Noise")

plt.show()
