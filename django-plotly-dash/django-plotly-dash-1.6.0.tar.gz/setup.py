#!/usr/bin/env python

from setuptools import setup

#import django_plotly_dash as dpd
#VERSION = dpd.__version__

with open('django_plotly_dash/version.py') as f:
    exec(f.read())

with open('README.md') as f:
    long_description = f.read()

setup(
    name="django-plotly-dash",
    version=__version__,
    url="https://github.com/GibbsConsulting/django-plotly-dash",
    description="Django use of plotly dash apps through template tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mark Gibbs",
    author_email="django_plotly_dash@gibbsconsulting.ca",
    license='MIT',
    packages=[
    'django_plotly_dash',
    'django_plotly_dash.migrations',
    'django_plotly_dash.templatetags',
    ],
    include_package_data=True,
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Framework :: Dash',
    ],
    keywords='django plotly plotly-dash dash dashboard',
    project_urls = {
    'Source': "https://github.com/GibbsConsulting/django-plotly-dash",
    'Tracker': "https://github.com/GibbsConsulting/django-plotly-dash/issues",
    'Documentation': 'http://django-plotly-dash.readthedocs.io/',
    },
    install_requires = ['plotly',
                        'dash>=1.11',
                        'dash-core-components',
                        'dash-html-components',
                        'dash-renderer',
                        'dpd-components',
                        'Django>=2.2',
                        'Flask>=1.0.2'],
    python_requires=">=3.6",
    )

