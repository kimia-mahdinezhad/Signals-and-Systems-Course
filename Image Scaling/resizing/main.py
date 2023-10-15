from skimage import io, img_as_ubyte
import numpy as np


def resize_nearest_neighbor(image, ratio):
    # Setting new width and height
    new_width = int(width / ratio)
    new_height = int(height / ratio)

    # Calculating the scaling factor
    width_scale = new_width / (width - 1)
    height_scale = new_height / (height - 1)

    # Creating a matrix new width and height
    new_image = np.zeros([new_width, new_height, 3])

    # Creating new image based on nearest neighbor algorithm
    for width_index in range(new_width - 1):
        for height_index in range(new_height - 1):
            new_image[width_index + 1, height_index + 1] = image[1 + int(width_index / width_scale), 1 + int(height_index / height_scale)]

    return new_image


# Reading image as colored and gray
colored_image = img_as_ubyte(io.imread("KimiaMahdinejad.jpg", as_gray=False))
gray_image = img_as_ubyte(io.imread("KimiaMahdinejad.jpg", as_gray=True))

# Getting width and height of the image
width, height = colored_image.shape[:2]

# Resizing image with nearest neighbor algorithm and saving the new image

# X(2m, 2n)
nearest_neighbor_resized_colored_2 = resize_nearest_neighbor(colored_image, 2)
io.imsave("KimiaMahdinejad_NearestNeighbor_Colored_2.jpg", nearest_neighbor_resized_colored_2.astype(np.uint8))

nearest_neighbor_resized_gray_2 = resize_nearest_neighbor(gray_image, 2)
io.imsave("KimiaMahdinejad_NearestNeighbor_Gray_2.jpg", nearest_neighbor_resized_gray_2.astype(np.uint8))

# X(m/2, n/2)
nearest_neighbor_resized_colored_1_2 = resize_nearest_neighbor(colored_image, 1/2)
io.imsave("KimiaMahdinejad_NearestNeighbor_Colored_1_2.jpg", nearest_neighbor_resized_colored_1_2.astype(np.uint8))

nearest_neighbor_resized_gray_1_2 = resize_nearest_neighbor(gray_image, 1/2)
io.imsave("KimiaMahdinejad_NearestNeighbor_Gray_1_2.jpg", nearest_neighbor_resized_gray_1_2.astype(np.uint8))
