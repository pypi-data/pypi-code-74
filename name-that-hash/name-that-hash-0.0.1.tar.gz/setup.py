# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['name_that_hash']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'rich>=9.9.0,<10.0.0']

entry_points = \
{'console_scripts': ['nth = name_that_hash:runner']}

setup_kwargs = {
    'name': 'name-that-hash',
    'version': '0.0.1',
    'description': 'The Modern Hash Identifcation System',
    'long_description': None,
    'author': 'brandon',
    'author_email': 'brandon@skerritt.blog',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
