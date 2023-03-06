import numpy as np
from matplotlib import pyplot as plt

from accessiplot.detection.visual_complexity import get_complexity


def get_complexity():

    x = np.arange(1, 6)
    _ = np.array([100, 10, 300, 20, 500])
    num_lines = 5
    for i in range(num_lines):
        y_val = (np.random.rand(1, 5)).T
        plt.plot(x, y_val)

    complexity = get_complexity(plt)
    assert complexity >= 0.5
