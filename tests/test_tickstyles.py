#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class TickStylesTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(TickStylesTest, self).__init__(testCaseName)
        self.imageName = "tickstyles.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))
        line.xTickLabels = ["X 1", "X 2", "X 3", "X 4", "X 5"]
        line.yTickLabels = ["Y Ten", "Y Twenty", "Y Thirty", "Y Forty",
                            "Y Fifty", "Y Sixty"]
        line.yTickLabelPoints = [10, 20, 30, 40, 50, 60]
        line.setXTickLabelProperties(color="blue", weight="bold", rotation="45")
        line.setYTickLabelProperties(style="italic", alpha=0.5, color="red")
        plot.add(line)
        plot.setTitle("Craaazy Title")
        plot.setTitleProperties(style="italic", weight="bold", rotation="5",
                                color="orange")
        plot.setXLabel("X Label")
        plot.setYLabel("Y Label")
        plot.setYLimits(0, 60)

        plot.setPlotParameters(bottom=.15, left=0.15)

        plot.save(self.imageName)

ImageComparisonTestCase.register(TickStylesTest)

if __name__ == "__main__":
    test = TickStylesTest()

    test.constructImage()
