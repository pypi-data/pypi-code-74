from pathlib import Path

from setuptools import (find_packages,
                        setup)

import locus

project_base_url = 'https://github.com/lycantropos/locus/'

setup(name=locus.__name__,
      packages=find_packages(exclude=('tests', 'tests.*')),
      version=locus.__version__,
      description=locus.__doc__,
      long_description=Path('README.md').read_text(encoding='utf-8'),
      long_description_content_type='text/markdown',
      author='Azat Ibrakov',
      author_email='azatibrakov@gmail.com',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      license='MIT License',
      url=project_base_url,
      download_url=project_base_url + 'archive/master.zip',
      python_requires='>=3.5',
      install_requires=Path('requirements.txt').read_text(encoding='utf-8'))
