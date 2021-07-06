citationhelper
==============

This is a utility that generates a list of all packages imported into python scripts (\*.py) in a given list of directories.  It is intended to be used to help keep track of community software used in research projects so that the packages can be properly cited in publications.  The utility works by first walking the named directories and identifying \*.py files, then searching these files for import statements.

Installation
************

citationhelper can be installed via pip

    pip install citationhelper

Alternatively, citationhelper can be installed from github

    pip install git+https://github.com/EarthCubeInGeo/citationhelper.git

After installing, set the environment variable CITEHELP_REFFILE if you want to use a custom JSON library of full citations.  The utility will work without this, but it can only generate a list of package names with no citation information.

    export CITEHELP_REFFILE=filename

Usage
*****
Run citationhelper with the `citehelp` command followed by a list of the directories to search for import statements and print a report to the screen.

    citehelp project_directory


**WARNING**: This tool was developed to assist researchers in keeping track of software packages, but it is HIGHLY recommended users review the list of packages produced.
