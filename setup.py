#!/usr/bin/python
#
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

setup(
    name = "bedserver",
    version = "0.0.12", # Update also in __init__ ; look into zest.releaser to avoid having two versions
    description = "A fast and simple bedfile server",
    long_description="Query your bed files via http with this bedfile server",
    author = "David Rio",
    author_email = "driodeiros@gmail.com",
    url = 'http://github.com/drio/bedserver',
    license = 'https://github.com/drio/bedserver/blob/master/LICENSE',
    packages= ['bedserver'],
    scripts=['bin/bedserver'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    platforms = 'Posix; MacOS X; Windows',
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Topic :: Internet',
    ],
    dependency_links = [],
    install_requires = ['pysam', 'tornado', 'flask'],
)
