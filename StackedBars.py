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
        
        self.bars.append(bar)

    def getXLabelLocations(self):
        if len(self.bars) == 0:
            return []
        else:
            numBarVals = len(self.bars[0].xValues)
            return [i + self.width / 2.0 for i in xrange(numBarVals)]

    def draw(self, axis):
        self.xTickLabelPoints = self.getXLabelLocations()
        axis.set_xticks(self.xTickLabelPoints)
        if self.xTickLabels is not None:
            axis.set_xticklabels(self.xTickLabels)
            
        plotHandles = []
        plotLabels = []

        if len(self.bars) == 0:
            return [plotHandles, plotLabels]

        numBars = len(self.bars)
        
        bottoms = [0 for i in xrange(len(self.xTickLabelPoints))]
        
        xVals = [i + i * self.spacing \
                     for i in xrange(len(self.bars[0].xValues))]

        for bar in self.bars:
            attrs = bar.getAttributes()
            currHandle = axis.bar(xVals, bar.yValues, bottom=bottoms, **attrs)
            
            bottoms = [bar.yValues[i] + bottoms[i] \
                           for i in xrange(len(self.xTickLabelPoints))]
            
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)
        return [plotHandles, plotLabels]
