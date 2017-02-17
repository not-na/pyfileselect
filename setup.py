#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  setup.py
#  
#  Copyright 2017 notna <notna@apparat.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Distribution command:
# sudo python setup.py install sdist bdist register upload

import imp

def load_module(name):
    names = name.split(".")
    path = None
    for name in names:
        f, path, info = imp.find_module(name, path)
        path = [path]
    return imp.load_module(name, f, path[0], info)    

ver = load_module("pyfileselect.version")

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

# Fix for very old python versions from https://docs.python.org/2/distutils/setupscript.html#additional-meta-data
# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

try:
    longdesc = open("README.txt","r").read()
except Exception:
    longdesc = "Simple and Portable Native File Selection Dialog for Python"

# Extension setup
# Disabled until functional
#ext_native = Extension('pyfileselect._nativefileselect',
#                       sources = ['pyfileselect/_nativefileselect.c'])

# Main setup
setup(name='pyfileselect',
      version=ver.VERSION,
      description="Simple and Portable Native File Selection Dialog for Python", # from the github repo
      long_description=longdesc,
      author="notna",
      author_email="notna@apparat.org",
      url="https://github.com/not-na/pyfileselect",
      packages=['pyfileselect'],
      requires=[],
      provides=["pyfileselect"],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      #ext_modules=[ext_native],
      #include_dirs=["./nativefiledialog/src/include/"],
      classifiers=[
        "Development Status :: 4 - Beta",
        
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        
        "License :: OSI Approved",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        
        "Topic :: Software Development :: Libraries :: Python Modules",
        
        ],
      )
