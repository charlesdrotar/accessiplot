.. _overview:

========
Overview
========

.. image:: ./imgs/accessibility.png
    :align: center
    :scale: 60%
    :alt: Apple's Accessibility Image

Introduction
------------

Currently data visualizations generated in python are mostly inaccessible. There are a variety of
accessibility issues that surface regularly

- **missing labels detection** (for those using screenreaders)
- **contrast ratio detection** (for those who are BLV)
- **color detection** (for those with visual impairments)
- **overlycomplexity detection** (for those with cognitive impairments)
- **text legibility detection** (for those with dyslexia)
- **alternative text detection** (for those who are BLV using screenreaders)
- **marker detection** (for those who are BLV)
- **MORE...**

Accessiplot is an attempt to help fix these problems at the time of creation of the plot. The 
solution is detection, detecting these issues before they are published as part of the code execution 
phase. It is much harder to address after a paper has been published given the collaborative 
nature of research and reproducibility issues.

Accessiplot is a python library that attempts to notify data scientists during the development process.
When a report is already generated and it is determined that it is not accessible it is already too late.
Catching this early on in the process is key. One main reason is the high percentage of research that is not
reproducible. Another reason is the amount of effort to recreate a graph and modify it to be accessible.

Accessiplot addresses the accessibility issues by notifying the user of accessibility issues at the time 
of plot generation and presenting that as actionable information. This is currently for **DETECTION**,
not **ADDRESSING** issues.


Related Work
------------

Related Work– 1-3 paragraphs: Talk about relevant work that closely connects with your project.


Methodology
-----------

We currently have 4 different different detections implemented:

(1) overcomplexity detection
<<<<<<<<<<<<<<<<<<<<<<<<<<<<

**Supported Graph Types:**

- Line Charts

Using `Pixel Approximate Entropy`_ we use this score as a measure to determine if the 
graph itself is overly complex. This can make a graph especially difficult
to process if you have cognitive disabilities. Additionally, it makes creating
adequate alternative text a harder task as well.

(2) contrast ratio detection
<<<<<<<<<<<<<<<<<<<<<<<<<<<<

**Supported Graph Types:**

- Line Charts
- Histograms

Using the WCAG guidelines to calculate contrast ratio, we take the rgb value of
two different components of the graph (line, bar, or background) and calculate the
relative luminance. From there we compare the two values, and it is the ratio of those 
values that leads to the contrast ratio

(3) missing label detection
<<<<<<<<<<<<<<<<<<<<<<<<<<<

**Supported Graph Types:**

- Line Charts
- Histograms

This code checks for labels on the x-axis and y-axis and in the case of line-charts - 
labels for every line. Missing labels for graphs make it especially difficult
to decipher complex graphs easily.

(4) color detection
<<<<<<<<<<<<<<<<<<<

**Supported Graph Types:**

- Line Charts
- Histograms

This code checks to see if there are issues with the color scheme for people of different
color-blindness disabilities. It also has the ability to simulate what a person with color-blindness
would see if they were to look at a given chart.

Disability Justice Perspective
------------------------------

Disability Justice Perspective– 1 paragraph: How did a disability studies perspective inform your project?


Learnings and Future Work
-------------------------

Learnings and future work – 1-2 paragraphs: Describe what you learned and how this can be extended/ built on in the future.


How you Made your App Accessible
--------------------------------

There is an emphasis on creating accessible documentation for the accessiplot library.
Using the `WAVE online accessibility tool`_ we were able to determine
that we really only have contrast ratio issues. Additionally we made sure that
the documentation is created on each pull request that is merged in so it is always current. Lastly,
there are a collection of examples in the :ref:`examples` section to help jumpstart any new user.
The goal of this library is to be an accessible library for accessibility.

..
    Hypertext links:

.. _WAVE online accessibility tool: https://wave.webaim.org/
.. _Pixel Approximate Entropy: https://doi.org/10.48550/arXiv.1811.03180