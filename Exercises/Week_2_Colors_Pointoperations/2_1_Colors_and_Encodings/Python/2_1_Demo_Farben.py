import matplotlib.pyplot as plt

image = plt.imread("Bunte_Formen.png")
image_2 = plt.imread("Neue_Form.png")


print(image_2.shape)
print(type(image_2[0, 0, 0]))

# =============================================================================
# Mit Kanälen spielen
# =============================================================================

image_no_red = image.copy()
image_no_red[:, :, 0] = 0.2

image_more_red = image.copy()
image_more_red[:, :, 0] = image_more_red[:, :, 0] * 1.5

plt.figure()
plt.imshow(image)
plt.title("Original Bild")

plt.figure()
plt.imshow(image_no_red)
plt.title("Kein Rot-Kanal")

plt.figure()
plt.imshow(image_more_red)
plt.title("Stärkerer Rot-Kanal")

# plt.figure()
plt.imshow(image_2)
plt.title("Neues Bild")

plt.show()
