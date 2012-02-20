#!/usr/bin/env python

import unittest
from boomslang.Utils import _check_min_version

class UtilsTest(unittest.TestCase):
    def test_min_version(self):
        self._test_ok_version((0, 2), (0, 1))
        self._test_ok_version((0, 2), (0, 1, 5))
        self._test_ok_version((0, 2, 3), (0, 1))
        self._test_ok_version((0, 1), (0, 1))
        self._test_bad_version((0, 9, 8), (1, 0))
        self._test_bad_version((0, 9, 8), (1,))
        self._test_ok_version([1, 2, 0], (0, 98, 0))
        self._test_ok_version((1, 0), (0, 9, 8))

    def _test_ok_version(self, version, min_version):
        self.assertTrue(_check_min_version(version, min_version),
                        "%s should meet min version requirements for %s" %
                        (version, min_version))

    def _test_bad_version(self, version, min_version):
        self.assertFalse(_check_min_version(version, min_version),
                         "%s should not meet min version requirements for %s" %
                         (version, min_version))

if __name__ == "__main__":
    unittest.main()
