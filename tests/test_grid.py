#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase

class GridTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(GridTest,self).__init__(testCaseName)
        self.imageName = "grid.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))

        plot.add(line)
        plot.setXLabel("X Label")
        plot.setYLabel("Y Label")
        plot.setYLimits(0, 60)

        plot.grid = True

        plot.save(self.imageName)

ImageComparisonTestCase.register(GridTest)

if __name__ == "__main__":
    test = GridTest()
    test.constructImage()
