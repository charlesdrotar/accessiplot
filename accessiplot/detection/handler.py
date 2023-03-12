from accessiplot.utils.chart_type import determine_chart_type
from accessiplot.utils.logger import logger
from enum import Enum
import matplotlib.pyplot as plt


class ExtendedEnum(Enum):
    """
    Extend the functionality of the Enum class to have a means to get all values.
    """
    @classmethod
    def ALL(self):
        return list(map(lambda c: c.name, self))


class DetectionTypes(ExtendedEnum):
    """
    Enum used to keep track of supported detection tests.
    """
    CONTRAST_RATIO = 1  # i.e. calculate contrast ratios
    LABEL = 2  # i.e. missing labels
    MARKER = 4  # i.e. missing markers
    COLOR = 8  # i.e. Color-blindness
    OVERCOMPLEXITY = 16  # i.e. overly complex graph.


class DetectionHandler():
    """
    This is the entry point for generating detection outputs for a given axes
    object. It takes a matplotlib axes object and runs a set of detections
    specified by the user when they call `self.run_detections()`. Additionally
    when running on a histogram plot, additional context must be passed in
    to the `histogram` parameter to be able to get the proper colors and labels.

    Parameters
    ----------
    ax: Axes object
        Matplotlib Axes object.

    histogram: tuple
        A tuple of histogram metadata from calling ax.hist()
    """

    def __init__(self, ax, histogram=None):
        self.ax = ax
        self.histogram = histogram
        self.chart_type = determine_chart_type(self.ax)
        self.detections = {}

    def run_detections(self, run_detections_list):
        """
        Run specific list of detections and generate results in a JSON
        formatted output and store that in self.detections.

        Parameters
        ----------
        run_detections_list: list of str
           A list of DetectionTypes enum names to run on a given axes.
        """

        from accessiplot.detection.contrast_ratio import calculate_contrast_ratios_from_ax
        from accessiplot.detection.label import get_missing_labels_from_ax
        from accessiplot.detection.color_detection import full_detection
        from accessiplot.detection.visual_complexity import get_complexity

        # Run detection cases based on which were selected by user.
        detections = {}
        if DetectionTypes.CONTRAST_RATIO.name in run_detections_list:
            logger.info(f"Running detections for '{DetectionTypes.CONTRAST_RATIO.name}'")
            self.contrast_ratios_by_index, self.colors_by_index, contrast_detections = calculate_contrast_ratios_from_ax(self)
            detections[DetectionTypes.CONTRAST_RATIO.name] = contrast_detections
        if DetectionTypes.LABEL.name in run_detections_list:
            logger.info(f"Running detections for '{DetectionTypes.LABEL.name}'")
            _, _, _, label_detections = get_missing_labels_from_ax(self)
            detections[DetectionTypes.LABEL.name] = label_detections
        if DetectionTypes.COLOR.name in run_detections_list:
            logger.info(f"Running detections for '{DetectionTypes.COLOR.name}'")
            _, color_detections = full_detection(plt=plt)
            detections[DetectionTypes.COLOR.name] = color_detections
        if DetectionTypes.OVERCOMPLEXITY.name in run_detections_list:
            logger.info(f"Running detections for '{DetectionTypes.OVERCOMPLEXITY.name}'")
            _, overcomplexity_detections = get_complexity(plt=plt)
            detections[DetectionTypes.OVERCOMPLEXITY.name] = overcomplexity_detections

        self.detections = detections
