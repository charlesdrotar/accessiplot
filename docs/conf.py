# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'accessiplot'
copyright = '2023, Charles Drotar'
author = 'Charles Drotar'

release = '0.0.1'
version = '0.0.1'

import os
import sys
import datetime
import warnings


sys.path.insert(0, os.path.abspath('..' + os.path.sep))
sys.path.insert(0, os.path.abspath('sphinxext'))

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'numpydoc'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_class_members_toctree = False

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Set master doc to index
master_doc = 'index'