import pytest
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib import pyplot as plt

import sys

from accessiplot.detection.color_detection import *

def test_get_common_colors_from_image():
    # data to be plotted
    x = np.arange(1, 11)
    y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
    num_lines = 10
    for i in range(num_lines):
        y_val = (np.random.rand(1,10)).T
        plt.plot(x, y_val)
    plt.show()


def test_get_common_colors_from_plot():
    assert True
    
    
def test_convert_image():
    assert True


def test_display_image():
    assert True


def test_compare_colors():
    assert True
    

test_get_common_colors_from_image()
