#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest, math

class LargeLabelTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(LargeLabelTest, self).__init__(testCaseName)
        self.imageName = "largelabel.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.xValues = xrange(100)
        line.xTickLabels = ["Whoa this label is really long why is this label so long"]
        line.xTickLabelPoints = [42]
        line.xTickLabelProperties["rotation"] = 45
        line.yValues = [math.sin(x) for x in xrange(100)]
        line.yTickLabels = ["Look at this value. Pretty sweet value right?"]
        line.yTickLabelPoints = [0.3]

        plot.add(line)
        plot.setXLabel("Value")
        plot.setYLabel("sin(Value)")

        plot.save(self.imageName)

ImageComparisonTestCase.register(LargeLabelTest)

if __name__ == "__main__":
    test = LargeLabelTest("testImageComparison")

    test.constructImage()

