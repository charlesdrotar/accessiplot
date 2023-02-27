# Configuration file for the Sphinx documentation builder.

# -- Project information
import datetime
import os
import sys

project = 'accessiplot'
copyright = '2023, Charles B Drotar'
author = 'Charles B Drotar'

release = '0.0.1'
version = '0.0.1'

sys.path.insert(0, os.path.abspath('..' + os.path.sep))
sys.path.insert(0, os.path.abspath('sphinxext'))

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_gallery.gen_gallery',
    'numpydoc'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_class_members_toctree = False
autodoc_default_flags = ['members', 'inherited-members']

# generate autosummary even if no references
autosummary_generate = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# -- Set master doc to index
master_doc = 'index'

language = "en"

# General information about the project.
project = 'accessiplot'
year = datetime.datetime.now().year
copyright = '2023-{0}, Charles B Drotar'.format(year)
author = 'Charles B Drotar'

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/accessibility.html
html_theme = 'pydata_sphinx_theme'
# html_theme = 'sphinx_rtd_theme'


html_theme_options = {
   "logo": {
      "image_light": "logo-light.png",
      "image_dark": "logo-dark.png",
   }
}

# -- Options for EPUB output
epub_show_urls = 'footnote'


sphinx_gallery_conf = {
    'doc_module': 'accessiplot',
    'backreferences_dir': os.path.join('modules', 'generated'),
    'reference_url': {'accessiplot': None},
    'filename_pattern': '/example_',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
    def adds(pth):
        print("Adding stylesheet: %s" % pth)
        app.add_css_file(pth)

    adds('css/fields.css')  # for parameters, etc.
