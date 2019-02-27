(c) Copyright 2018 SUSE LLC

# Branding
SUSE branding for documentation built with Sphinx

# Installing

## Install as package

In order to automatically install the theme, do the following

1. Checkout this repository:
   ```
   git checkout https://github.com/SUSE/suse-sphinx-theme.git
   ```
2. Install:
   ```
   python setup.py install
   ```
3. Change the theme name in your `conf.py`:
   ```
   html_theme = 'suse_sphinx_theme'
   ```
4. Start building with the new theme
   ```
   make html
   ```

## Manual installation
To use the SUSE Sphinx theme, do the following:

1. Copy the suse_sphinx_theme folder from this repo to the base directory for your Sphinx documentation
2. Open conf.py and set `html_theme = 'suse_sphinx_theme'` , `html_theme_path = ['.']`, and `html_theme_options = {}` if they are not already set
3. Rebuild your documentation (typically `make clean html`)

This theme is derived from the openstackdocstheme at https://github.com/openstack/openstackdocstheme , and is heavily modified.

