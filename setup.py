#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distutils.core import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-gibberish',
    version=__import__('gibberish').get_version().replace(' ', '-'),
    description='Turn perfectly proofread sites into a dyslectic paradise.',
    long_description=README,
    author='Daniel J. Becker',
    author_email='hello@danieljbecker.de',
    packages=('gibberish',),
    license='GPL',
)
