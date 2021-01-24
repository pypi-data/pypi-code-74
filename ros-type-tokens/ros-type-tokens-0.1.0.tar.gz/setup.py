# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

try:
    import regex as re
except ImportError:
    import re
import os
from setuptools import setup, find_packages

SOURCE = os.path.relpath(os.path.join(os.path.dirname(__file__), "src"))

# Utility function to read the README, etc..
# Used for the long_description and other fields.
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        contents = f.read()
    return contents

__version__ ,= re.findall('__version__ = "(.*)"', read("src/rostypes/__init__.py"))

requirements = [r for r in read("requirements.txt").splitlines() if r]


setup(
    name             = "ros-type-tokens",
    version          = __version__,
    author           = u"André Santos",
    author_email     = "andre.f.santos@inesctec.pt",
    description      = "Type tokens for ROS types",
    long_description = read("README.md"),
    long_description_content_type = "text/markdown",
    license          = "MIT",
    keywords         = "ros types typing type-tokens",
    url              = "https://github.com/git-afsantos/ros-type-tokens",
    packages         = find_packages(SOURCE),
    package_dir      = {"": SOURCE},
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance"
    ],
    python_requires  = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires = requirements,
    extras_require   = {},
    zip_safe         = False
)
