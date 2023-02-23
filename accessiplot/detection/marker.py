import matplotlib


__all__ = [
    'get_markers'
]

def get_markers(plt):
    """
    Simple function to get the markers
    """
    axes_object = plt.gca()
    markers = [line.get_marker() for line in axes_object.lines]
    for marker in markers:
        print(marker)
