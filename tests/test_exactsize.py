#!/usr/bin/env python

from boomslang import Line, Plot
import unittest
from PIL import Image
import os

class ExactSizeTest(unittest.TestCase):
    imageName = "exactsize.png"

    def __init__(self, testName):
        super(ExactSizeTest, self).__init__("testExactSize")

    def setUp(self):
        if os.path.exists(self.imageName):
            os.unlink(self.imageName)

    def tearDown(self):
        if os.path.exists(self.imageName):
            os.unlink(self.imageName)

    def testExactSize(self):
        plot = Plot()
        line = Line()
        plot.setDimensions(3, 4)

        line.xValues = range(5)
        line.yValues = range(5)

        plot.add(line)
        plot.save(self.imageName)

        im = Image.open(self.imageName)
        self.assertEqual(im.size, (300,400))

        plot.setDimensions(3,4,dpi=250)

        plot.save(self.imageName)
        im = Image.open(self.imageName)
        self.assertEqual(im.size, (750,1000))

if __name__ == "__main__":
    test = ExactSizeTest("testImageComparison")
    test.testExactSize()
