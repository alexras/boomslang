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
        super(StackedBars,self).__init__("stacked bar")
        
        self.bars = []
        self.width = 0.8
        
    def add(self, bar):
        if not isinstance(bar, Bar):
            print >>sys.stderr, "Can only add Bars to a StackedBars"
            sys.exit(1)
        #
        # If this is the first bar added, then use its settings.
        # FIXME: What if the first bar doesn't have these set?
        #
        if len(self.bars) == 0:
            if bar.xTickLabels:
                self.xTickLabels = bar.xTickLabels
            if bar.xTickLabelPoints:
                self.xTickLabelPoints = bar.xTickLabelPoints
            if bar.xTickLabelProperties:
                self.xTickLabelProperties = bar.xTickLabelProperties
            self.xValues = bar.xValues
            self.yValues = bar.yValues
        #
        # Each bar should have the same width.
        #
        bar.width = self.width
        self.bars.append(bar)

    def draw(self, axis, transform=None):
        super(StackedBars, self).draw(axis)
        return self._draw(axis, transform)

    def _draw(self, axis, transform=None):
        plotHandles = []
        plotLabels = []

        if len(self.bars) == 0:
            return [plotHandles, plotLabels]

        numBars = len(self.bars)
        
        bottoms = [0 for i in xrange(len(self.xValues))]
       
        #
        # What does this do?
        #
        #if transform:
        #    xVals = [transform.transform((x,0))[0] for x in xVals]

        for bar in self.bars:
            attrs = bar.getAttributes()
            attrs['width'] = self.width

            currHandle = axis.bar(bar.xValues, bar.yValues, bottom=bottoms, **attrs)
            
            bottoms = [bar.yValues[i] + bottoms[i] \
                           for i in xrange(len(self.xValues))]
            
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)

        plotHandles.reverse()
        plotLabels.reverse()
        return [plotHandles, plotLabels]
