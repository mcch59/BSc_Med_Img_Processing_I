import matplotlib.pyplot as plt
import cv2
import numpy as np

image = plt.imread("Herz.png")

kernel = np.ones(shape=[3, 3])

eroded_image = cv2.erode(image, kernel=kernel, iterations=5)
dilated_image = cv2.dilate(image, kernel=kernel, iterations=5)


fig, ax = plt.subplots(2, 3)

ax[0, 0].imshow(image, cmap="gray")
ax[0, 0].title.set_text("Original Bild")

ax[0, 1].imshow(eroded_image, cmap="gray")
ax[0, 1].title.set_text("Erodiertes Bild, 5 Iterationen")

ax[0, 2].imshow(dilated_image, cmap="gray")
ax[0, 2].title.set_text("Dilatiertes Bild, 5 Iterationen")

plt.show()
