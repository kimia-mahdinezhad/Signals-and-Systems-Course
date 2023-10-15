from skimage import io, img_as_ubyte
import numpy as np
from matplotlib import pyplot as plt


def draw_histogram_plot():
    # Calculate Colored Image Histogram
    scales_colored = np.zeros(256)

    for i in range(len(image_colored)):
        for j in range(len(image_colored[0])):
            for k in range(len(image_colored[0][0])):
                scales_colored[image_colored[i][j][k]] += 1

    # Calculate Colored Image Threshold
    max_val_colored = 0
    for i in range(256):
        if scales_colored[i] > scales_colored[max_val_colored]:
            max_val_colored = i

    # Draw Colored Image Histogram
    plot1 = plt.figure(1)
    plot1.suptitle('Colored Image Histogram')
    plt.plot(scales_colored)

    # Calculate Gray Image Histogram
    scales_gray = np.zeros(256)

    for i in range(len(image_gray)):
        for j in range(len(image_gray[0])):
            scales_gray[image_gray[i][j]] += 1

    # Calculate Gray Image Threshold
    max_val_gray = 0
    for i in range(256):
        if scales_gray[i] > scales_gray[max_val_gray]:
            max_val_gray = i

    # Draw Gray Image Histogram
    plot2 = plt.figure(2)
    plot2.suptitle('Gray Image Histogram')
    plt.plot(scales_gray)

    return max_val_colored, max_val_gray


def show_image_with_threshold():
    # Rebuild Colored Image With Threshold
    new_image_colored = image_colored

    for i in range(len(image_colored)):
        for j in range(len(image_colored[0])):
            for k in range(len(image_colored[0][0])):
                if new_image_colored[i][j][k] >= threshold_colored:
                    new_image_colored[i][j][k] = 0

    # Save Colored Image With Threshold
    io.imsave("KimiaMahdinejad_removed_noise_colored.jpg", new_image_colored.astype(np.uint8))

    # Rebuild Gray Image With Threshold
    new_image_gray = image_gray

    for i in range(len(image_gray)):
        for j in range(len(image_gray[0])):
            if new_image_gray[i][j] > threshold_gray:
                new_image_gray[i][j] = 0

    # Save Gray Image With Threshold
    io.imsave("KimiaMahdinejad_removed_noise_gray.jpg", new_image_gray.astype(np.uint8))


# Read Image as Colored and Gray
image_colored = img_as_ubyte(io.imread("KimiaMahdinejad.jpg", as_gray=False))
image_gray = img_as_ubyte(io.imread("KimiaMahdinejad.jpg", as_gray=True))

threshold_colored, threshold_gray = draw_histogram_plot()

show_image_with_threshold()

plt.show()
