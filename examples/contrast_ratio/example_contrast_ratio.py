"""
============================
Low Contrast Ratio Detection
============================
This example shows how to detect low contrast ratio in an image
using the `accessiplot.detection.contrast_ratio` module.
"""

from accessiplot.detection.handler import DetectionHandler, DetectionTypes
import matplotlib.pyplot as plt
import numpy as np


# data to be plotted
x = np.arange(1, 11)
y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])

_ = plt.figure()
ax = plt.axes()

num_lines = 10
for i in range(num_lines):
    y_val = (np.random.rand(1, 10)).T
    ax.plot(x, y_val)

dh = DetectionHandler(ax=ax)
dh.run_detections(run_detections_list=[DetectionTypes.CONTRAST_RATIO.name])

print("contrast_ratios_by_index:", dh.contrast_ratios_by_index)

print("colors_by_index:", dh.colors_by_index)

print("detections:", dh.detections)
