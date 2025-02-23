import numpy as np
import cv2

from frequency_filter_mask import generate_2D_gaussian


def high_pass_filter(image):
    """High pass filter for 2D images by eliminating lower frequencies with binary mask
    Steps:
    1. Calculate frequency space with 2D Fourier transform.
    2. Calculate the indices for the binary filter mask. Frequencies in the middle of the image are to be eliminated.
    3. Create the filter mask as a one-matrix. (By default we keep all frequencies)
    4. Set the mask to zero where the lower frequencies occur. (Discard lower frequencies)
    5. Multiply the original frequency spectrum with the binary filter mask.
    6. Apply inverse 2D Fourier transform to get the filtered image.
    Returns:
        array: high passed image
    """
    fft = np.fft.fftshift(np.fft.fft2(image))

    row_lower = int(fft.shape[0] * 0.47)
    row_upper = int(fft.shape[0] * 0.53)
    column_lower = int(fft.shape[1] * 0.47)
    column_upper = int(fft.shape[1] * 0.53)

    filter_mask = np.ones(shape=fft.shape)
    filter_mask[row_lower:row_upper, column_lower:column_upper] = 0

    fft_filtered = fft * filter_mask

    high_passed_image = np.abs(np.fft.ifft2(fft_filtered))

    return high_passed_image


def low_pass_filter(image):
    """Low pass filter for 2D images by eliminating higher frequencies with binary mask.
    1. Calculate frequency space with 2D Fourier transform.
    2. Calculate the indices for the binary filter mask. Frequencies in the middle of the image are to be kept.
    3. Create the filter mask as a zero-matrix. (By default we discard all frequencies)
    4. Set the mask to one where the lower frequencies occur. (Only keep lower frequencies)
    5. Multiply the original frequency spectrum with the binary filter mask.
    6. Apply inverse 2D Fourier transform to get the filtered image.
    Returns:
        array: low passed image
    """

    fft = np.fft.fftshift(np.fft.fft2(image))

    filter_mask = np.zeros_like(fft)

    row_lower = int(fft.shape[0] * 0.4)
    row_higher = int(fft.shape[0] * 0.6)
    column_lower = int(fft.shape[1] * 0.4)
    column_higher = int(fft.shape[1] * 0.6)

    filter_mask[row_lower:row_higher, column_lower:column_higher] = 1

    fft_filtered = filter_mask * fft

    low_passed_image = np.abs(np.fft.ifft2(fft_filtered))

    return low_passed_image


def band_pass_filter(image):
    """Band pass filter for 2D images by eliminating higher and lower frequencies with binary mask.
    1. Calculate frequency space with 2D Fourier transform.
    2. Calculate the indices for the binary filter mask. The idea is to create a filter mask that allows frequencies up to a high frequency and then discard the lower ones from that mask afterwards.
    3. Create the filter mask as a zero-matrix. (By default we discard all frequencies)
    4. Set the mask to one up to the higher frequency.
    5. Set the mask to zero up to the lower frequency.
    6. Multiply the original frequency spectrum with the binary filter mask.
    7. Apply inverse 2D Fourier transform to get the filtered image.
    Returns:
        array: band passed image
    """

    fft = np.fft.fftshift(np.fft.fft2(image))

    # Indices for higher frequencies
    row_lower_h = int(fft.shape[0] * 0.2)
    row_upper_h = int(fft.shape[0] * 0.8)
    column_lower_h = int(fft.shape[1] * 0.2)
    column_upper_h = int(fft.shape[1] * 0.8)

    # Indices for lower frequency
    row_lower_l = int(fft.shape[0] * 0.45)
    row_upper_l = int(fft.shape[0] * 0.55)
    column_lower_l = int(fft.shape[1] * 0.45)
    column_upper_l = int(fft.shape[1] * 0.55)

    filter_mask = np.zeros(shape=fft.shape)
    filter_mask[row_lower_h:row_upper_h, column_lower_h:column_upper_h] = 1
    filter_mask[row_lower_l:row_upper_l, column_lower_l:column_upper_l] = 0

    fft_filtered = fft * filter_mask
    band_passed_image = np.abs(np.fft.ifft2(fft_filtered))
    return band_passed_image


def better_low_pass_filter(image, kernel_sigma):
    """Better low pass filter that avoids artifacts

    Instead of using a binary filter mask that abruptly cuts off frequencies, using a smooth gaussian filter mask results in better filtered images.

    Steps:

    1. Calculate  frequency spectrum through 2D Fourier transform.
    2. Generate a 2D Gaussian array.
    3. Fit the 2D Gaussian array to the fft to match the sizes.
    4. Multiply the frequency spectrum with the 2D Gaussian array to keep only lower frequencies but with smooth transitions between frequencies.
    5. Inverse 2D Fourier transform to get the filtered image.

    Returns:
        array: low passed image
    """
    fft = np.fft.fftshift(np.fft.fft2(image))

    kernel = generate_2D_gaussian(size=fft.shape[0], sigma=kernel_sigma)
    kernel = cv2.resize(kernel, dsize=[fft.shape[1], fft.shape[0]])

    filtered_image = np.abs(np.fft.ifft2(fft * kernel))

    return filtered_image


def better_high_pass_filter(image, kernel_sigma):
    """Better high pass filter that avoids artifacts

    Instead of using a binary filter mask that abruptly cuts off frequencies, using a smooth gaussian filter mask results in better filtered images.

    Steps:

    1. Calculate  frequency spectrum through 2D Fourier transform.
    2. Generate a 2D Gaussian array.
    3. Fit the 2D Gaussian array to the fft to match the sizes.
    4. Invert the Gaussian array. 0 in the middle, gradually turning into 1 towards edges
    4. Multiply the frequency spectrum with the inverted 2D Gaussian array to keep only higher frequencies but with smooth transitions between frequencies.
    5. Inverse 2D Fourier transform to get the filtered image.

    Returns:
        array: low passed image
    """
    fft = np.fft.fftshift(np.fft.fft2(image))

    kernel = generate_2D_gaussian(size=fft.shape[0], sigma=kernel_sigma)
    kernel = cv2.resize(kernel, dsize=[fft.shape[1], fft.shape[0]])
    kernel_inv = np.abs(kernel - kernel.max())

    filtered_image = np.abs(np.fft.ifft2(fft * kernel_inv))

    return filtered_image
