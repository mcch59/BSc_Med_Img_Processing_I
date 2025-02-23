import matplotlib.pyplot as plt

from filter_functions import (
    better_low_pass_filter,
    low_pass_filter,
    high_pass_filter,
    better_high_pass_filter,
)

image = plt.imread("Chest.png")[:, :, 0]

low_passed_image = low_pass_filter(image)
low_passed_image_2 = better_low_pass_filter(image, kernel_sigma=5)

high_passed_image = high_pass_filter(image)
high_passed_image_2 = better_high_pass_filter(image, kernel_sigma=20)

plt.figure()
plt.imshow(low_passed_image, cmap="gray")
plt.title("Tiefpass Bild Sub-Optimal")

plt.figure()
plt.imshow(low_passed_image_2, cmap="gray")
plt.title("Tiefpass Bild Optimal")

plt.figure()
plt.imshow(high_passed_image, cmap="gray")
plt.title("Hochpass Bild Sub-Optimal")

plt.figure()
plt.imshow(high_passed_image_2**0.8, cmap="gray")
plt.title("Hochpass Bild Optimal")

plt.show()
