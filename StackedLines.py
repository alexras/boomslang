import pylab
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from PlotInfo import *
from Line import *
import sys

class StackedLines(PlotInfo):
    """
    Lines stacked one atop the other, with colors filling in the gaps
    """

    def __init__(self):
        super(StackedLines,self).__init__("stacked lines")

        self.lines = []
        self.colors = []

    def addLine(self, line, color="white"):
        """
        Add `line` (a :class:`boomslang.Line.Line`) to the stack of lines,
        coloring the gap between it and the previous line with `color`
        """

        self.lines.append(line)
        self.colors.append(color)

    def draw(self, fig, axis, transform=None):
        super(StackedLines, self).draw(fig, axis)

        plotHandles = []
        plotLabels = []

        xValues = None
        yValues = []

        for line in self.lines:
            if xValues == None:
                xValues = line.xValues
            yValues.append(line.yValues)

        yDataStacked = self._cumulativeSum(yValues)

        axis.fill_between(xValues, 0, yDataStacked[0],
                          facecolor=self.colors[0],
                          linestyle=self.lines[0].lineStyle,
                          linewidth=self.lines[0].lineWidth)
        # Since fill_between doesn't have legend support, will have to create a
        # proxy artist for it. See
        # http://matplotlib.sourceforge.net/users/legend_guide.html#using-proxy-artist

        proxyArtist = Rectangle((0,0), 1, 1, color=self.colors[0])
        plotHandles.append(proxyArtist)
        plotLabels.append(self.lines[0].label)

        for i in xrange(len(yDataStacked) - 1):
            axis.fill_between(xValues, yDataStacked[i],
                              yDataStacked[i + 1],
                              facecolor=self.colors[i + 1],
                              linestyle=self.lines[i+1].lineStyle,
                              linewidth=self.lines[i+1].lineWidth)
            proxyArtist = Rectangle((0,0), 1, 1, color=self.colors[i+1])
            plotHandles.append(proxyArtist)
            plotLabels.append(self.lines[i+1].label)
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
                newList = [currentList[i] + prevList[i]
                           for i in xrange(len(currentList))]
                output.append(newList)
        return output
