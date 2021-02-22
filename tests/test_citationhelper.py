# test.py

import pytest
import citationhelper.citationhelper as ch

def test_py():
    imports = ch.collect_imports(['tests/py_scripts'])
    expected_imports = ['copy', 'custom_scripts', 'datetime', 'gzip', 'my_functions', 'my_utils', 'numpy', 'os', 'scipy', 'sys']
    assert imports == expected_imports

def test_ipynb():
    imports = ch.collect_imports(['tests/ipynb_notebooks'])
    expected_imports = ['datetime', 'my_scripts', 'my_scripts2', 'numpy', 'os', 'scipy', 'sys']
    assert imports == expected_imports
