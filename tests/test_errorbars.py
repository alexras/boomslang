#!/usr/bin/env python

from boomslang import Line, Plot
import unittest
from ImageComparisonTestCase import ImageComparisonTestCase

class ErrorBarsTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(ErrorBarsTest,self).__init__(testCaseName)
        self.imageName = "errorbars.png"

    def constructImage(self):
        plot = Plot()

        # Uneven error bars
        line = Line()
        line.xValues = [6,10,4,0,8,2,12]
        line.yValues = [50,90,30,10,70,20,110]
        line.yMins   = [y - 30 for y in line.yValues]
        line.yMaxes  = [y + 50 for y in line.yValues]
        line.label = "Asymmetric Errors"
        line.color = "red"

        # Even error bars
        line2 = Line()
        line2.xValues = [1,5,3,9,7,11]
        line2.yValues = [100, 120, 110, 140, 130, 150]
        line2.color = "blue"
        line2.label = "Symmetric Errors"
        line2.yErrors = [5,25,15,45,35,55]

        plot.add(line)
        plot.add(line2)
        plot.xLabel = "X Label"
        plot.yLabel = "Y Label"
        plot.hasLegend()
        plot.xLimits = (-1, 13)
        plot.save(self.imageName)

ImageComparisonTestCase.register(ErrorBarsTest)

if __name__ == "__main__":
    test = ErrorBarsTest("testImageComparison")

    test.constructImage()
