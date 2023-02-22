import matplotlib

def get_labels(plt:matplotlib.pyplot):
    axes_object = plt.gca()
    labels = [line.get_label() for line in axes_object.lines]
    for label in labels:
        print(label)