#!/usr/bin/env python

from boomslang import Line, Plot
from numpy import arange, pi
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class ProjectionTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(ProjectionTest, self).__init__(testCaseName)
        self.imageName = "projection.png"

    def constructImage(self):
        plot = Plot()
        plot.projection = 'polar'

        r = arange(0,1,0.001)
        theta = 2*2*pi*r

        line = Line()
        line.xValues = theta
        line.yValues = r
        plot.add(line)
        plot.save(self.imageName)

ImageComparisonTestCase.register(ProjectionTest)

if __name__ == "__main__":
    test = ProjectionTest("testImageComparison")
    test.constructImage()
