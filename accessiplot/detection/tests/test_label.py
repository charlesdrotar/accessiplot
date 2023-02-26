import pytest
import numpy as np
from matplotlib import pyplot as plt
from accessiplot.detection.label import get_labels


@pytest.mark.parametrize(
    'num_lines, labels, expected', [
        # Empty labels
        pytest.param(
            2,
            ['_child0', '_child1', '', ''],
            {
                'lines': {0: '_child0', 1: '_child1'},
                'axes': {'x': '', 'y': ''}
            }
        ),
        # All labels present
        pytest.param(
            2,
            ['plot0', 'plot1', 'x', 'y'],
            {
                'lines': {},
                'axes': {}
            }
        )
    ]
)
def test_label_detection(num_lines, labels, expected):
    # data to be plotted
    x = np.arange(1, 11)

    # Reset the figure so that tests start with a fresh figure.
    _ = plt.figure()
    ax = plt.axes()
    for _ in range(num_lines):
        y_val = (np.random.rand(1, 10)).T
        ax.plot(x, y_val, label=labels[_])

    # Set axes labels for testing

    ax.set_xlabel(labels[-2])
    ax.set_ylabel(labels[-1])
    print(ax.get_xlabel(), ax.get_ylabel())

    _, x_label, y_label, detections = get_labels(ax=ax)

    print(detections, expected)
    assert x_label == ax.get_xlabel()
    assert y_label == ax.get_ylabel()
    assert detections == expected
