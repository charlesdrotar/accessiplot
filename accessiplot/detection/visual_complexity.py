from accessiplot.utils.logger import logger
from pae import PAEMeasure

__all__ = [
    'get_complexity'
]


def get_complexity(plt, threshold: float = 0.5):
    """
    Given a line chart, calculate its visual complexity
    based on Pixel Approximate Entropy.

    Parameters
    ----------
    plt: matplotlib.plt
        Matplotlib pyplot object
    threshold: float
        Threshold to detect if the visual complexity score is above it.

    Returns
    -------
    score: float
        The visual complexity score based on Pixel Approximate Entropy.

    References
    ----------
    .. [1] https://doi.org/10.48550/arXiv.1811.03180
    """
    detections = {}
    pae_means = PAEMeasure(300, 200)
    score = 0
    axes_object = plt.gca()
    lines = [line.get_data() for line in axes_object.lines]
    # print(lines)
    for line in lines:
        score += pae_means.pae(line[1])
    score *= len(lines)
    if score >= threshold:
        logger.warning('The line chart has a high visual complexity score:\n"\
                     "threshold = {} v.s. actual = {}.'.format(threshold, score))
        detections = {"Pixel Approximate Entropy": score, "threshold": threshold}
    return score, detections
