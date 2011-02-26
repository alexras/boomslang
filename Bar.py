import pylab
from matplotlib import pyplot
from PlotInfo import *
from boomslang.Label import Label
import warnings

class Bar(PlotInfo):
    """
    A bar chart consisting of a single series of bars.
    """

    def __init__(self,
                 label=None,
                 labelBars=False,
                 width=0.8,
                 linewidth=1.0,
                 color="black",
                 edgeColor=None,
                 hatch=None,
                 align="center",
                 **kwargs
                ):
        super(Bar,self).__init__("bar", **kwargs)

        self.label = label
        self.labelBars = labelBars

        self.width = width
        self.linewidth = linewidth
        self.color = color
        self.edgeColor = edgeColor
        self.hatch = hatch
        self.align = align

    def draw(self, axis, transform=None):
        super(Bar,self).draw(axis)
        
        return self._draw(axis, transform)
    
    def _draw(self, axis, transform=None):
        kwdict = self.getAttributes()
        
        plotObjects = []
        labels = [self.label]
        
        if transform:
            xValues = [transform.transform((x,0))[0] for x in self.xValues]
        else:
            xValues = self.xValues
        
        plotObjects.append(axis.bar(xValues, self.yValues, **kwdict)[0])
        
        if self.labelBars:
            maxYValue = max(self.yValues)
            for i in xrange(len(self.yValues)):
                xVal = xValues[i]
                yVal = self.yValues[i]
                
                label = Label(xVal, yVal, "%d" % (yVal))
                label.setTextOffset(0, 0.05 * maxYValue)
                label.marker = 'x'
                (labelObjects, labelLabels) = label.draw(axis)
                plotObjects.extend(labelObjects)
                labels.extend(labelLabels)
        
        return [plotObjects, labels]

    def getAttributes(self):
        kwdict = {}
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["width"] = self.width
        kwdict["linewidth"] = self.linewidth
        kwdict["align"] = self.align

        if self.hatch is not None:
            kwdict["hatch"] = self.hatch
            warnings.warn("Setting hatch for bar charts only seems to work when exporting to svg, png, or pdf", Warning)

        if self.edgeColor is not None:
            kwdict["edgecolor"] = self.edgeColor

        return kwdict
