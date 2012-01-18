#!/usr/bin/env python

from boomslang import Plot, Line
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class UnorderedTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(UnorderedTest, self).__init__(testCaseName)
        self.imageName = "unordered.png"

    def constructImage(self):
        line = Line()
        line.xValues = [2, 1, 3, 4, 0]
        line.yValues = [2, 1, 3, 4, 0]

        plot = Plot()
        plot.add(line)

        plot.save(self.imageName)

ImageComparisonTestCase.register(UnorderedTest)

if __name__ == "__main__":
    test = UnorderedTest("testImageComparison")

    test.constructImage()
