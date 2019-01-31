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


## Building upstream doc with this theme
Building the upstream OpenStack docs with the SUSE theme is very similar to the Manual Installation described above:

1. Checkout the project with the desired docs (for example: `git clone git://git.openstack.org/openstack/nova`)
2. Build the local project normally (typically `tox -edocs`), see the local project documentation for details (e.g. doc/source/contributor/development-environment.rst for nova)
3. Within the docs folder of the project, update conf.py and set `html_theme = 'suse_sphinx_theme'` and add `'suse_sphinx_theme',` to the extensions list (conf.py is typically under doc/source)
4. Manually install the theme into the tox environment, this will vary a little depending on where the `suse_sphinx_theme` is cloned, for example (from the Nova top level folder in this case) `.tox/docs/bin/pip install -e ~/upstream/suse-sphinx-theme/`
5. re-run the tox build job `tox -edocs`
6. the output of the Nova doc build is under `doc/build/html` , other projects may output to a different location
