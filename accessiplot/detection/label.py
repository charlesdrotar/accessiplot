from accessiplot.detection.handler import DetectionHandler
from accessiplot.utils.chart_type import ChartTypes
from accessiplot.utils.logger import logger
import warnings


__all__ = [
    'get_missing_labels_from_ax',
    'get_missing_labels_lines',
    'get_missing_labels_histograms'
    ''
]


def get_missing_labels_histograms(dh: DetectionHandler):
    """
    Dummy function to prove out retrieving a list of labels given a
    Matplotlib pyplot object.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    Returns
    -------
    bin_labels: list
        list of labels for each line.
    x_label: str
        label for the x-axis.
    y_label: str
        label for the y-axis.
    detections: dict
        Dictionary of lines and axes that are missing labels.
    """

    labels = []  # TODO: Need to add logic to check for bin labels.
    detections = {"bins": {}, "axes": {}}
    x_label = dh.ax.get_xlabel()
    y_label = dh.ax.get_ylabel()
    legend = dh.ax.get_legend()
    title = dh.ax.get_title()

    # Check default values and log detections
    if x_label == "":
        logger.warning("Missing x-axis label")
        detections["axes"]["x"] = ""
    if y_label == "":
        logger.warning("Missing y-axis label")
        detections["axes"]["y"] = ""
    if title == "":
        logger.warning("Missing plot title")
        detections["title"] = ""
    if legend is None:
        logger.warning("Missing plot title")
        detections["legend"] = None

    return labels, x_label, y_label, detections


def get_missing_labels_lines(dh: DetectionHandler):
    """
    Retrieves the labels from the lines and axes and determines
    if they are the default value or empty strings. If they
    are not overridden then we flag as detections.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    Returns
    -------
    line_labels: list
        list of labels for each line.
    x_label: str
        label for the x-axis.
    y_label: str
        label for the y-axis.
    detections: dict
        Dictionary of lines and axes that are missing labels.
    """

    labels = [line.get_label() for line in dh.ax.lines]
    detections = {"lines": {}, "axes": {}}
    x_label = dh.ax.get_xlabel()
    y_label = dh.ax.get_ylabel()
    legend = dh.ax.get_legend()
    title = dh.ax.get_title()

    for i in range(len(labels)):
        label = labels[i]
        # '_child' is the default name for a label by matplotlib.
        if label.startswith('_child'):
            logger.warning(f"Missing label for line#{i}:{label}")
            detections["lines"][i] = label

    # Check default values and log detections
    if x_label == "":
        logger.warning("Missing x-axis label")
        detections["axes"]["x"] = ""
    if y_label == "":
        logger.warning("Missing y-axis label")
        detections["axes"]["y"] = ""
    if title == "":
        logger.warning("Missing plot title")
        detections["title"] = ""
    if legend is None:
        logger.warning("Missing plot title")
        detections["legend"] = None

    return labels, x_label, y_label, detections


def get_missing_labels_from_ax(dh: DetectionHandler):
    """
    Generates dictionaries of the contrast_ratios_by_index and detections.
    Also a list of colors_by_index is generated to keep track of the colors
    that are associated with the contrast ratios.
    It determines the processing logic based on the chart type.

    Parameters
    ----------
    dh : accessiplot.detection.handler.DetectionHandler
        A DetectionHandler object that contains the axes object and histogram object if necessary.

    chart_type: str
        accessiplot.utils.chart_type.ChartType enum name

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
    labels = []
    x_label = ""
    y_label = ""
    detections = {}

    if dh.chart_type == ChartTypes.LINE_CHART.name:
        labels, x_label, y_label, detections = get_missing_labels_lines(dh)
    elif dh.chart_type == ChartTypes.HISTOGRAM.name:
        labels, x_label, y_label, detections = get_missing_labels_histograms(dh)
    else:
        warnings.warn(f"chart_type:{dh.chart_type} is unsupported! Returning dummy values for analysis")
    return labels, x_label, y_label, detections
