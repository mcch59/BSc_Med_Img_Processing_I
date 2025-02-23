import matplotlib.pyplot as plt
import numpy as np
import cv2

plt.close("all")

image = plt.imread("Herz.png")

kernel = np.ones(shape=[5, 5], dtype=np.uint8)

eroded_image = cv2.erode(image, kernel, iterations=6)

dilated_image = cv2.dilate(image, kernel, iterations=6)


dilated_eroded_image = cv2.dilate(eroded_image, kernel, iterations=6)
eroded_dilated_image = cv2.erode(dilated_image, kernel, iterations=6)

kernel_small = np.ones([3, 3])
edges = cv2.dilate(image, kernel_small, iterations=1) - image
edges_2 = image - cv2.erode(image, kernel_small, iterations=1)

fig, ax = plt.subplots(2, 3)
ax[0, 0].imshow(image, cmap="gray")
ax[0, 0].title.set_text("original image")

ax[0, 1].imshow(eroded_image, cmap="gray")
ax[0, 1].title.set_text("eroded image")

ax[0, 2].imshow(dilated_image, cmap="gray")
ax[0, 2].title.set_text("dilated image")

ax[1, 0].imshow(dilated_eroded_image, cmap="gray")
ax[1, 0].title.set_text("Dilation of eroded image")

ax[1, 1].imshow(eroded_dilated_image, cmap="gray")
ax[1, 1].title.set_text("Erosion of dilated image")

plt.figure()
plt.imshow(edges, cmap="gray")
plt.title("Outer edges (contour) of heart with dilation")

plt.figure()
plt.imshow(edges_2, cmap="gray")
plt.title("Inner edges of heart (furthest outer pixels of the heart) with erosion")


plt.show()
