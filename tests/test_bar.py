#!/usr/bin/env python

from boomslang import Bar, Plot
import unittest
from ImageComparisonTestCase import ImageComparisonTestCase

class BarTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(BarTest,self).__init__(testCaseName)
        self.imageName = "bar.png"

    def constructImage(self):
        plot = Plot()

        bar = Bar()
        bar.xValues = range(5)
        bar.yValues = [2, 8, 4, 6, 5]

        plot.add(bar)
        plot.setXLabel("Widget ID")
        plot.setYLabel("# Widgets Sold")

        plot.save(self.imageName)

ImageComparisonTestCase.register(BarTest)

if __name__ == "__main__":
    test = BarTest("testImageComparison")

    test.constructImage()
