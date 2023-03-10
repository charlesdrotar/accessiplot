from matplotlib.colors import to_rgb
import warnings
from accessiplot.utils.chart_type import ChartTypes
from accessiplot.detection.handler import DetectionHandler

__all__ = [
    'is_contrast_ratio_below_threshold',
    'calculate_contrast_ratios_from_ax',
    'calculate_contrast_ratio_histogram',
    'calculate_contrast_ratio_lines',
    'calculate_contrast_ratio',
    'calculate_relative_luminance',
    'normalize'
]

DELIMITER = "_---_"
BACKGROUND = "BACKGROUND"


def is_contrast_ratio_below_threshold(contrast_ratio: float, threshold: float = 2.5):
    """
    Pass in a contrast ratio and it will detect if it is below a limit.

    Parameters
    ----------
    contrast_ratio : float
        The contrast ratio calculated using the WCAG 2.0 definition.
    threshold : float
        Threshold to detect if the contrast ratio is below it.

    Returns
    -------
    is_below_threshold: bool
        Result of comparison of threshold and contrast ratio.
    """

    # TODO: This needs a bit more love to detect what threshold to use automatically by context
    is_below_threshold = False

    if contrast_ratio < threshold:
        is_below_threshold = True
    return is_below_threshold


def calculate_contrast_ratios_from_ax(dh: DetectionHandler):
    """
    Generates dictionaries of the contrast_ratios_by_index and detections.
    Also a list of colors_by_index is generated to keep track of the colors
    that are associated with the contrast ratios.
    It determines the processing logic based on the chart type from the
    DetectionHandler object.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    Returns
    -------
    contrast_ratios_by_index: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    colors_by_index: list
        List where each element is a tuple of `(r, g, b)` where `r`, `g`, and `b` are
        normalized from the 0->255 value down to a 0->1 value.
    detections: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    """
    contrast_ratios_by_index = {}
    colors_by_index = []
    detections = {}

    if dh.chart_type == ChartTypes.LINE_CHART.name:
        contrast_ratios_by_index, colors_by_index, detections = calculate_contrast_ratio_lines(dh)
    elif dh.chart_type == ChartTypes.HISTOGRAM.name:
        contrast_ratios_by_index, colors_by_index, detections = calculate_contrast_ratio_histogram(dh)
    else:
        warnings.warn(f"chart_type:{dh.chart_type} is unsupported! Returning dummy values for analysis")
    return contrast_ratios_by_index, colors_by_index, detections


def calculate_contrast_ratio_histogram(dh: DetectionHandler):
    """
    Generates a dictionary of contrast ratios from an Axes object,
    the corresponding colors of the lines and background, and
    a dictionary of comparisons that have a contrast ratio below
    a given threshold.

    1) Get color of all bins as rgb and append to list
    2) Get color of the background and append to list
    3) Do an n**2 comparison of colors in the above list and generate contrast ratios.
       These are stored as key/value mappings where the key is `<index_color1>_<index_color2>`.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    Returns
    -------
    contrast_ratios_by_index: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    line_colors: list
        List where each element is a tuple of `(r, g, b)` where `r`, `g`, and `b` are
        normalized from the 0->255 value down to a 0->1 value.
    detections: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    """
    if dh.histogram is None:
        warnings.warn("The DetectionHandler object does not have histogram metadata associated with it."
                      "Skipping histogram processing.")
        return {}, [], {}

    colors = []
    for rect in dh.histogram[2]:
        rect_color = rect.get_facecolor()
        if rect_color not in colors:
            colors.append(to_rgb(rect_color))

    colors.append(to_rgb(dh.ax.get_facecolor()))

    contrast_ratios_by_index = {}
    detections = {}

    for i in range(len(colors)):
        for j in range(len(colors)):
            contrast_ratios_by_index[f'{i}{DELIMITER}{j}'] = \
                calculate_contrast_ratio(colors[i], colors[j])

    for key in contrast_ratios_by_index.keys():
        ind_str1, ind_str2 = key.split(DELIMITER)
        if ind_str1 == ind_str2:
            continue  # Don't do self-analysis for contrast ratio.
        if is_contrast_ratio_below_threshold(contrast_ratios_by_index[key]):
            # TODO: Need to do better handling of threshold based on plot
            detections[key] = contrast_ratios_by_index[key]

    return contrast_ratios_by_index, colors, detections


