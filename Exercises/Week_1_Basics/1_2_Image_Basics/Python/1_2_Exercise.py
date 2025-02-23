import matplotlib.pyplot as plt
import numpy as np


def get_image_statistics(image):
    print(f"Image shape: {image.shape}")
    print(f"Minimum pixel value: {image.min()}")
    print(f"Maximum pixel value: {image.max()}")
    print(f"Datatype of pixels: {type(image[0,0])}")


image = plt.imread("cameraman.bmp")

get_image_statistics(image)

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Original image")
# =============================================================================
# Histogram
# =============================================================================
image_flattened = image.flatten()

plt.figure()
bin_vals, bin_edges, _ = plt.hist(image_flattened, bins=256)
plt.title("Histogram")

plt.show()
