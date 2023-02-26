import numpy as np
from matplotlib import pyplot as plt
from accessiplot.detection.marker import get_markers


def test_marker_detection_works():
    # data to be plotted
    x = np.arange(1, 11)
    _ = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
    num_lines = 10
    for _ in range(num_lines):
        y_val = (np.random.rand(1, 10)).T
        plt.plot(x, y_val)

    _ = get_markers(plt=plt)

    # TODO: Do an adequate assertion on the values and parameterize appropriately
    assert True
