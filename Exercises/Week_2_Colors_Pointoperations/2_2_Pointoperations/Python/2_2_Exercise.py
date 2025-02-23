import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

# =============================================================================
# Contrast enhancement low intensity values
# =============================================================================
cameraman = plt.imread("cameraman_1.bmp")
cameraman_enhanced = cameraman.copy()
cameraman_enhanced[cameraman_enhanced > 150] = 150
cameraman_enhanced = cameraman_enhanced - cameraman_enhanced.min()
cameraman_enhanced = cameraman_enhanced / cameraman_enhanced.max()
cameraman_enhanced = np.round(cameraman_enhanced * 255).astype("uint8")

plt.figure()
plt.imshow(cameraman, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(cameraman_enhanced, cmap="gray")
plt.title("enhanced low intensities")

# =============================================================================
# Noise reduction by averaging
# =============================================================================
image_1 = plt.imread("Saturn_1.jpg")
image_2 = plt.imread("Saturn_2.jpg")
image_3 = plt.imread("Saturn_3.jpg")

smoothed_image = (image_1.astype(int) + image_2.astype(int) + image_3.astype(int)) / 3

plt.figure()
plt.imshow(image_1, cmap="gray", vmin=0, vmax=255)
plt.title("Noisy image 1")

plt.figure()
plt.imshow(image_2, cmap="gray", vmin=0, vmax=255)
plt.title("Noisy image 2")

plt.figure()
plt.imshow(image_3, cmap="gray", vmin=0, vmax=255)
plt.title("Noisy image 3")

plt.figure()
plt.imshow(smoothed_image, cmap="gray", vmin=0, vmax=255)
plt.title("Smoothed image")

plt.show()
