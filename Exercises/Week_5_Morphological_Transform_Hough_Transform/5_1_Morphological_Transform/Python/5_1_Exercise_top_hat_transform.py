import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read in image and pre-processing
image_orig = plt.imread("Bakterien.png")
# print(image.shape)
# print(type(image[0, 0, 0]))

image = np.sum(image_orig, axis=-1) / 3

raw_mask = (image < 0.9) * 1.0


# Zylinderhut Transformation
kernel = np.ones(shape=[3, 3])
eroded_mask = cv2.erode(raw_mask, kernel=kernel, iterations=8)
opened_mask = cv2.dilate(eroded_mask, kernel=kernel, iterations=10)

cleaned_mask = raw_mask - opened_mask
cleaned_mask[cleaned_mask < 0] = 0

cleaned_image = np.zeros(image_orig.shape)
for channel_number in range(cleaned_image.shape[2]):
    cleaned_image[:, :, channel_number] = (
        cleaned_mask * image_orig[:, :, channel_number]
    )


plt.figure()
plt.imshow(image_orig)
plt.title("Original image")

plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Grayscale image")

plt.figure()
plt.imshow(raw_mask, cmap="gray")
plt.title("Binary raw mask")

plt.figure()
plt.imshow(eroded_mask, cmap="gray")
plt.title("Eroded mask")

plt.figure()
plt.imshow(opened_mask, cmap="gray")
plt.title("Opened Mask")

plt.figure()
plt.imshow(cleaned_mask, cmap="gray")
plt.title("Result top-hat transform")

plt.figure()
plt.imshow(cleaned_image)
plt.title("Cleaned image")

plt.show()
