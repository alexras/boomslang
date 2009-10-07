import pylab
from matplotlib import pyplot
from PlotInfo import *
from Bar import *
import sys

class ClusteredBars(PlotInfo):
    """
    A clustered bar chart consisting of multiple series of bars
    with the same X axis values.
    """
    def __init__(self):
        PlotInfo.__init__(self, "clustered bar")
        
        self.bars = []
        self.spacing = 0
        self.width = 0.8
        
    def add(self, bar):
        if not isinstance(bar, Bar):
            print >>sys.stderr, "Can only add Bars to a ClusteredBars"
            sys.exit(1)
        
        self.bars.append(bar)
    
    def getXLabelLocations(self):
        labelLocations = []
        numBars = len(self.bars)
        clusterWidth = numBars * self.width + self.spacing
        
        clusterMiddle = float(numBars * self.width) / 2.0
        
        for i in xrange(len(self.bars[0].xValues)):
            labelLocations.append(clusterWidth * i + clusterMiddle) 

        return labelLocations
    
    def draw(self, axis):
        if self.xTickLabels is not None:
            self.xTickLabelPoints = self.getXLabelLocations()
            if len(self.xTickLabelPoints) != len(self.xTickLabels):
                print >>sys.stderr, "Number of clustered bar labels doesn't match number of points"
                print >>sys.stderr, "Labels: %s" % (self.xTickLabels)
                print >>sys.stderr, "Points: %s" % (self.xTickLabelPoints)
                sys.exit(1)

            axis.set_xticks(self.xTickLabelPoints)
            axis.set_xticklabels(self.xTickLabels)

        numBars = len(self.bars)
        
        plotHandles = []
        plotLabels = []

        for i in xrange(numBars):
            bar = self.bars[i]
            
            xVals = [(x * (self.width * numBars + self.spacing)) \
                + (i * self.width) for x in bar.xValues]
            
            attrs = bar.getAttributes()

            currHandle = axis.bar(xVals, bar.yValues, **attrs)
            # Only give handle to first rectangle in bar
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)

        return [plotHandles, plotLabels]
