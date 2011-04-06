#!/usr/bin/env python

from boomslang import Line, Plot, PlotLayout

from ImageComparisonTestCase import ImageComparisonTestCase

class LogScaleTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(LogScaleTest,self).__init__(testCaseName)
        self.imageName = "logscale.png"

    def constructImage(self):
        layout = PlotLayout()

        plotBase10 = Plot()
        plotBase10.loglog = True

        lineBase10 = Line()
        lineBase10.marker = 'x'
        lineBase10.xValues = [1, 10, 100, 1000, 10000]
        lineBase10.yValues = [1, 25, 140, 1024, 10342]

        plotBase10.add(lineBase10)

        plotBase2 = Plot()
        plotBase2.logx = True
        plotBase2.logbase = 2

        lineBase2 = Line()
        lineBase2.marker = 'x'
        lineBase2.xValues = [1, 2, 4, 8, 16, 32, 64]
        lineBase2.yValues = [1, 2, 3, 4, 5, 6, 7]

        plotBase2.add(lineBase2)


        layout.addPlot(plotBase10)
        layout.addPlot(plotBase2)

        layout.width = 2
        layout.save(self.imageName)

ImageComparisonTestCase.register(LogScaleTest)

if __name__ == "__main__":
    test = LogScaleTest()

    test.constructImage()
