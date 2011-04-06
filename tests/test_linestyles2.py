#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase

class LineStyles2Test(ImageComparisonTestCase):
    def __init__(self, testCaseName):
        super(LineStyles2Test, self).__init__("linestyles2.png")

    def constructImage(self):

        plot = Plot()

        for i in xrange(6):
            line = Line()
            line.xValues = xrange(5)
            line.yValues = [(i+1) * x for x in line.xValues]
            line.label = "Line %d" % (i + 1)
            plot.add(line)

        plot.addLineColor("red")
        plot.addLineColor("blue")
        plot.addLineColor("green")
        plot.addMarker('')
        plot.addMarker('x')
        plot.hasLegend(columns=2)
        plot.save(self.imageName)

ImageComparisonTestCase.register(LineStyles2Test)

if __name__ == "__main__":
    test = LineStyles2Test()

    test.constructImage()
