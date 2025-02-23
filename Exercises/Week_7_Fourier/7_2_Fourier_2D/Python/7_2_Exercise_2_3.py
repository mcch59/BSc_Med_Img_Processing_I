import matplotlib.pyplot as plt
import numpy as np

from filter_functions import low_pass_filter, high_pass_filter, band_pass_filter


image = plt.imread("brain_images/Brain.png")
fft = np.fft.fftshift(np.fft.fft2(image))

low_passed_image = low_pass_filter(image)
high_passed_image = high_pass_filter(image)
band_passed_image = band_pass_filter(image)


# Plotting
plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original Bild")

plt.imshow(np.log(np.abs(fft)))
plt.title("Logarithmisch aufgetragenes Frequenzspektrum")

plt.figure()
plt.imshow(low_passed_image, cmap="gray")
plt.title("Tiefpass Bild Sub-Optimal")

plt.figure()
plt.imshow(high_passed_image, cmap="gray")
plt.title("Hochpass Bild Sub-Optimal")

plt.figure()
plt.imshow(band_passed_image, cmap="gray")
plt.title("Bandpass Bild Sub-Optimal")

plt.show()
