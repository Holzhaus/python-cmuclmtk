#!/usr/bin/env python
# -*- coding: utf-8-*-
from setuptools import setup

setup(name='cmuclmtk',
      version='0.1.2',
      description='Wrapper library for accessing the language model tools for CMU Sphinx (CMUCLMTK).',
      long_description=open('README.rst').read(),
      author='Jan Holthuis',
      author_email='holthuis.jan@googlemail.com',
      license='BSD',
      url='https://github.com/Holzhaus/python-cmuclmtk',
      packages=['cmuclmtk'],
      keywords='cmu sphinx cmuclmtk language modeling training vocabulary dictionary vocab dict',
      zip_safe=True
    )
