import pytest
import numpy as np
from matplotlib.colors import to_rgb
from matplotlib import pyplot as plt
from accessiplot.detection.contrast_ratio import *

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


def test_contrast_ratio_detection_works():
    # data to be plotted
    x = np.arange(1, 11)
    y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
    num_lines = 10
    for i in range(num_lines):
        y_val = (np.random.rand(1,10)).T
        plt.plot(x, y_val)

    contrast_ratios_dict, line_colors, detections = calculate_contrast_ratios_from_plt(plt)

    #TODO: Do an adequate assertion on the values and parameterize appropriately
    assert True
