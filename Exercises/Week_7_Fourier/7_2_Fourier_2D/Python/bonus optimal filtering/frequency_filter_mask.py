import numpy as np
import matplotlib.pyplot as plt


def generate_2D_gaussian(size, sigma):
    """Generate a square 2D array with  Gaussian distribution.
    Credits go to: https://stackoverflow.com/users/6465762/clemisch

    Args:
        size (int or float): desired height/width of the square 2D Gaussian
        sigma (int or float): standard deviation of Gauss distribution

    Returns:
        array: 2D Gaussian distribution
    """
    x = np.linspace(-(size - 1) / 2.0, (size - 1) / 2.0, size)

    gauss_dist_1D = 1 / (2 * np.pi * np.sqrt(sigma)) * np.exp(-1 / 2 * (x / sigma) ** 2)
    gauss_dist_1D = gauss_dist_1D[:, None]

    gaussian_matrix = gauss_dist_1D * gauss_dist_1D.T
    gaussian_matrix = gaussian_matrix / gaussian_matrix.max()
    plt.figure()
    plt.imshow(gaussian_matrix)
    plt.title("Gaussian matrix for filtering")
    return gaussian_matrix
