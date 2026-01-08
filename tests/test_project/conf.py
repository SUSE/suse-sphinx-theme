import os
import sys

# Add the theme to the path so it can be imported without installation
sys.path.insert(0, os.path.abspath("../../"))

import suse_sphinx_theme

extensions = []
html_theme = "suse_sphinx_theme"
html_theme_path = [suse_sphinx_theme.get_html_theme_path()]
project = "Minimal Test"
copyright = "SUSE"
author = "SUSE"
