import pytest
import numpy as np
from matplotlib import pyplot as plt
from accessiplot.detection.marker import *

def test_contrast_ratio_detection_works():
    # data to be plotted
    x = np.arange(1, 11)
    y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
    num_lines = 10
    for i in range(num_lines):
        y_val = (np.random.rand(1,10)).T
        plt.plot(x, y_val)

    markers = get_markers(plt=plt)

    #TODO: Do an adequate assertion on the values and parameterize appropriately
    assert True