"""
=================================
Labels Present Shows 0 Detections
=================================
This example shows that all labels were detected
and none were found to be missing.
"""

from accessiplot.detection.handler import DetectionHandler, DetectionTypes
from matplotlib import pyplot as plt
import numpy as np


num_lines = 2
labels = ['plot0', 'plot1']
x_axis = 'x'
y_axis = 'y'
title = "Hi I am an Example Title"

# data to be plotted
x = np.arange(1, 11)

_ = plt.figure()
ax = plt.axes()

# Reset the figure so that tests start with a fresh figure.
for _ in range(num_lines):
    y_val = (np.random.rand(1, 10)).T
    ax.plot(x, y_val, label=labels[_])

ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(title)
ax.legend()

dh = DetectionHandler(ax=ax)
dh.run_detections(run_detections_list=[DetectionTypes.LABEL.name])

print("detections:", dh.detections)

plt.show()
