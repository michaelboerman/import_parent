# Sphinx configuration for ReadTheDocs using MyST and autodoc
import os
import sys
from datetime import datetime

# ensure project root is on sys.path so autodoc can import import_parent
sys.path.insert(0, os.path.abspath(".."))

project = "import_parent"
author = "Michael Boerman"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# MyST parser settings (optional tweaks)
myst_enable_extensions = [
    "deflist",
    "html_admonition",
    "html_image",
]
autodoc_member_order = "bysource"
