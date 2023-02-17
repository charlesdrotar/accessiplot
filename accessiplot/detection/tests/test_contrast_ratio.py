import pytest
from accessiplot.detection.contrast_ratio import *

@pytest.mark.parametrize(
    'c1,c2, expected', [
        # Red vs. Blue, contrast ratio
        pytest.param('r', 'b', 2.148936170212766),
                # Red vs. Blue, contrast ratio
        pytest.param('c', 'm', 2.319956564494119)
    ]
)
def test_contrast_ratio_using_strings(c1, c2, expected):
    # Tests that contrast ratios are symmetric and within expected value.
    # Use this website for reference - https://contrast-ratio.com/
    # Use lib/matplotlib/_color_data.py
    contrast_ratio = \
        calculate_contrast_ratio(convert_string_color_to_rgb(c1), 
        convert_string_color_to_rgb(c2))
    contrast_ratio_swapped = \
        calculate_contrast_ratio(convert_string_color_to_rgb(c2), 
        convert_string_color_to_rgb(c1))

    assert contrast_ratio == contrast_ratio_swapped

    pytest.approx(expected, 0.01) == contrast_ratio