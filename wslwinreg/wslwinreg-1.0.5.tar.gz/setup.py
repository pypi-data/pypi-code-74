#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build the egg file for wslwinreg for python

setup.py clean
setup.py sdist bdist_wheel
twine upload --verbose dist/*

Copyright 2020-2021 by Rebecca Ann Heineman becky@burgerbecky.com

It is released under an MIT Open Source license. Please see LICENSE
for license details. Yes, you can use it in a
commercial title without paying anything, just give me a credit.
Please? It's not like I'm asking you for money!

"""

from __future__ import absolute_import, print_function
import io
import os
import sys
import setuptools

# pylint: disable=import-outside-toplevel

CWD = os.path.dirname(os.path.abspath(__file__))

# Project specific strings
PROJECT_NAME = 'wslwinreg'
PROJECT_KEYWORDS = [
    'cygwin',
    'msys2',
    'wsl',
    'winreg',
    'development',
    'windows',
    'visual studio',
    'vs',
    'burger'
]

# Manually import the project
PROJECT_MODULE = __import__(PROJECT_NAME)

# Read me file is the long description
with io.open(os.path.join(CWD, 'README.rst'), encoding='utf-8') as filep:
    LONG_DESCRIPTION = filep.read()

# Create the dependency list
INSTALL_REQUIRES = [
    'setuptools >= 17.1',
    'enum34 >= 1.0.0'
]

# Project classifiers
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
]

# Extra files to include in the form of this tuple (directory,[files])
DATA_FILES = [
    # (PROJECT_NAME, ['LICENSE.txt'])
]

#
# Parms for setup
#

SETUP_ARGS = dict(
    name='wslwinreg',
    version=PROJECT_MODULE.__version__,

    # Use the readme as the long description
    description=PROJECT_MODULE.__summary__,
    long_description=LONG_DESCRIPTION,
    # long_description_content_type='text/x-rst; charset=UTF-8',
    license=PROJECT_MODULE.__license__,
    url=PROJECT_MODULE.__uri__,

    author=PROJECT_MODULE.__author__,
    author_email=PROJECT_MODULE.__email__,

    keywords=PROJECT_KEYWORDS,
    platforms=['Any'],
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',

    classifiers=CLASSIFIERS,
    packages=[PROJECT_NAME],
    include_package_data=True,
    data_files=DATA_FILES,
    package_data={
        PROJECT_NAME: ['bin/*.exe']
    }
)

########################################

CLEAN_DIR_LIST = [
    PROJECT_NAME + '.egg-info',
    PROJECT_NAME + '-' + PROJECT_MODULE.__version__,
    'dist',
    'build',
    'temp',
    '.pytest_cache',
    '.tox',
    '.vscode'
]

CLEAN_DIR_RECURSE_LIST = [
    'temp',
    '__pycache__',
    '_build',
    'bin',
    '.vs'
]

CLEAN_EXTENSION_LIST = [
    '*.pyc',
    '*.pyo',
    '*.user'
]


def clean(working_dir):
    """
    Clean up all the temp files after uploading

    Helps in keeping source control from having to track
    temp files
    """

    # Delete all folders, including read only files
    try:
        from burger import delete_directory, clean_directories, clean_files
    except ImportError as exc:
        print("Install python module burger with pip to run clean")
        raise exc

    for item in CLEAN_DIR_LIST:
        delete_directory(os.path.join(working_dir, item))

    clean_directories(
        working_dir,
        CLEAN_DIR_RECURSE_LIST,
        recursive=True)

    #
    # Delete all *.pyc and *.pyo files
    #

    clean_files(
        working_dir,
        name_list=CLEAN_EXTENSION_LIST,
        recursive=True)

#
# Perform the setup
#


if __name__ == '__main__':
    # Ensure the directory is the current one
    if CWD:
        os.chdir(CWD)

    # Perform a thorough cleaning job
    if 'clean' in sys.argv:
        clean(CWD)

    # Unlock the files to handle Perforce locking
    try:
        from burger import unlock_files, lock_files
    except ImportError:
        def lock_files(not_used):
            """ Stub """
            return not_used

        def unlock_files(not_used):
            """ Stub """
            return not_used

    LOCK_LIST = unlock_files(CWD) + \
        unlock_files(os.path.join(CWD, PROJECT_NAME))
    try:
        setuptools.setup(**SETUP_ARGS)

    # If any files were unlocked, relock them
    finally:
        lock_files(LOCK_LIST)
