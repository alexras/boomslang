import os
import unittest2
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    testLoader = unittest2.defaultTestLoader.discover(
        os.path.join(os.path.dirname(__file__), "examples"), pattern="test_*.py")

