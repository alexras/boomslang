#!/usr/bin/env python

from boomslang import Bar, Plot
import unittest
from ImageComparisonTestCase import ImageComparisonTestCase

class HatchedBarsTest(ImageComparisonTestCase):
    def __init__(self, testCaseName):
        super(HatchedBarsTest, self).__init__(testCaseName)
        self.imageName = "hatchedbars.png"

    def constructImage(self):
        bar = Bar()

        bar.xValues = range(5)
        bar.yValues = [2, 4, 6, 8, 10]
        # Valid values include all marker types, /, //, \, \\
        bar.hatch = r"\\"
        bar.color="red"
        bar.edgeColor="black"

        plot = Plot()
        plot.add(bar)
        plot.save(self.imageName)

ImageComparisonTestCase.register(HatchedBarsTest)

if __name__ == "__main__":
    test = HatchedBarsTest()

    test.constructImage()
