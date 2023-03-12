from accessiplot.detection.handler import DetectionHandler, DetectionTypes
from matplotlib import pyplot as plt
import numpy as np
import pytest


@pytest.mark.parametrize(
    'num_lines, labels, expected', [
        # Empty labels
        pytest.param(
            2,
            [False, '', '_child0', '_child1', '', ''],
            {
                'lines': {0: '_child0', 1: '_child1'},
                'axes': {'x': '', 'y': ''},
                'title': '',
                'legend': None
            }
        ),
        # All labels present
        pytest.param(
            2,
            [True, 'My Title', 'plot0', 'plot1', 'x', 'y'],
            {
                'lines': {},
                'axes': {}
            }
        )
    ]
)
def test_label_detection_lines(num_lines, labels, expected):
    # data to be plotted
    x = np.arange(1, 11)

    # Reset the figure so that tests start with a fresh figure.
    _ = plt.figure()
    ax = plt.axes()
    for _ in range(num_lines):
        y_val = (np.random.rand(1, 10)).T
        ax.plot(x, y_val, label=labels[_ + 2])

    # Set axes labels for testing

    ax.set_xlabel(labels[-2])
    ax.set_ylabel(labels[-1])
    ax.set_title(labels[1])
    if labels[0]:
        ax.legend()
    dh = DetectionHandler(ax=ax)
    dh.run_detections(run_detections_list=[DetectionTypes.LABEL.name])

    print(dh.detections, expected)
    assert dh.detections[DetectionTypes.LABEL.name] == expected


@pytest.mark.parametrize(
    'labels, expected', [
        # Empty labels
        pytest.param(
            [False, '', '', ''],
            {
                'bins': {},
                'axes': {'x': '', 'y': ''},
                'title': '',
                'legend': None
            }
        ),
        # All labels present
        pytest.param(
            [True, 'My Title', 'x', 'y'],
            {
                'bins': {},
                'axes': {}
            }
        )
    ]
)
def test_label_detection_histogram(labels, expected):
    # Creating dataset
    a = np.array([22, 87, 5, 43, 56,
                  73, 55, 54, 11,
                  20, 51, 5, 79, 31,
                  27])

    # Creating histogram
    _, ax = plt.subplots(figsize=(10, 7))
    h = ax.hist(a, bins=[0, 25, 50, 75, 100])
    dh = DetectionHandler(ax=ax, histogram=h)

    # Set axes labels for testing

    ax.set_xlabel(labels[-2])
    ax.set_ylabel(labels[-1])
    ax.set_title(labels[1])
    if labels[0]:
        ax.legend()
    dh = DetectionHandler(ax=ax)
    dh.run_detections(run_detections_list=[DetectionTypes.LABEL.name])

    print(dh.detections, expected)
    assert dh.detections[DetectionTypes.LABEL.name] == expected
