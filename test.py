import unittest
import os

class TestExamples(unittest.TestCase):
    for example in filter(lambda x: x.endswith('py'), os.listdir('examples')):
        example_no_py = example[:-3]
        full_path = os.path.join('examples', example)
        exec("def test_%s(self):\n" % (example_no_py,) +
             "    res = os.system('python %s')\n" % (full_path,) +
             "    self.assertTrue(res == 0)")

if __name__ == '__main__':
    unittest.main()
