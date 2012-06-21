#!/usr/bin/env python

from boomslang import Line, Plot, PlotLayout
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class LegendLabelSizesTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(LegendLabelSizesTest,self).__init__(testCaseName)
        self.imageName = "legendLabelSizes.png"

    def constructImage(self):
        line = Line()
        line.xValues = range(5)
        line.yValues = [2,3,5,7,9]
        line.label = "A Line"

        linePlot1 = Plot()
        linePlot1.title = "Small Legend"
        linePlot1.add(line)
        linePlot1.hasLegend()
        linePlot1.legendLabelSize = 10

        linePlot2 = Plot()
        linePlot2.title = "Large Legend"
        linePlot2.add(line)
        linePlot2.hasLegend()
        linePlot2.legendLabelSize = 30

        linePlot3 = Plot()
        linePlot3.title = "Inherited from Layout"
        linePlot3.add(line)
        linePlot3.hasLegend()

        layout = PlotLayout()
        layout.width = 2
        layout.addPlot(linePlot1)
        layout.addPlot(linePlot2)
        layout.addPlot(linePlot3)
        layout.legendLabelSize = 15

        layout.save(self.imageName)

ImageComparisonTestCase.register(LegendLabelSizesTest)

if __name__ == "__main__":
    test = LegendLabelSizesTest("testImageComparison")

    test.constructImage()
