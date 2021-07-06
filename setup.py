#!/usr/bin/env python
"""
citationhelper is a utility that creates a list of all python
  packages that have been imported in *.py scripts in given
  directories.  These packages should be cited in publications.
The full license can be found in LICENSE.txt
"""

import os
import sys
import subprocess
from setuptools import find_packages, setup

# # Get the package requirements
# REQSFILE = os.path.join(os.path.dirname(__file__), 'requirements.txt')
# with open(REQSFILE, 'r') as f:
#     REQUIREMENTS = f.readlines()
# REQUIREMENTS = '\n'.join(REQUIREMENTS)
REQUIREMENTS = ''

# # Do some nice things to help users install on conda.
# if sys.version_info[:2] < (3, 0):
#     EXCEPTION = OSError
# else:
#     EXCEPTION = subprocess.builtins.FileNotFoundError
# try:
#     subprocess.call(['conda', 'install', ' '.join(REQUIREMENTS)])
#     REQUIREMENTS = []
# except EXCEPTION:
#     pass
#
# Get the readme text
README = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(README, 'r') as f:
    READMETXT = f.readlines()
READMETXT = '\n'.join(READMETXT)

# Package description
DESC = "Tool for determining packages used in a particular project that should be cited."

#############################################################################
# First, check to make sure we are executing
# 'python setup.py install' from the same directory
# as setup.py (root directory)
#############################################################################
PATH = os.getcwd()
assert('setup.py' in os.listdir(PATH)), \
       "You must execute 'python setup.py install' from within the \
repo root directory."


#############################################################################
# Now execute the setup
#############################################################################
setup(name='citationhelper',
      install_requires=REQUIREMENTS,
      setup_requires=REQUIREMENTS,
      version="0.4",
      description=DESC,
      author="InGeO",
      author_email="ingeo-team@ingeo.datatransport.org",
      url="",
      download_url="",
      packages=find_packages(),
      long_description=READMETXT,
      zip_safe=False,
      py_modules=['citationhelper'],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Topic :: Scientific/Engineering",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License (GPL)",
                   "Natural Language :: English",
                   "Programming Language :: Python",
                  ],
      entry_points={
          'console_scripts': [
              'citehelp=citationhelper.citationhelper:main',
        ],
}
      )
