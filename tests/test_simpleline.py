#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class SimpleLineTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(SimpleLineTest,self).__init__(testCaseName)
        self.imageName = "simpleline.png"

    def constructImage(self):
        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))

        plot = Plot()
        plot.add(line)
        plot.xLabel = "X Label"
        plot.yLabel = "Y Label"
        plot.yLimits = (0, 60)
        plot.save(self.imageName)

ImageComparisonTestCase.register(SimpleLineTest)

if __name__ == "__main__":
    test = SimpleLineTest("testImageComparison")
    test.constructImage()
