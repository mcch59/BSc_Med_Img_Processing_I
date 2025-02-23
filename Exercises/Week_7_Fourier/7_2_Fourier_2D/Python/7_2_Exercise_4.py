import matplotlib.pyplot as plt
import numpy as np
import scipy

"""
Filtering of noisy image 1
"""
noisy_image_1 = plt.imread("brain_images/noisy_image_1.png")

fft_1 = np.fft.fftshift(np.fft.fft2(noisy_image_1))
fft_mask_1 = np.zeros(fft_1.shape, dtype=int)

fft_mask_1[87, 81] = 1
fft_mask_1[57, 56] = 1
fft_mask_1[27, 31] = 1
fft_mask_1[147, 131] = 1
fft_mask_1[177, 156] = 1
fft_mask_1[207, 181] = 1
fft_mask_1[232, 6] = 1
fft_mask_1[3, 206] = 1

# Frequencies around selected frequencies are filtered too to make sure the artifact is removed
fft_mask_1 = scipy.signal.correlate2d(fft_mask_1, np.ones(shape=[3, 3]), mode="same")
fft_mask_1 = fft_mask_1 > 0

fft_1[fft_mask_1 == 1] = 1

reconstructed_image = np.abs(np.fft.ifft2(fft_1))

plt.figure()
plt.imshow(fft_mask_1)
plt.title("Bild 1: Maske zum Entfernen der Artefakte")

plt.figure()
plt.imshow(np.log(np.abs(fft_1)))
plt.title("Bild 1: Logarithmisch aufgetragenes Frequenz Spektrum nach Filterung")

plt.figure()
plt.imshow(noisy_image_1, cmap="gray")
plt.title("Bild 1: Bild mit Artefakten")

plt.figure()
plt.imshow(reconstructed_image, cmap="gray")
plt.title("Bild 1: Gefiltertes Bild")


"""
Filtering of noisy image 2
"""
noisy_image_2 = plt.imread("brain_images/noisy_image_2.png")

fft_2 = np.fft.fftshift(np.fft.fft2(noisy_image_2))
fft_mask_2 = np.zeros(fft_2.shape, dtype=int)

fft_mask_2[157, 106] = 1
fft_mask_2[197, 106] = 1
fft_mask_2[227, 106] = 1
fft_mask_2[77, 106] = 1
fft_mask_2[47, 106] = 1
fft_mask_2[7, 106] = 1

# Frequencies around selected frequencies are filtered too to make sure the artifact is removed
fft_mask_2 = scipy.signal.correlate2d(fft_mask_2, np.ones(shape=[3, 3]), mode="same")
fft_mask_2 = fft_mask_2 > 0

fft_2[fft_mask_2 == 1] = 1

reconstructed_image = np.abs(np.fft.ifft2(fft_2))

plt.figure()
plt.imshow(fft_mask_2)
plt.title("Bild 2: Maske zum Entfernen der Artefakte")

plt.figure()
plt.imshow(np.log(np.abs(fft_2)))
plt.title("Bild 2: Logarithmisch aufgetragenes Frequenz Spektrum nach Filterung")

plt.figure()
plt.imshow(noisy_image_2, cmap="gray")
plt.title("Bild 2: Bild mit Artefakten")

plt.figure()
plt.imshow(reconstructed_image, cmap="gray")
plt.title("Bild 2: Gefiltertes Bild")

plt.show()
