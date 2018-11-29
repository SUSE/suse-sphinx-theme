(c) Copyright 2018 SUSE LLC

# Branding
SUSE branding for documentation built with Sphinx

To use the SUSE Sphinx theme, do the following:

1. Copy the susedocs folder from this repo to the base directory for your Sphinx documentation
2. Open conf.py and set `html_theme = 'susedocs'` , `html_theme_path = ['.']`, and `html_theme_options = {}` if they are not already set
3. Rebuild your documentation (typically `make clean html`)

This theme is derived from the openstackdocstheme at https://github.com/openstack/openstackdocstheme , and is heavily modified.

