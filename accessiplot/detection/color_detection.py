import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import colorsys
from colorthief import ColorThief

from colorspacious import cspace_convert
from colorspacious import deltaE


def get_common_colors_from_image(fn, top_count=6):
    """
    Given a file name of an image,
    return a list of most common colors used in the image, in RGB.
    """
    color_thief = ColorThief(fn)
    palette = color_thief.get_palette(color_count=top_count)
    palette.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
    return palette


def get_common_colors_from_plot(plot):
    """
    Given a line chart,
    return a list of colors used for the lines and background, in RGB.
    """
    axes_object = plt.gca()
    lines_colors = [to_rgb(line.get_color()) for line in axes_object.lines]
    lines_colors.append(to_rgb(axes_object.get_facecolor()))
    return [(round(x[0] * 255), round(x[1] * 255), round(x[2] * 255))
            for x in lines_colors]


def convert_image(img, color_vision_deficiency="deuteranomaly", severity=100):
    """
    Given an image,
    simulate how a person with color vision deficiency will see it.
    """
    assert color_vision_deficiency in ["deuteranomaly", "protanomaly",
                                       "tritanomaly"]
    assert severity > 0 and severity <= 100

    cvd_space = {"name": "sRGB1+CVD",
                 "cvd_type": color_vision_deficiency,
                 "severity": severity}
    return cspace_convert(img, cvd_space, "sRGB1").astype('uint8')


def display_images(old, new):
    """
    Given an original version of an image and a tuple of its modified versions,
    display them in a single plot for readers to compare.
    """
    image_width = 3.0  # inches
    total_width = (1 + len(new)) * image_width
    height = image_width / old.shape[1] * old.shape[0]
    fig = plt.figure(figsize=(total_width, height))
    ax = fig.add_axes((0, 0, 1, 1))
    ax.imshow((np.column_stack((old,) + new)))
    plt.show()


def compare_colors(colors, color_vision_deficiency="deuteranomaly",
                   severity=100, threshold=10):
    """
    Given a list of colors,
    check if any two of them are too similar to each other
    in the eye of someone with a specified color vision deficiency.
    """

    colors_array = np.array(colors)
    new_colors_array = convert_image(colors_array, color_vision_deficiency,
                                     severity)

    for i in range(len(new_colors_array)):
        for j in range(i+1, len(new_colors_array)):
            c1 = new_colors_array[i]
            c2 = new_colors_array[j]
            delta = deltaE(c1, c2, input_space="sRGB255")
            if delta <= threshold:
                print(c1)
                print(c2)
                print(delta)
