import numpy as np
import matplotlib.pyplot as plt

from my_custom_functions import square_array, search_for_large_values


plt.close("all")  # schliesst alle offenen Fenster/Abbildungen

# =============================================================================
# Aufgabe 1
# =============================================================================
my_array = np.array(
    [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12],
        [4, 8, 12, 16],
    ]
)

# =============================================================================
# Aufgabe 2
# =============================================================================
plt.figure()
plt.imshow(my_array, cmap="gray", vmin=0, vmax=16)

# =============================================================================
# Aufgabe 3
# =============================================================================
my_array_2 = my_array[1:3, 1:3]
plt.figure()
plt.imshow(my_array_2, cmap="gray", vmin=0, vmax=30)

# =============================================================================
# Aufgabe 4
# =============================================================================
my_array_3 = square_array(my_array)

plt.figure()
plt.imshow(my_array_3, cmap="gray", vmin=0, vmax=255)

# =============================================================================
# Aufgabe 5
# =============================================================================
search_for_large_values(my_array)
print("---------- new array ----------")
search_for_large_values(my_array_3)

plt.show()
