"""
============================
Low Contrast Ratio Detection
============================
This example shows how to detect low contrast ratio in an image
using the `accessiplot.detection.contrast_ratio` module.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from accessiplot.detection.contrast_ratio import *


# data to be plotted
x = np.arange(1, 11)
y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
num_lines = 10
for i in range(num_lines):
    y_val = (np.random.rand(1,10)).T
    plt.plot(x, y_val)

contrast_ratios_dict, line_colors, detections = calculate_contrast_ratios_from_plt(plt)

print("contrast_ratios_dict:", contrast_ratios_dict)

print("line_colors:", line_colors)

print("detections:", detections)