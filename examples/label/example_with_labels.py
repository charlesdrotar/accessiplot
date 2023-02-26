"""
===============================
Labels Present Shows Detections
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

# Reset the figure so that tests start with a fresh figure.
for _ in range(num_lines):
    y_val = (np.random.rand(1, 10)).T
    plt.plot(x, y_val, label=labels[_])

plt.xlabel = labels[-2]
plt.ylabel = labels[-1]

_, x_label, y_label, detections = get_labels(ax=plt.gca())

print("detections:", detections)

plt.show()
