import setuptools


setuptools.setup(
    name='TensorFlow El 8lbah', # Replace with your own username
    version="0.0.1",
    author='MinaZ',
    author_email='mwagdy64@gmail.com',
    description='DL FrameWork to train and test on mnist and cifar10',
    long_description_content_type="text/markdown",
    url='https://github.com/Mina93178/Deep_learning_frame_work',
    packages=setuptools.find_packages(),
    install_requires=[
      'numpy', 'texttable', 'matplotlib',
    ],
  ## dependancy_links=['https://pypi.org/project/matplotlib/', 'https://pypi.org/project/numpy/', 'https://pypi.org/project/texttable/'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',


    ],
      keywords='Deep_learning_frame_work ',
      python_requires='>=3.6',

)