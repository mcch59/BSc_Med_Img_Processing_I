import matplotlib.pyplot as plt
import numpy as np

from filter_functions import low_pass_filter

image = plt.imread("demo_images/Linien.png")

fft = np.fft.fftshift(np.fft.fft2(image))

low_passed_image = low_pass_filter(image)

fft_filtered = fft.copy()

# Korrektur im Frequenzraum
fft_filtered[125, 125] = 0

image_filtered = np.abs(np.fft.ifft2(fft_filtered))

plt.figure()
plt.imshow(image, cmap="gray", vmin=0, vmax=1)
plt.title("Ortsraum")

plt.figure()
plt.imshow(np.log(np.abs(fft)))
plt.title("Frequenzraum")

plt.figure()
plt.imshow(low_passed_image, cmap="gray")
plt.title("Tiefpass-gefiltertes Bild")

plt.figure()
plt.imshow(image_filtered, cmap="gray", vmin=0, vmax=1)
plt.title("Gefiltertes Bild")
plt.show()
