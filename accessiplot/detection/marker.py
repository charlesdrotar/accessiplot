import matplotlib


__all__ = [
    'get_markers'
]

def get_markers(plt):
    """
    Dummy function to prove out retrieving a list of markers given a 
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
    markers = [line.get_marker() for line in axes_object.lines]
    for marker in markers:
        print(marker)
