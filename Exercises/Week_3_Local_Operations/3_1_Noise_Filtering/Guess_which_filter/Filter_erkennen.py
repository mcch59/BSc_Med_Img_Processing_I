import matplotlib.pyplot as plt
import numpy as np

from filter_functions import my_filter_1, my_filter_2

image = plt.imread("Zebra.jpg")

image_1 = my_filter_1(image)
image_2 = my_filter_2(image)

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")

plt.figure()
plt.imshow(image_1, cmap="gray")
plt.title("Filter 1")

plt.figure()
plt.imshow(image_2, cmap="gray")
plt.title("Filter 2")


plt.show()
