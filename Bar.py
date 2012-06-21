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
        """
        The width of each bar in the set of bars
        """
        self.linewidth = linewidth
        """
        The width of the line that borders each bar
        """

        self.color = color
        """
        The color of the bars
        """

        self.edgeColor = edgeColor
        """
        The color of the line that borders each bar
        """

        self.hatch = hatch
        """
        The style of hatching used within the bar, if any. Valid values are any
        marker type, ``/``, ``//``, ``\`` and ``\\``
        """

        self.align = align
        """
        If `center` (default), `xValues` values denote the center of each
        bar. If `edge`, `xValues` values denote the left edge of each bar.
        """

    def draw(self, fig, axis, transform=None):
        super(Bar,self).draw(fig, axis)

        return self._draw(fig, axis, transform)

    def _draw(self, fig, axis, transform=None):
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
                (labelObjects, labelLabels) = label.draw(fig, axis)
                plotObjects.extend(labelObjects)
                labels.extend(labelLabels)

        return [plotObjects, labels]

    def getAttributes(self):
        kwdict = super(Bar,self).getAttributes()

        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["width"] = self.width
        kwdict["linewidth"] = self.linewidth
        kwdict["align"] = self.align

        if self.hatch is not None:
            kwdict["hatch"] = self.hatch
            warnings.warn(
                "Setting hatch for bar charts only seems to work when "
                "exporting to svg, png, or pdf", Warning)

        if self.edgeColor is not None:
            kwdict["edgecolor"] = self.edgeColor

        return kwdict
