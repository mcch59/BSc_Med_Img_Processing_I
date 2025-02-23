import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("Saturn_1.jpg").astype(float)

checking_radius = 5

filtered_image = image.copy()


noise_overall = 22


for row in range(checking_radius, image.shape[0] - checking_radius):
    for column in range(checking_radius, image.shape[1] - checking_radius):

        checking_area = image[
            row - checking_radius : row + checking_radius + 1,
            column - checking_radius : column + checking_radius + 1,
        ]

        noise_local = np.std(checking_area)
        mean_local = np.mean(checking_area)
        filtered_image[row, column] = (noise_local - noise_overall) / (
            noise_local + 0.0000001  # + kleine Zahl, damit nie durch 0 geteilt wird
        ) * (image[row, column] - mean_local) + mean_local


plt.figure()
plt.imshow(image, cmap="gray")

plt.figure()
plt.imshow(filtered_image, cmap="gray", vmin=0, vmax=255)

plt.show()
