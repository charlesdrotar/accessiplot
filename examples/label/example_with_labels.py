"""
===============================
Labels Present Shows 0 Detections
===============================
This example shows that all labels were detected
and none were found to be missing.
"""
import numpy as np
from matplotlib import pyplot as plt
from accessiplot.detection.label import get_labels

num_lines = 2
labels = ['plot0', 'plot1', 'x', 'y']

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

_, x_label, y_label, detections = get_labels(ax=ax)

print("detections:", detections)

plt.show()
