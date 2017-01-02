#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['']


setup(name='tomber',
    version='1.0.4',
    description='a python Tomb (the Crypto Undertaker) wrapper',
    long_description=read('README.mkdn'),
    license="BSD",
    author='Federico Reiven',
    author_email='reiven@gmail.com',
    url='https://github.com/reiven/tomber',
    keywords='tomb wrapper',
    packages=find_packages(),
    install_requires=requires,
    )
