# -*- coding: utf-8 -*-

from setuptools import setup
from ftrack_sphinx_rtd_theme import __version__

setup(
    name='ftrack_sphinx_rtd_theme',
    version=__version__,
    url='https://bitbucket.org/ftrack/ftrack-sphinx-rtd-theme',
    license='MIT',
    author='Mattias Seebergs, Dave Snider',
    author_email='mattias.seebergs@ftrack.com, dave.snider@gmail.com',
    description='ftrack version of the Read The Docs theme for Sphinx.',
    zip_safe=False,
    packages=['ftrack_sphinx_rtd_theme'],
    package_data={'ftrack_sphinx_rtd_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines()
)
