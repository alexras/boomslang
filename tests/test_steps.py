#!/usr/bin/env python
from boomslang import Line, Plot, PlotLayout
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class StepsTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(StepsTest, self).__init__(testCaseName)
        self.imageName = "steps.png"

    def constructImage(self):
        xVals = [1, 2, 3, 4, 5]
        yVals = [1, 2, 3, 4, 5]

        def generatePlot(stepType):
            line = Line()
            line.xValues = xVals
            line.yValues = yVals
            line.marker = 'o'
            line.stepFunction(stepType)

            plot = Plot()
            plot.add(line)
            plot.title = r'"%s" Steps' % (stepType)
            plot.xLimits = (0, 6)
            plot.yLimits = (0, 6)

            return plot

        prePlot = generatePlot("pre")
        midPlot = generatePlot("mid")
        postPlot = generatePlot("post")

        layout = PlotLayout()
        layout.width = 1
        layout.addPlot(prePlot)
        layout.addPlot(midPlot)
        layout.addPlot(postPlot)

        layout.save(self.imageName)


ImageComparisonTestCase.register(StepsTest)

if __name__ == "__main__":
    test = StepsTest("testImageComparison")

    test.constructImage()
