import matplotlib.pyplot as plt

image = plt.imread("Bunte_Formen.png")

gray_image = (image[:, :, 0] + image[:, :, 1] + image[:, :, 2]) / 3

plt.figure()
plt.imshow(image)

plt.figure()
plt.imshow(gray_image, cmap="gray", vmin=0, vmax=1)


plt.show()
