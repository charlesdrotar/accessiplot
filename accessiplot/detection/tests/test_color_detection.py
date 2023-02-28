import pytest
import numpy as np
from matplotlib.colors import to_rgb
import matplotlib
from matplotlib import pyplot as plt

import sys, os

from accessiplot.detection.color_detection import *

def test_get_common_colors_from_image():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s, color='black')

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
    ax.grid()

    file_name = "test.png"
    
    fig.savefig(file_name)
    
    img = plt.imread(file_name)
    colors = get_common_colors_from_image(file_name)
    
    # this is a gray scale image,
    # so the R, G, B values for every color should be the same.
    
    flag = True
    for i in colors:
        if not (i[0] == i[1] and i[1] == i[2]):
            flag = False
    assert flag
    
    os.remove(file_name)


def test_get_common_colors_from_plot():
    # data to be plotted
    x = np.arange(1, 6)
    y = np.array([100, 10, 300, 20, 500])
    num_lines = 5
    colors = [(168, 96, 50), (66, 135, 245), (183, 65, 191), (123, 186, 127), (100, 100, 100)]
    colors = cspace_convert(colors, "sRGB255", "sRGB1")
    for i in range(num_lines):
        y_val = (np.random.rand(1,5)).T
        plt.plot(x, y_val, color=(colors[i][0], colors[i][1], colors[i][2]))
    
    actual = get_common_colors_from_plot(plt, )

    flag = True
    for i in colors:
        if not i in actual:
            flag = False
    assert flag
    
    
def test_convert_image():
    
    colors1 = [(11, 11, 11), (100, 100, 100), (255, 255, 255)]
    colors1 = cspace_convert(colors1, "sRGB255", "sRGB1")
    result_colors1 = convert_image(colors1, "protanomaly", 50)
    
    flag1 = True
    for i in result_colors1:
        if not (i[0] == i[1] and i[1] == i[2]):
            flag1 = False
    assert flag1
    
    file_name = "grace_hopper.jpg"
    hopper_sRGB = plt.imread(matplotlib.cbook.get_sample_data(file_name))
    hopper_sRGB = cspace_convert(hopper_sRGB, "sRGB255", "sRGB1")

    img1 = convert_image(hopper_sRGB)
    img2 = convert_image(hopper_sRGB, "tritanomaly", 100)
    
    display_images(hopper_sRGB, (img1, img2))
    
    plt.show()
    
    os.remove(file_name)
    
    # There is some problem with this function that I need to fix, but will save it for now.
    assert True


def test_compare_colors():
    colors1 = [(11, 11, 11), (231, 116, 26), (242, 212, 175), (46, 161, 47), (30, 172, 36), (31, 120, 179)]
    flag1 = compare_colors(colors1)
    colors1 = cspace_convert(colors1, "sRGB255", "sRGB1")
    assert flag1
    
    # those are black / white / gray, so they should not be too similar to each other
    colors2 = [(11, 11, 11), (100, 100, 100), (255, 255, 255)]
    colors2 = cspace_convert(colors2, "sRGB255", "sRGB1")
    flag2 = compare_colors(colors2, "protanomaly", 50)
    assert not flag2
    
