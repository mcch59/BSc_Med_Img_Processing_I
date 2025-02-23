import matplotlib.pyplot as plt
import numpy as np


def print_mean_and_variance(image, image_name):

    mean = np.mean(image)
    var = np.var(image)

    print(f"Das Bild {image_name} hat ein Mittelwert von {mean}")
    print(f"Das Bild {image_name} hat eine Varianz von {var}")
    print()


# =============================================================================
# Bilder einlesen
# =============================================================================
image = plt.imread("cameraman_1.bmp")
image_2 = plt.imread("cameraman_2.bmp")
image_3 = plt.imread("cameraman_3.bmp")

# =============================================================================
# Ausgabe Mittelwert und Varianz
# =============================================================================
print_mean_and_variance(image, "Kameramann 1")
print_mean_and_variance(image_2, "Kameramann 2")
print_mean_and_variance(image_3, "Kameramann 3")


plt.figure()
plt.imshow(image_3, cmap="gray", vmin=0, vmax=255)

plt.figure()
plt.imshow(image, cmap="gray", vmin=0, vmax=255)

plt.figure()
plt.imshow(image_2, cmap="gray", vmin=0, vmax=255)


plt.show()
