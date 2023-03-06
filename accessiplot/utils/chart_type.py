from enum import Enum


class ChartTypes(Enum):
    """
    Enum used to keep track of supported chart types
    """
    LINE_CHART = 1
    HISTOGRAM = 2
    SCATTERPLOT = 3


def determine_chart_type(ax):
    """
    Determines the chart type based on the Axes object.
    Currently it just checks if there are lines are not.
    This should be more intelligent.

    Parameters
    ----------
    ax: Axes object
        Matplotlib Axes object.

    Returns
    -------
    graph_type: str
        ChartTypes enum name for supported chart type.
    """
    graph_type = ChartTypes.LINE_CHART.name
    if len(ax.get_lines()) == 0:
        graph_type = ChartTypes.HISTOGRAM.name
    # TODO: Add support for other chart types.
    # TODO: This should also have more intelligence above checking line numbers.
    return graph_type
