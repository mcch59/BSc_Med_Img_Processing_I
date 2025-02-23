import numpy as np

array_1 = np.array([250])
array_1 = array_1.astype("uint8")

array_1 = array_1.astype(float)  # ohne Umwandlung überschreiten wir uint8 Reichweite
array_2 = array_1 + array_1

print(array_2)
