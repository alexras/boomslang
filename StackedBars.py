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
        self.spacing = 0
        self.width = 0.8
        
    def add(self, bar):
        if not isinstance(bar, Bar):
            print >>sys.stderr, "Can only add Bars to a StackedBars"
            sys.exit(1)
                    
        bar.width = self.width
        self.bars.append(bar)

    def draw(self, axis, transform=None):
        if len(self.bars) == 0:
            return [[], []]
        
        self.xValues = [i + i * self.spacing for i in 
                        xrange(len(self.bars[0].xValues))]
        if transform:
            self.xValues = [transform.transform((x,0))[0] for x in self.xValues]
        
        self.yValues = self.bars[0].yValues
        
        # If the StackedBars doesn't have X label properties set, set them to
        # the value of the first bar.
        
        if not self.xTickLabels:
            self.xTickLabels = self.bars[0].xTickLabels
            
        if not self.xTickLabelPoints:
            self.xTickLabelPoints = self.bars[0].xTickLabelPoints
        
        if len(self.xTickLabelProperties) == 0:
            self.xTickLabelProperties = self.bars[0].xTickLabelProperties
            
        super(StackedBars, self).draw(axis)
        
        return self._draw(axis, transform)
    
    def _draw(self, axis, transform=None):        
        plotHandles = []
        plotLabels = []
        
        bottoms = [0 for i in xrange(len(self.xValues))]
        
        for bar in self.bars:
            attrs = bar.getAttributes()
            attrs['width'] = self.width
            
            currHandle = axis.bar(self.xValues, bar.yValues, bottom=bottoms, 
                                  **attrs)
            
            bottoms = [bar.yValues[i] + bottoms[i] 
                       for i in xrange(len(self.xValues))]
            
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)
        
        plotHandles.reverse()
        plotLabels.reverse()
        return [plotHandles, plotLabels]
