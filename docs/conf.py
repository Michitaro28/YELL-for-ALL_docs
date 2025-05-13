import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'YELL for ALL'
author = 'Sugawara Michitaro'
copyright = f'{datetime.now().year}, {author}'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'myst_parser',
    'sphinx_copybutton',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.mermaid',
    'sphinx_tabs.tabs',
    'sphinx_togglebutton',
    'sphinx_design',
    'sphinx_click',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "replacements",
    "substitution",
    "smartquotes",
    "tasklist",
    "dollarmath",
    "amsmath",
    "html_admonition",
]

todo_include_todos = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'ja'

# -- Theme --------------------------------------------------------------------
html_theme = "pydata_sphinx_theme"  # ← 他に furo や pydata_sphinx_theme ,sphinx-book-themeに切替可
html_static_path = ['_static']
html_css_files = []
html_js_files = []

# -- PlantUML & Mermaid -------------------------------------------------------
plantuml = "java -jar ./utils/plantuml.jar"
mermaid_cmd = "mmdc"

# -- Intersphinx --------------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_static_path = ['_static']
