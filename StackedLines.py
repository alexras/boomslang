import pylab
from matplotlib import pyplot
from PlotInfo import *
from Line import *
import sys

class StackedLines(PlotInfo):
    """
    Lines stacked one atop the other, with colors filling in the gaps
    """

    def __init__(self):
        PlotInfo.__init__(self, "stacked lines")

        self.lines = []
        self.colors = []
    
    def addLine(self, line, color="white"):
        self.lines.append(line)
        self.colors.append(color)

    def draw(self, axis, transform=None):
        PlotInfo.draw(self, axis)
        
        plotHandles = []
        plotLabels = []
        
        xValues = None
        yValues = []
        
        for line in self.lines:
            if xValues == None:
                xValues = line.xValues
            yValues.append(line.yValues)
        
        yDataStacked = self._cumulativeSum(yValues)
        
        plotHandles.append(axis.fill_between(xValues, 0, yDataStacked[0], 
                                             facecolor=self.colors[0]))
        for i in xrange(len(yDataStacked) - 1):
            handle = axis.fill_between(xValues, yDataStacked[i], 
                                       yDataStacked[i + 1], 
                                       facecolor=self.colors[i + 1])
            plotHandles.append(handle)
            plotLabels.append(self.lines[i].label)
        return [plotHandles, plotLabels]
    
    def _cumulativeSum(self, yValuesLists):
        output = []

        for i in xrange(len(yValuesLists)):
            currentList = yValuesLists[i]

            if i == 0:
                output.append(currentList)
                continue
            else:
                prevList = output[i-1]
                newList = [currentList[i] + prevList[i] for i in xrange(len(currentList))]
                output.append(newList)
        return output    
