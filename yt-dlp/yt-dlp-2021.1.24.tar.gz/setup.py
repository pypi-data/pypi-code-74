#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, Command, find_packages
import os.path
import warnings
import sys
from distutils.spawn import spawn

# Get the version from youtube_dlc/version.py without importing the package
exec(compile(open('youtube_dlc/version.py').read(),
             'youtube_dlc/version.py', 'exec'))

DESCRIPTION = 'Command-line program to download videos from YouTube.com and many other other video platforms.'

LONG_DESCRIPTION = '\n\n'.join((
    'Official repository: <https://github.com/pukkandan/yt-dlp>',
    '**PS**: Many links in this document will not work since this is a copy of the README.md from Github',
    open("README.md", "r", encoding="utf-8").read()))

if len(sys.argv) >= 2 and sys.argv[1] == 'py2exe':
    print("inv")
else:
    files_spec = [
        ('etc/bash_completion.d', ['youtube-dlc.bash-completion']),
        ('etc/fish/completions', ['youtube-dlc.fish']),
        ('share/doc/youtube_dlc', ['README.txt']),
        ('share/man/man1', ['youtube-dlc.1'])
    ]
    root = os.path.dirname(os.path.abspath(__file__))
    data_files = []
    for dirname, files in files_spec:
        resfiles = []
        for fn in files:
            if not os.path.exists(fn):
                warnings.warn('Skipping file %s since it is not present. Type  make  to build all automatically generated files.' % fn)
            else:
                resfiles.append(fn)
        data_files.append((dirname, resfiles))

    params = {
        'data_files': data_files,
    }
    #if setuptools_available:
    params['entry_points'] = {'console_scripts': ['youtube-dlc = youtube_dlc:main']}
    #else:
    #    params['scripts'] = ['bin/youtube-dlc']

class build_lazy_extractors(Command):
    description = 'Build the extractor lazy loading module'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        spawn(
            [sys.executable, 'devscripts/make_lazy_extractors.py', 'youtube_dlc/extractor/lazy_extractors.py'],
            dry_run=self.dry_run,
        )

setup(
    name="yt-dlp",
    version=__version__,
    maintainer="pukkandan",
    maintainer_email="pukkandan@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/pukkandan/yt-dlp",
    packages=find_packages(exclude=("youtube_dl","test",)),
    project_urls={
        'Documentation': 'https://github.com/pukkandan/yt-dlp#yt-dlp',
        'Source': 'https://github.com/pukkandan/yt-dlp',
        'Tracker': 'https://github.com/pukkandan/yt-dlp/issues',
        #'Funding': 'https://donate.pypi.org',
    },
    classifiers=[
	    "Topic :: Multimedia :: Video",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6',
	
	cmdclass={'build_lazy_extractors': build_lazy_extractors},
    **params
)