def calculate_contrast_ratio_lines(dh: DetectionHandler):
    """
    Generates a dictionary of contrast ratios from an Axes object,
    the corresponding colors of the lines and background, and
    a dictionary of comparisons that have a contrast ratio below
    a given threshold.

    1) Get color of all lines as rgb and append to list
    2) Get color of the background and append to list
    3) Do an n**2 comparison of colors in the above list and generate contrast ratios.
       These are stored as key/value mappings where the key is `<index_color1>_<index_color2>`.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    Returns
    -------
    contrast_ratios_by_index: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    line_colors: list
        List where each element is a tuple of `(r, g, b)` where `r`, `g`, and `b` are
        normalized from the 0->255 value down to a 0->1 value.
    detections: dict
        Dictionary where the key is the indices of the lines/background being compared
        and the value is the contrast ratio as a float.
    """

    lines = dh.ax.lines
    colors = [to_rgb(line.get_color()) for line in lines]
    colors.append(to_rgb(dh.ax.get_facecolor()))

    contrast_ratios_by_index = {}
    detections = {}

    for i in range(len(colors)):
        for j in range(len(colors)):
            if i != len(lines):
                left = lines[i].get_label()
            else:
                left = BACKGROUND
            if j != len(lines):
                right = lines[j].get_label()
            else:
                right = BACKGROUND
            print("key and indices:", i, left, j, right)
            key = f'{left}{DELIMITER}{right}'
            contrast_ratios_by_index[key] = \
                calculate_contrast_ratio(colors[i], colors[j])

    for key in contrast_ratios_by_index.keys():
        ind_str1, ind_str2 = key.split(DELIMITER)
        if ind_str1 == ind_str2:
            continue  # Don't do self-analysis for contrast ratio.
        if is_contrast_ratio_below_threshold(contrast_ratios_by_index[key]):
            # TODO: Need to do better handling of threshold based on plot
            detections[key] = contrast_ratios_by_index[key]

    return contrast_ratios_by_index, colors, detections


def calculate_contrast_ratio(rgb1, rgb2):
    """
    Calculates the contrast ratio given two tuples of normalized rgb values.
    These values must be in the range of [0,1].

    Parameters
    ----------
    rgb1: tuple
        A tuple of 3 values that are [0,1] which represent the normalized RGB
        values converted from the 8-bit 0-255 representation.
    rgb2: tuple
        A tuple of 3 values that are [0,1] which represent the normalized RGB
        values converted from the 8-bit 0-255 representation.

    Returns
    -------
    contrast_ratio: float
        Contrast ratio calculated from the relative luminance of two
        normalized rgb tuples of values.

    References
    ----------
    .. [1] https://www.w3.org/TR/WCAG20/#relativeluminancedef
    .. [2] https://contrast-ratio.com/
    .. [3] https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html
    """

    l1 = calculate_relative_luminance(rgb1)
    l2 = calculate_relative_luminance(rgb2)

    if l1 > l2:
        contrast_ratio = (l1 + 0.05) / (l2 + 0.05)
    else:
        contrast_ratio = (l2 + 0.05) / (l1 + 0.05)

    return contrast_ratio


def calculate_relative_luminance(rgb: tuple):
    """
    Calculates the relative luminance given a tuple of normalized rgb values.
    These values must be in the range of [0,1]. This is used to calculate
    contrast ratios.

    Parameters
    ----------
    rgb: tuple
        A tuple of 3 values that are [0,1] which represent the scaled RGB
        values converted from the 8-bit 0-255 representation.

    Returns
    -------
    relative_luminance: float
        The light intensity of a given color value.

    Notes
    -----
    Observing the coefficients in the formula helps to determine the
    contributing effects of `r`, `g`, and `b` to relative luminance. We
    can see that `g` gives the greatest contribution to relative luminance.

    Raises
    ------
    ValueError
        Raises if `r`, `g`, or `b` are not in a normalized [0,1] form.

    References
    ----------
    .. [1] https://www.w3.org/TR/WCAG20/#relativeluminancedef
    """

    r, g, b = rgb
    # Check to make sure the appropriate normalized rgb value is passed in.
    if (not 0.0 <= r <= 1.0) or (not 0.0 <= g <= 1.0) or (not 0.0 <= b <= 1.0):
        raise ValueError(f"The values of r:{r}, g:{g}, or b:{b} are not all within [0,1]!")

    r = normalize(r)
    g = normalize(g)
    b = normalize(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def normalize(primary_color: float):
    """
    Normalize the , G, or B value using the WCAG 2.0 formula defined
    for calculating the relative luminance.

    Parameters
    ----------
    primary_color: float
        Value for r, g, or b in the scaled in the range [0,1]

    Returns
    -------
    normalized_color: float
        Normalizes the value based on if it is `>0.03928` or not.

    References
    ----------
    .. [1] https://www.w3.org/TR/WCAG20/#relativeluminancedef
    """

    if primary_color <= 0.03928:
        normalized_color = primary_color / 12.92
    else:
        normalized_color = ((primary_color + 0.055) / 1.055) ** 2.4

    return normalized_color
