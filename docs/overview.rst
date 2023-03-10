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

Data visualization is the process of transforming data into graphics. Those visual representations make 
it easier for people to understand and interpret complex data. However, as its name suggests, 
visualizations mainly make use of visual cues to convey information. This makes it difficult for 
people with disabilities to access the information embedded in visualizations. As `L??onie Watson`_ ,
a screen reader user said at the `Accessibility Fireside Chat`_ : *"One of the hardest things I've discovered 
about trying to use or access data visualizations is the amount of information I need to keep in my head to 
be able to make sense of it."*

As an attempt to detect the accessibility issues in Python visualizations, Accessiplot is inspired by the existing
effort of making data visualizations more accessible in both the design and the development phase. For example,
we refer to the `Web Content Accessibility Guidelines (WCAG) for complex images`_ to determine which accessibility
issues we should prioritize detecting, and how we should detect them. Moreover, our decision to take an infrastructure
perspective (i.e., focus on *creating* accessible visualizations) instead of an individual approach is sparked by
libraries that make JavaScript visualizations more accessible, such as `HighCharts`_ and `VoxLens`_ .


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

The disability justice principle that informed our project is collective access. 
Currently, there lacks a solution for enforcing accessibility guidelines on Python visualizations, 
which makes it difficult for people with disabilities to access the information embedded on those visualizations. 
Therefore, we are developing this package in the hope that nobody will not be left behind by this pervasive and 
important form of conveying information. 


Learnings and Future Work
-------------------------

Through this project, we have gained valuable insights on how to extend the application of the WCAG guidelines 
beyond websites to Python visualizations. In particular, we have delved deep into some specific areas,
such as calculating contrast ratios, simulating color vision deficiency, and identifying overcomplexity.
We have also learned how to break down a Matplotlib object in order to evaluate whether its key components meet 
the guidelines. 

There are many possible avenues for future work on this project. Currently, Accessiplot only detect
certain accessiblity issues on line charts and histograms. In the future, we aim to expand its functionalities
to encompass more accessibility issues as well as other forms of visualizations generated by Matplotlib.
In addition, we hope to evaluate the library's effectiveness with data scientists who use Matplotlib to create 
data visualizations in a regular basisto learn whether or not they find the library user-friendly and helpful. 
We would also like to learn whether or not people with disabilities find the visualizations generated with library's
assistance to be more accessible. 

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
.. _L??onie Watson: https://tink.uk/
.. _Accessibility Fireside Chat: https://www.youtube.com/watch?v=Aqx5PQwds80&t=401s
.. _Web Content Accessibility Guidelines (WCAG) for complex images: https://www.w3.org/WAI/tutorials/images/complex/
.. _HighCharts: https://www.highcharts.com/docs/accessibility/accessibility-module
.. _VoxLens: https://github.com/athersharif/voxlens