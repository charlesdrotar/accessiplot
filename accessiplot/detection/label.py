
__all__ = [
    'get_labels'
]


def get_labels(plt):
    """
    Dummy function to prove out retrieving a list of labels given a
    Matplotlib pyplot object.

    Parameters
    ----------
    plt : matplotlib.plt
        Matplotlib pyplot object

    Notes
    -----
    This is incomplete and is just meant to prove out simple retrieval.
    """

    axes_object = plt.gca()
    labels = [line.get_label() for line in axes_object.lines]
    for label in labels:
        print(label)
