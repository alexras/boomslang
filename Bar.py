import pylab
from matplotlib import pyplot
from PlotInfo import *
from boomslang.Label import Label

class Bar(PlotInfo):
    """
    A bar chart consisting of a single series of bars.
    """

    def __init__(self,
                 xValues=None,
                 yValues=None,
                 label=None,
                 labelBars=False,
                 width=0.8,
                 color="black",
                 edgeColor=None,
                 hatch=None,
                 align="center",
                ):
        super(Bar,self).__init__("bar")

        self.xValues = xValues
        self.yValues = yValues

        self.label = label
        self.labelBars = labelBars

        self.width = width
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
        kwdict["align"] = self.align

        if self.hatch is not None:
            kwdict["hatch"] = self.hatch
            print >>sys.stderr, "WARNING: Setting hash for bar charts only seems to work when exporting to svg, png, or pdf"

        if self.edgeColor is not None:
            kwdict["edgecolor"] = self.edgeColor

        return kwdict
