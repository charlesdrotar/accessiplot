import matplotlib

def get_markers(plt:matplotlib.pyplot):
    axes_object = plt.gca()
    markers = [line.get_marker() for line in axes_object.lines]
    for marker in markers:
        print(marker)
