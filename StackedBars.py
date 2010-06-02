import pylab
from matplotlib import pylab
from PlotInfo import *
from Bar import *
import sys

class StackedBars(PlotInfo):
    """
    A stacked bar chart consisting of multiple series of bars with the 
    same X axis values
    """
    
    def __init__(self):
        PlotInfo.__init__(self, "stacked bar")
        
        self.bars = []
        self.spacing = 0
        self.width = 0.8
        
    def add(self, bar):
        if not isinstance(bar, Bar):
            print >>sys.stderr, "Can only add Bars to a StackedBars"
            sys.exit(1)
        
        if len(self.bars) == 0:
            # Fake having xValues
            self.xValues = bar.xValues
            self.yValues = bar.yValues
        bar.width = self.width
        self.bars.append(bar)

    def getXLabelLocations(self):
        if len(self.bars) == 0:
            return []
        else:
            numBarVals = len(self.bars[0].xValues)
            return range(numBarVals)

    def draw(self, axis, transform=None):
        self.xTickLabelPoints = self.getXLabelLocations()
        
        PlotInfo.draw(self, axis)

        return self._draw(axis, transform)

    def _draw(self, axis, transform=None):
        self.xTickLabelPoints = self.getXLabelLocations()

        plotHandles = []
        plotLabels = []

        if len(self.bars) == 0:
            return [plotHandles, plotLabels]

        numBars = len(self.bars)
        
        bottoms = [0 for i in xrange(len(self.xTickLabelPoints))]
        
        xVals = [i + i * self.spacing \
                     for i in xrange(len(self.bars[0].xValues))]

        if transform:
            xVals = [transform.transform((x,0))[0] for x in xVals]

        for bar in self.bars:
            attrs = bar.getAttributes()
            attrs['width'] = self.width

            currHandle = axis.bar(xVals, bar.yValues, bottom=bottoms, **attrs)
            
            bottoms = [bar.yValues[i] + bottoms[i] \
                           for i in xrange(len(self.xTickLabelPoints))]
            
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)

        plotHandles.reverse()
        plotLabels.reverse()
        return [plotHandles, plotLabels]
