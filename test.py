import os
import unittest2
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    suite = unittest2.defaultTestLoader.discover(
        os.path.join(os.path.dirname(__file__), "tests"))
    unittest2.TextTestRunner().run(suite)

