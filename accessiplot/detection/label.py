
__all__ = [
    'get_labels'
]


def get_labels(ax):
    """
    Dummy function to prove out retrieving a list of labels given a
    Matplotlib pyplot object.

    Parameters
    ----------
    ax : matplotlib.axes
        Matplotlib pyplot object

    Notes
    -----
    This is incomplete and is just meant to prove out simple retrieval.
    """

    line_labels = [line.get_label() for line in ax.lines]
    detections = {"lines": {}, "axes": {}}
    x_label = ax.get_xlabel()
    y_label = ax.get_ylabel()

    for i in range(len(line_labels)):
        label = line_labels[i]
        # '_child' is the default name for a label by matplotlib.
        if label.startswith('_child'):
            detections["lines"][i] = label

    # Check if the x and y axes of the plot are empty strings.
    if ax.get_xlabel() == "":
        detections["axes"]["x"] = ""
    if ax.get_ylabel() == "":
        detections["axes"]["y"] = ""

    return line_labels, x_label, y_label, detections
