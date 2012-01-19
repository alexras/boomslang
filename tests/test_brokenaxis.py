#!/usr/bin/env python

from boomslang import Bar, BrokenAxisPlot
import unittest
from ImageComparisonTestCase import ImageComparisonTestCase

class BrokenAxisTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(BrokenAxisTest,self).__init__(testCaseName)
        self.imageName = "brokenaxis.png"

    def constructImage(self):
        plot = BrokenAxisPlot(break_points=(4,8))

        bar = Bar()
        bar.xValues = range(5)
        bar.yValues = [2, 12, 3, 18.5, 13]

        plot.add(bar)
        plot.setXLabel("Widget ID")
        plot.setYLabel("# Widgets Sold")

        plot.save(self.imageName)

ImageComparisonTestCase.register(BrokenAxisTest)

if __name__ == "__main__":
    test = BrokenAxisTest("constructImage")

    test.constructImage()
