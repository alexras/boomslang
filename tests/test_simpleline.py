#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase

class SimpleLineTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(SimpleLineTest,self).__init__(testCaseName)
        self.imageName = "simpleline.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))

        plot.add(line)
        plot.setXLabel("X Label")
        plot.setYLabel("Y Label")
        plot.setYLimits(0, 60)

        plot.save(self.imageName)

ImageComparisonTestCase.register(SimpleLineTest)

if __name__ == "__main__":
    test = SimpleLineTest()
    test.constructImage()
