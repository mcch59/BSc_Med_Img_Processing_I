import matplotlib.pyplot as plt
import skimage

image = plt.imread("Balken.bmp")

# Formatted string
print(f"Die Pixel haben eine Kodierung von {type(image[0,0])}")

# =============================================================================
# Histogramm plotten
# =============================================================================

image_flattened = image.flatten()  # Bild "platt machen"
plt.figure()
plt.hist(image_flattened, bins=256)
plt.title("Histogramm")
# =============================================================================
# Linienprofil
# =============================================================================

start_punkt = (0, 0)  # (Zeile, Spalte)
start_x = start_punkt[1]  # x-Koordinate = Spalte
start_y = start_punkt[0]  # y-Koordinate = Zeile

end_punkt = (511, 511)
end_x = end_punkt[1]
end_y = end_punkt[0]

linien_profil = skimage.measure.profile_line(image, start_punkt, end_punkt)


# =============================================================================
# Plotten
# =============================================================================
plt.figure()
plt.imshow(image, cmap="gray")

# Syntax beim Plotten: plt.plot(x,y) wobei x und y eine Liste oder Array mit
# x- und y-Koordinaten sein können
plt.scatter(start_x, start_y, c="red")  # 1. Punkt
plt.scatter(end_x, end_y, c="red")  # 2. Punkt

plt.plot([start_x, end_x], [start_y, end_y])

plt.figure()
plt.plot(linien_profil)
plt.title("Linien-Profil")

plt.show()
