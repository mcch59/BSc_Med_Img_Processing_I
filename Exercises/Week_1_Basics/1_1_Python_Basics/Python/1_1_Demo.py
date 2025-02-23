import numpy as np
import matplotlib.pyplot as plt

from my_custom_functions import multiply

plt.close("all")

liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array_1 = np.array(liste)


print(array_1[0, 0])  # Ausgabe Element erste Zeile, erste Spalte
# Formatted String: Man kann Variablen in den Text einfügen. Initiiert mit f" "
# Variablen sind in geschweiften Klammern
print(f"Das Array hat {array_1.shape[1]} Spalten")
print(f"Das Minimum im Array ist: {array_1.min()}")
print(f"Das Maximum im Array ist: {array_1.max()}")

array_2 = array_1 + 10

array_3 = multiply(array_1, 2)

for row in range(array_1.shape[0]):
    for column in range(array_1.shape[1]):

        pixel_value = array_1[row, column]

        if pixel_value > 5:
            print(pixel_value)


# =============================================================================
# Plotten
# =============================================================================
plt.figure()
plt.imshow(array_1, cmap="gray", vmin=1, vmax=20)

plt.figure()
plt.imshow(array_2, cmap="gray", vmin=1, vmax=20)

plt.figure()
plt.imshow(array_3, cmap="gray", vmin=1, vmax=20)

plt.show()
