import matplotlib

__all__ = [
    'get_labels'
]

def get_labels(plt):
    """
    Simple function to get the labels.
    """
    axes_object = plt.gca()
    labels = [line.get_label() for line in axes_object.lines]
    for label in labels:
        print(label)
