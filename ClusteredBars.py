import pylab
from matplotlib import pyplot
from matplotlib.transforms import Affine2D, IdentityTransform
from PlotInfo import *
from Bar import *
from StackedBars import *
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
        if not isinstance(bar, Bar) and not isinstance(bar, StackedBars):
            print >>sys.stderr, "Can only add Bars to a ClusteredBars"
            sys.exit(1)
        
        self.bars.append(bar)
    
    def getXLabelLocations(self):
        labelLocations = []
        clusterWidth = sum([bar.width for bar in self.bars])

        for x in self.bars[0].xValues:
            labelLocations.append((clusterWidth + self.spacing) * x +\
                                   clusterWidth / 2.0)

        return labelLocations
    
    def draw(self, axis, transform=None):
        if self.xTickLabels is not None:
            self.xTickLabelPoints = self.getXLabelLocations()
            if len(self.xTickLabelPoints) != len(self.xTickLabels):
                print >>sys.stderr, "Number of clustered bar labels doesn't match number of points"
                print >>sys.stderr, "Labels: %s" % (self.xTickLabels)
                print >>sys.stderr, "Points: %s" % (self.xTickLabelPoints)
                sys.exit(1)

        PlotInfo.draw(self, axis)

        return self._draw(axis, transform)
        

    def _draw(self, axis, transform=None):
        numBars = len(self.bars)
        
        plotHandles = []
        plotLabels = []
        
        xMin = None
        xMax = None

        clusterWidth = sum([bar.width for bar in self.bars])

        for i in xrange(numBars):
            bar = self.bars[i]

            pre_width = sum([self.bars[j].width for j in xrange(i)])

            bar_xform = Affine2D().scale(clusterWidth + self.spacing, 1)\
                                  .translate(pre_width, 0)

            if transform:
                xform = bar_xform + transform
            else:
                xform = bar_xform

            [handles, labels] = bar._draw(axis, transform=xform)
            bar.drawErrorBars(axis, transform=xform)

            if isinstance(bar, Bar):
                # Only give handle to first rectangle in bar
                plotHandles.append(handles[0])
                plotLabels.append(labels[0])
            else:
                # Assuming StackedBar
                if i == 0:
                    plotHandles.extend(handles)
                    plotLabels.extend(labels)

        scale_xform = Affine2D().scale(clusterWidth + self.spacing, 1)

        xMin = scale_xform.transform((self.bars[0].xValues[0], 0))[0] - \
                    self.bars[0].width / 2.0

        xMax = scale_xform.transform((self.bars[0].xValues[-1], 0))[0] + \
                    clusterWidth - self.bars[0].width / 2.0

        self.xLimits = (xMin, xMax)

        return [plotHandles, plotLabels]
