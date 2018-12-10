# -*- coding: utf-8 -*-
"""`suse_sphinx_theme` lives on `Github`_.

.. _github: https://github.com/SUSE/suse-sphinx-theme

"""
from io import open
from setuptools import setup
from susedocs import __version__


setup(
    name='suse_sphinx_theme',
    version=__version__,
    url='https://github.com/SUSE/suse-sphinx-theme',
    license='Apache',
    author='Jeremy Moffitt & contributors',
    author_email='jeremy.moffitt@suse.com',
    description='Sphinx Documentation theme that has SUSE branding',
    long_description=open('README.md', encoding='utf-8').read(),
    zip_safe=False,
    packages=['susedocs'],
    package_dir={'susedocs': 'susedocs'},
    package_data={'susedocs': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*',
        'static/favicon.ico'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'susedocs = susedocs',
        ]
    },
    install_requires=[
       'sphinx'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
