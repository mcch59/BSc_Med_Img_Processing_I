import matplotlib.pyplot as plt
import numpy as np


def float_to_uint(float_image):
    """Convert float encoded image to uint8 encoding.

    Args:
        float_image (array): Any image of any shape with values ranging from 0 to 1

    Returns:
        array: Same array with input array linearly mapped to [0;255] of uint8 dtype
    """

    uint_image = np.round(float_image * 255).astype("uint8")

    return uint_image


def rgb_to_gray_scale(rgb_image, output_pixel_dtype="uint8"):
    """Convert RGB image to grayscale image with either float32 or uint8 encoding.

    Args:
        rgb_image (uint8 array): RGB or RGBA image with uint8 pixel
        output_pixel_dtype (string, optional): Specification of output pxiel dtype. Defaults to "uint8". Alternatively can be "float32".

    Returns:
        array: Grayscale image of input image with either uin8 or float32 encoding.
    """

    rgb_image = rgb_image.astype(float)  # Grössere Reichweite füt Addition

    gray_image = (rgb_image[:, :, 0] + rgb_image[:, :, 1] + rgb_image[:, :, 2]) / 3

    gray_image = np.round(gray_image).astype("uint8")  # rgb_image war schon uint8

    if output_pixel_dtype == "float32":
        gray_image = gray_image / 255
        gray_image = gray_image.astype("float32")

    return gray_image


image = plt.imread("Bunte_Formen.png")
print(f"Maximaler Pixelwert: {image.max()}")
print(f"Minimaler Pixelwert: {image.max()}")
print(type(image[0, 0, 0]))


uint_image = float_to_uint(image)
print(f"Maximaler Pixelwert: {uint_image.max()}")
print(f"Minimaler Pixelwert: {uint_image.min()}")

print(type(uint_image[0, 0, 0]))

gray_image = rgb_to_gray_scale(uint_image, output_pixel_dtype="float32")


plt.figure()
plt.imshow(image)
plt.title("Original image")

plt.figure()
plt.imshow(uint_image)
plt.title("uint8 pixels")

plt.figure()
plt.imshow(gray_image, cmap="gray")
plt.title("Gray image")

plt.show()
