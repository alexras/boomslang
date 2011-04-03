#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase

class LineStylesTest(ImageComparisonTestCase):
    def __init__(self):
        super(LineStylesTest, self).__init__("linestyles.png")

    def constructImage(self):
        plot = Plot()

        for i in xrange(24):
            line = Line()
            line.xValues = xrange(5)
            line.yValues = [(i+1) * x for x in line.xValues]
            line.label = "Line %d" % (i + 1)
            plot.add(line)

        plot.addLineColor("red")
        plot.addLineColor("blue")
        plot.addLineStyle("-")
        plot.addLineStyle("dashed")
        plot.addLineStyle("dotted")
        plot.addMarker('none')
        plot.addMarker('x')
        plot.addMarker('o')
        plot.hasLegend(columns=2)
        plot.setLegendLabelSize(8)
        plot.save(self.imageName)

ImageComparisonTestCase.register(LineStylesTest)

if __name__ == "__main__":
    test = LineStylesTest()

    test.constructImage()
