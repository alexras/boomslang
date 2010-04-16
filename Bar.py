import pylab
from matplotlib import pyplot
from PlotInfo import *

class Bar(PlotInfo):
    """
    A bar chart consisting of a single series of bars.
    """

    def __init__(self):
        PlotInfo.__init__(self, "bar")
        self.width=0.8
        self.color="black"
        self.edgeColor=None
        self.hatch=None
        self.align="center"
    
    def draw(self, axis, transform=None):
        if self.xTickLabelPoints is None:
            self.xTickLabelPoints = self.xValues
            
            if self.xTickLabels is None:
                self.xTickLabels = self.xValues

        PlotInfo.draw(self, axis)

        return self._draw(axis, transform)

    def _draw(self, axis, transform=None):
        kwdict = self.getAttributes()

        if transform:
            xValues = [transform.transform((x,0))[0] for x in self.xValues]
        else:
            xValues = self.xValues

        return [[axis.bar(xValues, self.yValues, **kwdict)[0]],
                [self.label]]

    def getAttributes(self):
        kwdict = {}
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["width"] = self.width
        kwdict["align"] = self.align

        if self.hatch is not None:
            kwdict["hatch"] = self.hatch
            print >>sys.stderr, "WARNING: Setting hash for bar charts only seems to work when exporting to svg or png"

        if self.edgeColor is not None:
            kwdict["edgecolor"] = self.edgeColor

        return kwdict
