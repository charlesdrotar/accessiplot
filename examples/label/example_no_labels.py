"""
===========================
No Labels Present Detection
===========================
This example shows that all labels were detected as missing
as well as the x and y labels of the axes themselves.

The default values assigned by labels are defined in `labels`.
"""

import numpy as np
from matplotlib import pyplot as plt
from accessiplot.detection.handler import DetectionHandler, DetectionTypes

num_lines = 2
labels = ['_child0', '_child1', '', '']

# data to be plotted
x = np.arange(1, 11)

_ = plt.figure()
ax = plt.axes()

# Reset the figure so that tests start with a fresh figure.
for _ in range(num_lines):
    y_val = (np.random.rand(1, 10)).T
    ax.plot(x, y_val, label=labels[_])

ax.set_xlabel(labels[-2])
ax.set_ylabel(labels[-1])

dh = DetectionHandler(ax=ax)
dh.run_detections(run_detections_list=[DetectionTypes.LABEL.name])

print("detections:", dh.detections)

plt.show()
