import matplotlib.pyplot as plt
import numpy as np
import cv2

image = plt.imread("Binary_mask_femur.png")
kernel = np.ones(shape=[3, 3])


eroded_image = cv2.erode(image, kernel, iterations=2)
opened_image = cv2.dilate(eroded_image, kernel, iterations=2)

cleaned_femur = opened_image.copy()

dilated_cleaned_femur = cv2.dilate(cleaned_femur, kernel, iterations=4)
closed_cleaned_femur = cv2.erode(dilated_cleaned_femur, kernel, iterations=4)


plt.figure()
plt.imshow(image, cmap="gray")
plt.title("Raw binary segmentation mask")

plt.figure()
plt.imshow(eroded_image, cmap="gray")
plt.title("Eroded segmentation mask")

plt.figure()
plt.imshow(opened_image, cmap="gray")
plt.title("Cleaned femur through opening")

plt.figure()
plt.imshow(dilated_cleaned_femur, cmap="gray")
plt.title("Dilated cleaned femur")

plt.figure()
plt.imshow(closed_cleaned_femur, cmap="gray")
plt.title("Closed cleaned femur")

plt.show()
