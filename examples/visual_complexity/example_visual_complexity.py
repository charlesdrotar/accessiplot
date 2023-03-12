"""
===========================
Visual Complexity Detection
===========================
This example shows how to detect over-complexity issue
using the `accessiplot.detection.visual_complexity` module.
"""

from accessiplot.detection.visual_complexity import get_complexity
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1, 6)
y = np.array([100, 10, 300, 20, 500])
num_lines = 5
for i in range(num_lines):
    y_val = (np.random.rand(1, 5)).T
    plt.plot(x, y_val)

complexity = get_complexity(plt)

print('complexity score: {}'.format(complexity))
