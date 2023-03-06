"""
===================================
Color Blindness Detection Detection
===================================
This example shows how to detect if the use of colors in
a visualization is friendly to people with color vision
deficiencies using the `accessiplot.detection.color_detection` module.
"""

import numpy as np
import matplotlib.pyplot as plt
from accessiplot.detection.color_detection import full_detection

x = np.arange(1, 6)
y = np.array([100, 10, 300, 20, 500])
num_lines = 5
for i in range(num_lines):
    y_val = (np.random.rand(1, 5)).T
    plt.plot(x, y_val)

print(full_detection(plt, ))
