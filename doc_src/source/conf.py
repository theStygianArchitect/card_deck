# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from pathlib import Path

import toml

sys.path.insert(0, os.path.abspath('../../'))

# Extract project information variables from pyproject.toml
current_file = Path(__file__)
project_directory = current_file.parents[2]
toml_text = Path(f'{project_directory.resolve()}/pyproject.toml').read_text(encoding='Latin-1')
package_info = toml.loads(toml_text)
project_info = package_info['project']

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

authors = [author['name'] for author in project_info.get('authors')]

project = project_info.get('name')
copyright = ', '.join(authors)
author = ', '.join(authors)
version = project_info.get('version')
release = project_info.get('version')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_immaterial',
]

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_immaterial'
html_theme_options = {
    'site_url' : 'https://pages.github.com/theStygianArchitect/card_deck',
    'repo_url' : 'https://github.com/theStygianArchitect/card_deck',
    'repo_name': 'card_deck',
    'repo_type': 'github',
    'icon'     : {
        'repo': 'fontawesome/brands/github',
    },
    "features" : [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    'palette'  : [
        {
            'media'  : '(prefers-color-scheme: light)',
            'scheme' : 'default',
            'primary': 'indigo',
            'toggle' : {
                'icon': 'material/toggle-switch-off-outline',
                'name': 'Switch to dark mode',
            }
        },
        {
            'media'  : '(prefers-color-scheme: dark)',
            'scheme' : 'slate',
            'primary': 'purple',
            'toggle' : {
                'icon': 'material/toggle-switch',
                'name': 'Switch to light mode',
            }
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

# -- sphinx markdown-it ------------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md' : 'markdown',
}

# Myst configuration
myst_all_links_external = True
