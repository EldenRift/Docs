# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
project = 'Elden Rift'
copyright = '2025, Elden Rift'
author = 'Chayy'

# -- General configuration ---------------------------------------------------

# Add the myst-parser extension
extensions = ['myst_parser']

# Set the source suffix for Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',  # This enables Markdown files
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"  # Furo theme is compatible with Markdown
html_static_path = ['_static']

html_logo = "minecraft_titlepng.png"
html_favicon = "minecraft_titlepng.png"
html_theme_options = {
    "sidebar_hide_name": True,
}
html_css_files = ["custom.css"]
html_baseurl = "https://eldenrift.github.io/Docs/"