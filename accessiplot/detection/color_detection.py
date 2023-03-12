from accessiplot.utils.logger import logger
import colorsys
from colorthief import ColorThief
from colorspacious import cspace_convert
from colorspacious import deltaE
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np
import os


__all__ = [
    'get_common_colors_from_image',
    'get_common_colors_from_plot',
    'convert_image',
    'display_images',
    'compare_colors',
    'full_detection'
]


def get_common_colors_from_image(file_name: str, top_count: int = 6):
    """
    Given a file name of an image,
    return a list of most common colors used in the image, in RGB.

    Parameters
    ----------
    file_name : str
        The file name (path) to an image
    top_count : int
        The number of top colors to be returned

    Returns
    -------
    palette: list
        A list of most commonly used colors in the image.
    """

    color_thief = ColorThief(file_name)
    palette = color_thief.get_palette(color_count=top_count)
    palette.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb))
    palette = cspace_convert(palette, "sRGB255", "sRGB1")
    return palette


def get_common_colors_from_plot(plot):
    """
    Given a line chart,
    return a list of colors used for the lines and background, in RGB.

    Parameters
    ----------
    plt : matplotlib.pyplot
        A matplotlib.pyplot object in which a line chart is plotted.

    Returns
    -------
    lines_colors: list
        A list of colors used for the lines in the plot.
    """
    axes_object = plt.gca()
    lines_colors = [to_rgb(line.get_color()) for line in axes_object.lines]
    lines_colors.append(to_rgb(axes_object.get_facecolor()))
    lines_colors = cspace_convert(lines_colors, "sRGB1", "sRGB1")
    return lines_colors


def convert_image(img, color_vision_deficiency: str = "deuteranomaly", severity: int = 100):
    """
    Given an image,
    simulate how a person with color vision deficiency will see it.

    Parameters
    ----------
    img: arr
        An array-like of colors representing an image to be simulated.
    color_vision_deficiency: str
        The color vision deficiency to be simulated.
        It can be "deuteranomaly", "protanomaly", or "tritanomaly.
    severity: int
        The severity of color vision deficiency to be simulated,
        with 100 being the most severe one.

    Returns
    -------
    result_image: arr
        An array-like of colors representing an image after simulation.
    """

    assert color_vision_deficiency in ["deuteranomaly", "protanomaly",
                                       "tritanomaly"]
    assert severity > 0 and severity <= 100

    cvd_space = {"name": "sRGB1+CVD",
                 "cvd_type": color_vision_deficiency,
                 "severity": severity}

    result_image = cspace_convert(img, cvd_space, "sRGB1")  # .astype('uint8')
    return result_image


def display_images(old, new):
    """
    Given an original version of an image and a tuple of its modified versions,
    display them in a single plot for readers to compare.

    Parameters
    ----------
    odd: arr
        An array-like of colors representing an image.
    new: tuple
        A tuple of array-like of colors,
        each representing an image.
    """

    image_width = 3.0  # inches
    total_width = (1 + len(new)) * image_width
    height = image_width / old.shape[1] * old.shape[0]
    fig = plt.figure(figsize=(total_width, height))
    ax = fig.add_axes((0, 0, 1, 1))
    ax.imshow((np.column_stack((old,) + new)))
    plt.show()


def compare_colors(colors, color_vision_deficiency: str = "deuteranomaly",
                   severity: int = 100, threshold: int = 6):

    """
    Given a list of colors,
    check if any two of them are too similar to each other
    in the eye of someone with a specified color vision deficiency.
    If so, print out a warning.

    Parameters
    ----------
    colors: list
        A list of colors to be compared against each other.
    color_vision_deficiency: str
        The color vision deficiency to be simulated.
        It can be "deuteranomaly", "protanomaly", or "tritanomaly.
    severity: int
        The severity of color vision deficiency to be simulated,
        with 100 being the most severe one.
    threshold: int
        Threshold to detect if the Dealta-E value between two colors
        is below it.

    Returns
    -------
    flag: bool
        Whether or not there exists a pair of colors in the given list
        that are too similar to each other.

    References
    ----------
    .. [1] https://www.colorwiki.com/wiki/Delta_E

    """

    colors_array = np.array(colors)
    new_colors_array = convert_image(colors_array, color_vision_deficiency,
                                     severity)

    count = 0
    for i in range(len(new_colors_array)):
        for j in range(i+1, len(new_colors_array)):
            c1 = new_colors_array[i]
            c2 = new_colors_array[j]
            delta = deltaE(c1, c2, input_space="sRGB1")
            if delta <= threshold:
                if count == 0:
                    logger.warning(f"For a person with {color_vision_deficiency}, those colors are too close to each other:\n"\
                                   "str(c1) + ' and ' + str(c2)")
                # TODO: add a parameter for detecting the markers / labels
                count = count + 1
    flag = count != 0
    if not flag:
        pass  # TODO: should we print out a message saying everything is good?
    else:
        logger.info("Ignore this warnings if for each line, the markers are different or the labels are present.")
    return flag


def full_detection(plt, threshold: int = 6, show_comparison_plots: bool = False):
    """
    Given a line chart,
    detect if its use of color is unfriendly to people with
    either deuteranomaly, protanomaly or tritanomaly,
    and display the simulation for those color vision deficiencies.

    Parameters
    ----------
    plt : matplotlib.pyplot
        A matplotlib.pyplot object in which a line chart is plotted.
    threshold: int
        Threshold to detect if the Dealta-E value between two colors
        is below it.
    show_comparison_plots: bool
        Switch to toggle whether to plot comparisons as part of the
        detection.
    Returns
    -------
    flag: bool
        Whether or not there exists a pair of colors in the given list
        that are too similar to each other.
    detections: dict
        A dictionary that represents which color vision deficiency
        had a detection.
    """

    file_name = "test.jpg"
    plt.savefig(file_name)

    img = cspace_convert(plt.imread(file_name), "sRGB255", "sRGB1")

    cvd_list = ["deuteranomaly", "protanomaly", "tritanomaly"]
    detections = {k: v for (k, v) in zip(cvd_list, [{}, {}, {}])}
    colors = get_common_colors_from_plot(plt)
    simulations = []

    flag = False
    for cvd in cvd_list:
        is_an_accessibility_issue = compare_colors(colors, cvd, 100, threshold)
        if is_an_accessibility_issue:
            detections[cvd] = is_an_accessibility_issue
        flag = flag or is_an_accessibility_issue
        new_img = convert_image(img, cvd, 100)
        simulations.append(new_img)

    if show_comparison_plots:
        display_images(img, tuple(simulations))

    os.remove(file_name)  # clean up tmp file.
    return flag, detections
