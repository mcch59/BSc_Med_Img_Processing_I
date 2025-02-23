import matplotlib.pyplot as plt
import numpy as np

plt.close("all")

image = plt.imread("cameraman_1.bmp")
image_flattened = image.flatten()

# =============================================================================
# Kontrast erhöhen
# =============================================================================
image_enhanced = image.copy()

image_enhanced[image_enhanced < 150] = 150
image_enhanced[image_enhanced > 230] = 230

image_enhanced = image_enhanced - image_enhanced.min()  # Werte fangen bei 0 an
image_enhanced = image_enhanced / image_enhanced.max()  # Werte reichen von 0 bis 1

image_enhanced = image_enhanced * 255


# =============================================================================
# Bilder plotten
# =============================================================================

plt.figure()
plt.imshow(image, cmap="gray")

plt.figure()
plt.hist(image_flattened, bins=256)

plt.figure()
plt.imshow(image_enhanced, cmap="gray")
plt.title("enhanced")
plt.show()
