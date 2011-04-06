#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase

class TwinXTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(TwinXTest,self).__init__("twinx.png")

    def constructImage(self):
        line1 = Line()
        line1.xValues = range(7)
        line1.yValues = [1, 2, 4, 8, 16, 32, 64]
        line1.label = "First Plot"
        line1.lineStyle = "-"
        line1.color = "red"

        line2 = Line()
        line2.xValues = range(7)
        line2.yValues = [100, 90, 80, 70, 60, 50, 40]
        line2.label = "Second Plot"
        line2.lineStyle = "--"
        line2.color = "blue"

        plot = Plot()
        plot.add(line1)
        plot.add(line2)
        plot.setXLabel("Shared X Axis")
        plot.setYLabel("First Plot's Y Axis")
        plot.setTwinX("Second Plot's Y Axis", 1)
        plot.hasLegend()

        plot.save(self.imageName)

ImageComparisonTestCase.register(TwinXTest)

if __name__ == "__main__":
    test = TwinXTest()

    test.constructImage()
