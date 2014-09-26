#!/usr/bin/env python
# -*- coding: utf-8-*-
from setuptools import setup

long_description = 'Please see https://github.com/Holzhaus/python-cmuclmtk for details.'
if os.access('README.md', os.R_OK):
      with open('README.md') as f:
            long_description = f.read()

setup(name='cmuclmtk',
      version='0.1.4',
      description='Wrapper library for accessing the language model tools for CMU Sphinx (CMUCLMTK).',
      long_description=long_description,
      author='Jan Holthuis',
      author_email='holthuis.jan@googlemail.com',
      license='BSD',
      url='https://github.com/Holzhaus/python-cmuclmtk',
      packages=['cmuclmtk'],
      keywords='cmu sphinx cmuclmtk language modeling training vocabulary dictionary vocab dict',
      zip_safe=True
    )
