import pylab
from matplotlib import pyplot
from matplotlib.transforms import Affine2D, IdentityTransform
from PlotInfo import *
from Bar import *
from StackedBars import *
import sys
from boomslang_exceptions import BoomslangPlotConfigurationException

class ClusteredBars(PlotInfo):
    """
    A clustered bar chart consisting of multiple series of bars
    with the same X axis values.
    """

    def __init__(self):
        super(ClusteredBars,self).__init__("clustered bar")

        self.bars = []
        self.spacing = 0
        """
        The spacing between each bar in the cluster
        """

        self.background_color = "white"

        self.barWidth = None
        """
        The width of each bar in the cluster
        """

    def _getWidth(self):
        numBars = len(self.bars)
        if self.barWidth is None or numBars == 0:
            return None
        else:
            return self.barWidth * numBars

    def _setWidth(self, width):
        raise BoomslangPlotConfigurationException(
            "It isn't semantically meaningful for a clustered bar graph "
            "to have width. Set barWidth instead")

    width = property(_getWidth, _setWidth)
    """
    The overall width of each cluster of bars
    """

    def add(self, bar):
        """
        Add `bar` (a :class:`boomslang.Bar.Bar`) to the cluster of bars
        """

        if not isinstance(bar, Bar) and not isinstance(bar, StackedBars):
            raise BoomslangPlotConfigurationException(
                "Can only add Bars to a ClusteredBars")

        self.bars.append(bar)

    def _labelTransform(self, x):
        return (x + 1) * (self.width / 2.0) + \
                x * (self.width / 2.0 + self.spacing) - \
                (self.barWidth / 2.0)

    def _preDraw(self):
        if len(self.bars) == 0:
            return

        for bar in self.bars:
            bar._preDraw()

        if self.barWidth is None:
            self.barWidth = self.bars[0].width

        # All bars should have the same width
        for bar in self.bars:
            if isinstance(bar, Bar):
                bar.width = self.barWidth

        if self.xTickLabels is not None:
            self.xTickLabelPoints = [self._labelTransform(x)
                                     for x in self.bars[0].xValues]

            if len(self.xTickLabelPoints) != len(self.xTickLabels):
                raise BoomslangPlotConfigurationException(
                "Number of clustered bar labels doesn't "
                "match number of points. Labels: %s, Points: %s" %
                (self.xTickLabels, self.xTickLabelPoints))

    def draw(self, fig, axis, transform=None):
        super(ClusteredBars,self).draw(fig, axis)

        rect = axis.patch
        rect.set_facecolor(self.background_color)

        return self._draw(fig, axis, transform)

    def _draw(self, fig, axis, transform=None):
        numBars = len(self.bars)

        plotHandles = []
        plotLabels = []

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

            [handles, labels] = bar._draw(fig, axis, transform=xform)
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

        if self.xTickLabels is not None:
            xMin = self.xTickLabelPoints[0]
            xMax = self.xTickLabelPoints[-1]
        else:
            xMin = self._labelTransform(self.bars[0].xValues[0])
            xMax = self._labelTransform(self.bars[0].xValues[-1])

        self.xLimits = (xMin - clusterWidth / 2.0, xMax + clusterWidth / 2.0)

        return [plotHandles, plotLabels]
