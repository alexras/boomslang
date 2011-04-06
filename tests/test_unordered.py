#!/usr/bin/env python

from boomslang import Plot, Line
from ImageComparisonTestCase import ImageComparisonTestCase

class UnorderedTest(ImageComparisonTestCase):
    def __init__(self, testCaseName):
        super(UnorderedTest, self).__init__("unordered.png")

    def constructImage(self):
        line = Line()
        line.xValues = [2, 1, 3, 4, 0]
        line.yValues = [2, 1, 3, 4, 0]

        plot = Plot()
        plot.add(line)

        plot.save(self.imageName)

ImageComparisonTestCase.register(UnorderedTest)

if __name__ == "__main__":
    test = UnorderedTest()

    test.constructImage()
