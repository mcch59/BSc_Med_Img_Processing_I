import matplotlib.pyplot as plt
import numpy as np

image_orig = plt.imread("Saturn_RGB.jpg")

reference_row, reference_column = 170, 340

R_reference = image_orig[reference_row, reference_column, 0]
G_reference = image_orig[reference_row, reference_column, 1]
B_reference = image_orig[reference_row, reference_column, 2]

R_correction = 255 / R_reference
G_correction = 255 / G_reference
B_correction = 255 / B_reference

balanced_picture = np.zeros(shape=image_orig.shape)

for row in range(image_orig.shape[0]):
    for column in range(image_orig.shape[1]):
        balanced_picture[row, column, 0] = image_orig[row, column, 0] * R_correction
        balanced_picture[row, column, 1] = image_orig[row, column, 1] * G_correction
        balanced_picture[row, column, 2] = image_orig[row, column, 2] * B_correction


balanced_picture[balanced_picture > 255] = 255

balanced_picture = balanced_picture.astype("uint8")

plt.figure()
plt.imshow(image_orig)
plt.title("Original image")

plt.figure()
plt.imshow(balanced_picture)
plt.title("White white balanced image")

plt.show()
