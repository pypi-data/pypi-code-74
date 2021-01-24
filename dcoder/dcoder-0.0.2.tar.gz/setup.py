from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='dcoder',
  version='0.0.2',
  description='A module that can decode/encode text in various ciphers.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Swas.py',
  author_email='cwswas.py@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='decoder,encoder,ciphers', 
  packages=find_packages(),
  install_requires=[''] 
)