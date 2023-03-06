import pytest
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib import pyplot as plt
from accessiplot.detection.contrast_ratio import calculate_contrast_ratio
from accessiplot.detection.handler import DetectionHandler, DetectionTypes


@pytest.mark.parametrize(
    'c1,c2, expected', [
        # Red vs. Blue, contrast ratio
        pytest.param('r', 'b', 2.148936170212766),
        # Red vs. Blue, contrast ratio
        pytest.param('c', 'm', 2.319956564494119)
    ]
)
def test_contrast_ratio_are_symmetric_and_string_conversion_works(c1, c2, expected):
    # Tests that contrast ratios are symmetric and within expected value.
    # Use this website for reference - https://contrast-ratio.com/
    # Use lib/matplotlib/_color_data.py
    contrast_ratio = calculate_contrast_ratio(to_rgb(c1), to_rgb(c2))
    contrast_ratio_swapped = calculate_contrast_ratio(to_rgb(c2), to_rgb(c1))

    assert contrast_ratio == contrast_ratio_swapped

    pytest.approx(expected, 0.01) == contrast_ratio


def test_contrast_ratio_detection_works_lines():
    # data to be plotted
    x = np.arange(1, 11)
    _ = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
    num_lines = 10

    # Reset the figure so that tests start with a fresh figure.
    _ = plt.figure()
    ax = plt.axes()
    for _ in range(num_lines):
        y_val = (np.random.rand(1, 10)).T
        ax.plot(x, y_val)

    dh = DetectionHandler(ax=ax)
    dh.run_detections(run_detections_list=[DetectionTypes.CONTRAST_RATIO.name])
    assert True


def test_contrast_ratio_detection_works_histogram():
    # Creating dataset
    a = np.array([22, 87, 5, 43, 56,
                  73, 55, 54, 11,
                  20, 51, 5, 79, 31,
                  27])

    # Creating histogram
    _, ax = plt.subplots(figsize=(10, 7))
    h = ax.hist(a, bins=[0, 25, 50, 75, 100])
    dh = DetectionHandler(ax=ax, histogram=h)
    dh.run_detections(run_detections_list=[DetectionTypes.CONTRAST_RATIO.name])
    # TODO: Do an adequate assertion on the values and parameterize appropriately
    assert True
