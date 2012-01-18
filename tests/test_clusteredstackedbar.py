#!/usr/bin/env python
from boomslang import ClusteredBars, StackedBars, Bar, Plot
from random import uniform
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class ClusteredStackedBarTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(ClusteredStackedBarTest,self).__init__(testCaseName)
        self.imageName = "clusteredstackedbar.png"

    def constructImage(self):
        cluster = ClusteredBars()

        colors = ['red','green','blue','CornflowerBlue','LightSalmon']

        yVals = [[
            [1, 3, 2, 5, 4],
            [2, 2, 2, 2, 2],
            [1, 3, 2, 4, 3],
            [0, 4, 0, 4, 0],
            [5, 5, 5, 5, 5]
        ],[
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2]
        ],
        [
            [1, 3, 1, 3, 1],
            [1, 3, 1, 3, 1],
            [1, 3, 1, 3, 1],
            [1, 3, 1, 3, 1],
            [1, 3, 1, 3, 1],
        ]]

        for i in xrange(3):
            stack = StackedBars()

            for j in xrange(5):
                bar = Bar()
                bar.xValues = range(5)
                bar.yValues = yVals[i][j]
                bar.color = colors[j]
                bar.label = "Subject %d" % (j+1,)

                stack.add(bar)
            cluster.add(stack)

        cluster.spacing = 0.5
        cluster.xTickLabels = ["1", "2", "3", "4", "5"]

        plot = Plot()
        plot.add(cluster)
        plot.hasLegend()
        plot.setXLabel('Nested Cars')
        plot.setYLabel('Party (lampshades)')
        plot.save(self.imageName)

ImageComparisonTestCase.register(ClusteredStackedBarTest)

if __name__ == "__main__":
    test = ClusteredStackedBarTest("testImageComparison")
    test.constructImage()
