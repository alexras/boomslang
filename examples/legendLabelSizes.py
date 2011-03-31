#!/usr/bin/env python

from boomslang import Line, Plot, PlotLayout
from ImageComparisonTestCase import ImageComparisonTestCase

class LegendLabelSizesTest(ImageComparisonTestCase):
    def __init__(self):
        super(LegendLabelSizesTest,self).__init__("legendLabelSizes.png")

    def constructImage(self):

        line = Line()
        line.xValues = range(5)
        line.yValues = [2,3,5,7,9]
        line.label = "A Line"

        linePlot1 = Plot()
        linePlot1.setTitle("Small Legend")
        linePlot1.add(line)
        linePlot1.hasLegend()
        linePlot1.setLegendLabelSize(10)

        linePlot2 = Plot()
        linePlot2.setTitle("Large Legend")
        linePlot2.add(line)
        linePlot2.hasLegend()
        linePlot2.setLegendLabelSize(30)

        linePlot3 = Plot()
        linePlot3.setTitle("Inherited from Layout")
        linePlot3.add(line)
        linePlot3.hasLegend()

        layout = PlotLayout()
        layout.setWidth(2)
        layout.addPlot(linePlot1)
        layout.addPlot(linePlot2)
        layout.addPlot(linePlot3)
        layout.setLegendLabelSize(15)
        layout.setPlotParameters(left=0.03, bottom=0.03, right=0.98, top=0.94)

        layout.save(self.imageName)

ImageComparisonTestCase.register(LegendLabelSizesTest)

if __name__ == "__main__":
    test = LegendLabelSizesTest()

    test.constructImage()
