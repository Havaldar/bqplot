# -*- coding: utf-8 -*-
#
# bqplot documentation build configuration file, created by
# sphinx-quickstart on Thu Oct  8 15:45:33 2015.
#
# NOTE: This file has been edited manually from the auto-generated one from
# sphinx.  Do NOT delete and re-generate.  If any changes from sphinx are
# needed, generate a scratch one and merge by hand any new fields needed.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../bqplot/'))

# We load the bqplot release info into a dict by explicit execution
_release = {}
exec(compile(open('../../bqplot/_version.py').read(), '../../bqplot/_version.py', 'exec'), _release)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'jupyter_sphinx',
    'sphinx_thebe'
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# Add dev disclaimer.
if _release['version_info'][-1] == 'dev':
    rst_prolog = """
    .. note::

        This documentation is for a development version of bqplot. There may be
        significant differences from the latest stable release.

    """

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'bqplot'
copyright = u'2015, Bloomberg LP'
author = u'The BQplot Development Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(map(str, _release['version_info'][:2]))
# The full version, including alpha/beta/rc tags.
release = _release['__version__']

language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = 'bqplotdoc'

# -- Options for thebe ---------------------------------------------

thebe_config = {
    "always_load": False,
    "selector": "div.jupyter_cell",
    "selector_output": "div.cell_output",
    "repository_url": "https://github.com/bqplot/bqplot",
    "repository_branch": "stable",
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'bqplot.tex', u'bqplot Documentation',
   u'Bloomberg LP', 'manual'),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'bqplot', u'bqplot Documentation',
     [u'Bloomberg LP'], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'bqplot', u'bqplot Documentation',
   u'Bloomberg LP', 'bqplot', 'One line description of project.',
   'Miscellaneous'),
]
