import pylab
from matplotlib import pylab
from PlotInfo import *
from Bar import *
import sys
import traceback

class StackedBars(PlotInfo):
    """
    A stacked bar chart consisting of multiple series of bars with the
    same X axis values
    """

    def __init__(self):
        super(StackedBars,self).__init__("stacked bar")

        self.bars = []

        self.spacing = None
        """
        The spacing between stacks of bars
        """

        self.barWidth = None
        """
        The width of the bars in the stack
        """


    def _getWidth(self):
        numBars = len(self.bars)
        if self.barWidth is None or numBars == 0:
            return None
        else:
            return self.barWidth

    def _setWidth(self, width):
        print >>sys.stderr, ("The 'width' property of StackedBars is "
                             "deprecated. Set barWidth instead")
        self.barWidth = width

    width = property(_getWidth, _setWidth)

    def add(self, bar):
        """
        Add `bar` (a :class:`boomslang.Bar.Bar`) to the stack
        """

        if not isinstance(bar, Bar):
            print >>sys.stderr, "Can only add Bars to a StackedBars"
            sys.exit(1)

        self.bars.append(bar)

    def _preDraw(self):
        if len(self.bars) == 0:
            return

        # Pre-draw all bars in the stack before pre-drawing me
        for bar in self.bars:
            bar._preDraw()

        if self.barWidth is None:
            self.barWidth = self.bars[0].width

        # All bars should have the same width
        for bar in self.bars:
            bar.width = self.barWidth

        # If spacing is set, then ignore the individual bars' xValues.
        # Otherwise, treat each bar as a normal bar.
        if self.spacing:
            self.xValues = [i + i * self.spacing for i in
                            xrange(len(self.bars[0].xValues))]
        else:
            self.xValues = self.bars[0].xValues
        self.yValues = xrange(len(self.xValues))

        self.xLimits = (min(self.xValues) - self.barWidth / 2.0,
                        max(self.xValues) + self.barWidth / 2.0)

        if not self.xTickLabels:
            self.xTickLabels = self.bars[0].xTickLabels
        if not self.xTickLabelPoints:
            self.xTickLabelPoints = self.bars[0].xTickLabelPoints
        if len(self.xTickLabelProperties) == 0:
            self.xTickLabelProperties = self.bars[0].xTickLabelProperties

    def draw(self, fig, axis, transform=None):
        if len(self.bars) == 0:
            return [[], []]

        super(StackedBars, self).draw(fig, axis)
        return self._draw(fig, axis, transform)

    def _draw(self, fig, axis, transform=None):
        if transform:
            self.xValues = [transform.transform((x,0))[0] for x in self.xValues]

        plotHandles = []
        plotLabels = []
        bottoms = [0 for i in xrange(len(self.xValues))]
        for bar in self.bars:
            attrs = bar.getAttributes()
            attrs['width'] = self.barWidth
            currHandle = axis.bar(
                self.xValues, bar.yValues, bottom=bottoms, **attrs)
            bottoms = [bar.yValues[i] + bottoms[i]
                       for i in xrange(len(self.xValues))]
            plotHandles.append(currHandle[0])
            plotLabels.append(bar.label)
        plotHandles.reverse()
        plotLabels.reverse()
        return [plotHandles, plotLabels]
