.. _api_ref:

*************
API Reference
*************

.. include:: ../includes/api_css.rst

This is the class and function reference for ``accessiplot``. Please refer to
the :ref:`full user guide <user_guide>` for further details, as the class and
function raw specifications may not be enough to give full guidelines on their
uses.


================================================================
:mod:`accessiplot.detection`: Inaccessibility Detection of Plots
================================================================

The ``accessiplot.detection`` sub-module defines a set of tests of accessibility.

.. currentmodule:: accessiplot.detection

Contrast Ratio Detection
************************
.. autosummary::
    :toctree: generated/
    :template: function.rst

    contrast_ratio.is_contrast_ratio_below_threshold
    contrast_ratio.calculate_contrast_ratios_from_ax
    contrast_ratio.calculate_contrast_ratio
    contrast_ratio.calculate_relative_luminance
    contrast_ratio.normalize

Missing Label Detection
***********************

.. autosummary::
    :toctree: generated/
    :template: function.rst

    label.get_missing_labels_from_ax

Missing Marker Detection
************************
.. autosummary::
    :toctree: generated/
    :template: function.rst

    marker.get_markers


Detection Handler Classes
*************************

.. autosummary::
    :toctree: generated/
    :template: class.rst

    handler.DetectionHandler
    handler.DetectionTypes


=======================================================
:mod:`accessiplot.utils`: Utility Functions and Classes
=======================================================

.. currentmodule:: accessiplot.utils

Chart Type Enum
****************

.. autosummary::
    :toctree: generated/
    :template: class.rst

    chart_type.ChartTypes


Chart Type Detection
********************
.. autosummary::
    :toctree: generated/
    :template: function.rst
    
    chart_type.determine_chart_type