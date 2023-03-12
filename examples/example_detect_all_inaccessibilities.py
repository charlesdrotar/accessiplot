"""
==========================================
General Detection of all Inaccessibilities
==========================================
This example shows how to detect all inaccessiblities and
write the output as a JSON.
"""

from accessiplot.detection.handler import DetectionHandler, DetectionTypes
import matplotlib.pyplot as plt
import numpy as np


# data to be plotted
x = np.arange(1, 11)
_ = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
num_lines = 10

# Reset the figure so that tests start with a fresh figure.
_ = plt.figure()
ax = plt.axes()
for _ in range(num_lines):
    y_val = (np.random.rand(1, 10)).T
    ax.plot(x, y_val)

dh = DetectionHandler(ax=ax)
dh.run_detections(run_detections_list=DetectionTypes.ALL())

for key in dh.detections.keys():
    print(key, ":", dh.detections[key])
