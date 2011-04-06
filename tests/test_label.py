#!/usr/bin/env python

from boomslang import Label, Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import numpy
import unittest

class LabelTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(LabelTest, self).__init__(testCaseName)
        self.imageName = "label.png"

    def constructImage(self):
        line = Line()
        line.xValues = numpy.arange(0.0, 5.0, 0.01)
        line.yValues = numpy.cos(2 * numpy.pi * line.xValues)

        maxLabel = Label(2, 1, "Maximum!")
        maxLabel.setTextOffset(0.5, 0.5)
        maxLabel.hasArrow()

        minLabel = Label(1.5, -1, "Minimum!")
        minLabel.setTextPosition(1, -2)
        minLabel.hasArrow()

        randomLabel = Label(2, -1.7, "A Point!")
        randomLabel.setTextOffset(0, 0.2)
        randomLabel.marker = 'o'

        styledLabel = Label(1.25, 1.2, "A FancyPoint!",
                            bbox={'edgecolor':'red',
                                  'facecolor':'white',
                                  'ls':'dashed',
                                  'lw':'2'})
        styledLabel.setTextOffset(0, 0.2)
        styledLabel.marker = 'o'

        plot = Plot()
        plot.add(line)
        plot.add(minLabel)
        plot.add(maxLabel)
        plot.add(randomLabel)
        plot.add(styledLabel)
        plot.setYLimits(-3, 3)
        plot.setXLabel("X")
        plot.setYLabel("cos(x)")
        plot.save(self.imageName)

ImageComparisonTestCase.register(LabelTest)

if __name__ == "__main__":
    test = LabelTest()

    test.constructImage()
