#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class FontSizesTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(FontSizesTest, self).__init__(testCaseName)
        self.imageName = "fontsizes.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))

        plot.add(line)
        plot.xLabel = "X Label"
        plot.yLabel = "Y Label"
        plot.yLimits = (0, 60)

        plot.xTickLabelSize = 24
        plot.yTickLabelSize = 36
        plot.axesLabelSize = 18
        plot.tight = True

        plot.save(self.imageName)

ImageComparisonTestCase.register(FontSizesTest)

if __name__ == "__main__":
    test = FontSizesTest("testImageComparison")

    test.constructImage()
