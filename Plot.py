import pylab
import sys
from PlotInfo import PlotInfo
from PlotLayout import *
import copy
from LabelProperties import LabelProperties
from Inset import Inset
from Marker import Marker
from LineStyle import LineStyle
from Grid import Grid
from boomslang_exceptions import BoomslangPlotConfigurationException
from boomslang_exceptions import BoomslangPlotRenderingException
from Legend import Legend

from Utils import getGoldenRatioDimensions, _check_min_matplotlib_version

class Plot(object):
    """
    Represents a single plot, usually consisting of a single X and Y axis.
    """

    def __init__(self):
        self.plots = []

        self.title = None
        """
        The plot's title (will be centered above the axes themselves)
        """

        self.xFormatter = None
        self.yFormatter = None

        self.yLabel = None
        """
        The label for the plot's y-axis
        """

        self.xLabel = None
        """
        The label for the plot's x-axis
        """

        self._xLabelProperties = LabelProperties()
        self._yLabelProperties = LabelProperties()

        self.legend = None

        self._xLimits = None
        self._yLimits = None

        self.twinxLabel = None
        self.twinxIndex = -1
        self.twinxLimits = None

        self.lineStyles = None
        self.lineColors = None
        self.markers = None

        self.width = None

        self.height = None

        self.dpi = 100

        self.plotParams = None

        self.logx = False
        """
        If true, this plot's x-axis will be drawn in log scale.
        """

        self.logy = False
        """
        If true, this plot's y-axis will be drawn in log scale.
        """

        self.loglog = False
        """
        If true, both this plot's axes will be drawn in log scale.
        """

        self.logbase = 10
        """
        The base of the logarithm used to draw log scale axes.
        """

        self.logbasex = None
        """
        The base of the logarithm used to draw the x-axis. Overrides `logbase`,
        and only takes effect if logx or loglog are True.
        """

        self.logbasey = None
        """
        The base of the logarithm used to draw the y-axis. Overrides `logbase`,
        and only takes effect if logy or loglog are True.
        """

        self._grid = Grid()
        self._grid.visible = False

        self.insets = []

        self.hideTicks = False
        """
        If True, this plot's tick labels are hidden.
        """

        self.latex = False

        self.axesLabelSize = None
        """
        The size of the text used for labeling the x and y axes.
        """

        self.xTickLabelSize = None
        """
        The size of the text used for x-axis tick labels
        """

        self.yTickLabelSize = None
        """
        The size of the text used for y-axis tick labels
        """

        self.titleProperties = LabelProperties()

        self.tight = False
        """
        If True, this plot is auto-scaled so that axis labels don't get cut off.
        """

        self.projection = None
        """
        Defines the projection used when drawing this plot. The only currently
        supported value other than the standard (no projection) is 'polar'.
        """

    @property
    def xLabelProperties(self):
        """
        A dictionary of properties that control the appearance of the X axis'
        axis label. See :ref:`styling-labels` for more information on which
        properties can be set.
        """
        return self._xLabelProperties

    @xLabelProperties.setter
    def xLabelProperties(self, propsobj):
        self._xLabelProperties.update(propsobj)

    @property
    def yLabelProperties(self):
        """
        A dictionary of properties that control the appearance of the Y axis'
        axis label. See :ref:`styling-labels` for more information on which
        properties can be set.
        """
        return self._yLabelProperties

    @yLabelProperties.setter
    def yLabelProperties(self, propsobj):
        self._yLabelProperties.update(propsobj)

    @property
    def xLimits(self):
        """
        A pair giving the minimum and maximum values visible on the x-axis.
        """
        return self._xLimits

    @xLimits.setter
    def xLimits(self, value):
        if type(value) not in [tuple, list] or len(value) != 2:
            raise AttributeError("xLimits must be set to a (min, max) tuple")

        self._xLimits = tuple(value)

    @property
    def yLimits(self):
        """
        A pair giving the minimum and maximum values visible on the x-axis.
        """
        return self._yLimits

    @yLimits.setter
    def yLimits(self, value):
        if type(value) not in [tuple, list] or len(value) != 2:
            raise AttributeError("yLimits must be set to a (min, max) tuple")

        self._yLimits = value

    @property
    def legendLabelSize(self):
        """
        The size of the text in this plot's legend.
        """

        return self.legend.labelSize

    @legendLabelSize.setter
    def legendLabelSize(self, size):
        self.setLegendLabelSize(size)

    @property
    def grid(self):
        """
        A boomslang.Grid.Grid that defines the properties of this plot's grid
        lines. See :ref:`plots-grid-lines` for configuration options.
        """
        return self._grid

    @grid.setter
    def grid(self, value):
        if isinstance(value, bool) and value == True:
            self._grid.visible = True
        else:
            raise AttributeError("Plot.grid cannot be re-assigned")

    def setTitleProperties(self, **propList):
        """
        Set the properties of the title. See :ref:`styling-labels` for more
        information about valid properties.
        """
        self.__setProperties(self.titleProperties, propList)

    def __setProperties(self, propsDict, propList):
        for (key, val) in propList.items():
            propsDict[key] = val

    def __str__(self):
        return str(self.__dict__)

    def setAxesLabelSize(self, size):
        self.axesLabelSize = size

    def setXTickLabelSize(self, size):
        self.xTickLabelSize = size

    def setYTickLabelSize(self, size):
        self.yTickLabelSize = size

    def setLegendLabelSize(self, size):
        if self.legend is None:
            self.legend = Legend()

        self.legend.labelSize = size

    def split(self, pieces):
        """
        Split this plot into `pieces` separate plots, each showing a different
        portion of the x-axis
        """

        splitPlots = [copy.deepcopy(self) for i in xrange(pieces)]

        for plot in splitPlots:
            plot.plots = []

        for plot in self.plots:
            elements = plot.split(pieces)
            for i in xrange(pieces):
                splitPlots[i].add(elements[i])
                splitPlots[i].setXLimits(
                    min(elements[i].xValues), max(elements[i].xValues))
        return splitPlots

    def getDimensions(self):
        """
        Get the dimensions of this plot.
        """
        if self.width is None:
            (self.width, self.height) = getGoldenRatioDimensions(8.0)
        elif self.height is None:
            (goldWidth, goldHeight) = getGoldenRatioDimensions(self.width)
            self.height = goldHeight
        return (self.width, self.height)

    def hideTickLabels(self):
        self.hideTicks = True

    def setDimensions(self, width=None, height=None, dpi=100):
        """
        Set the dimensions for this plot to `width` x `height`
        """
        self.width = width
        self.height = height
        self.dpi = dpi

    def add(self, plottableObject):
        """
        Add a plottable object (a Line, Bar, etc.) to this plot, causing it to
        be drawn when the plot is drawn.
        """

        if not issubclass(plottableObject.__class__, PlotInfo):
            raise BoomslangPlotConfigurationException(
                "All objects added to a Plot must be a subclass of PlotInfo")

        self.plots.append(plottableObject)

    def addInset(self, plot, **kwargs):
        """
        Add `plot` (a Plot object) as an inset to this plot object.

        Valid arguments are as follows:

        ============  ====================================================================================================================
        Argument      Description
        ============  ====================================================================================================================
        ``width``     The width of the inset as a fraction of the size of the parent plot
        ``height``    The height of the inset as a fraction of the size of the parent plot
        ``location``  The location of the inset. See :ref:`plots-locations` for valid locations.
        ``padding``   The amount of padding between the edge of the parent plot and the inset as a fraction of the size of the parent plot
        ============  ====================================================================================================================
        """
        inset = Inset(plot, **kwargs)
        self.insets.append(inset)

    def addLineStyle(self, style):
        """
        Add a line style to the list of line styles through which the plot will
        cycle when drawing lines. If no line styles are specified, the plot
        will default to the line style specified in the Line objects
        themselves.

        Note that, when drawing lines, all line styles for a given color are
        cycled through before another color is used.
        """
        if self.lineStyles is None:
            self.lineStyles = []

        currStyle = LineStyle()
        currStyle.style = style
        self.lineStyles.append(currStyle)

    def addLineColor(self, color):
        """
        Add a line color to the list of line colors through which the plot will
        cycle when drawing lines. If no line colors are specified, the line
        colors specified by the Line objects themselves will be used.

        Note that, when drawing lines, all line styles for a given color are
        cycled through before another color is used.
        """
        if self.lineColors is None:
            self.lineColors = []
        self.lineColors.append(color)

    def addMarker(self, marker):
        """
        Add a marker style to the list of marker styles through which the plot
        will cycle when drawing lines. If no markers are specified, the markers
        specified by the Line objects themselves will be used.

        Note that, when drawing lines, all line style/color combinations are
        cycled through with a given marker before a new marker is chosen.
        """
        if self.markers is None:
            self.markers = []

        currMarker = Marker()
        currMarker.marker = marker
        self.markers.append(currMarker)

    def getNumPlots(self):
        # Get the number of plottable objects currently registered for this
        # plot.
        return len(self.plots)

    def setTwinX(self, label, index, yMin=None, yMax=None):
        """
        Make the plot use a secondary y-axis with the provided label. All
        registered plottable objects at or after the given index will use this
        second axis.
        """
        self.twinxLabel = label
        self.twinxIndex = index

        if yMin is not None and yMax is not None:
            self.twinxLimits = (yMin, yMax)

    def setYFormatter(self, formatter):
        """
        Set the y-axis formatter used by this plot to the given function.
        """
        self.yFormatter = pylab.FuncFormatter(formatter)

    def setXFormatter(self, formatter):
        """
        Set the x-axis formatter used by this plot to the given function.
        """
        self.xFormatter = pylab.FuncFormatter(formatter)

    def setXLabel(self, xLabel):
        self.xLabel = xLabel

    def setYLabel(self, yLabel):
        self.yLabel = yLabel

    def setXLimits(self, minX, maxX):
        self.xLimits = (minX, maxX)

    def setYLimits(self, minY, maxY):
        self.yLimits = (minY, maxY)

    def hasFigLegend(self, columns=1, location="best", scatterPoints=3,
                     draw_frame=True, bbox_to_anchor=None, labelSize=None,
                     title=None):
        """
        Declare that the figure has a legend with a given number of columns and
        location.
        """
        self.legend = Legend(columns = columns,
                              scatterPoints = scatterPoints,
                              drawFrame = draw_frame,
                              location = location,
                              figLegend = True,
                              labelSize = labelSize,
                              bboxToAnchor = bbox_to_anchor,
                              title = title)

    def hasLegend(self, columns=1, location="best", scatterPoints=3,
                  draw_frame=True, bbox_to_anchor=None, labelSize = None,
                  title=None):
        """
        Declare that the plot has a legend with a given number of columns and
        location.
        """
        self.legend = Legend(columns = columns,
                              scatterPoints = scatterPoints,
                              drawFrame = draw_frame,
                              location = location,
                              figLegend = False,
                              labelSize = labelSize,
                              bboxToAnchor = bbox_to_anchor,
                              title = title)

    def setTitle(self, title):
        self.title = title

    def __cmp__(self, other):
        if not isinstance(other, Plot):
            raise ValueError("Can't compare a Plot with a non-Plot")

        return cmp(self.title, other.title)

    def __setupLayout(self):
        layout = PlotLayout()
        (width, height) = self.getDimensions()

        layout.setPlotDimensions(width, height, dpi=self.dpi)

        if self.plotParams is not None:
            layout.setPlotParameters(**self.plotParams)

        if self.latex == True:
            layout.useLatexLabels()

        if self.axesLabelSize is not None:
            layout.setAxesLabelSize(self.axesLabelSize)

        if self.xTickLabelSize is not None:
            layout.setXTickLabelSize(self.xTickLabelSize)

        if self.yTickLabelSize is not None:
            layout.setYTickLabelSize(self.yTickLabelSize)

        layout.addPlot(self)
        return layout

    def useLatexLabels(self):
        self.latex = True

    def plot(self):
        """
        Draw this plot to a matplotlib canvas.
        """
        layout = self.__setupLayout()
        layout.plot()

    def plot_fig(self):
        layout = self.__setupLayout()
        return layout._doPlot()

    def setPlotParameters(self, **kwdict):
        """
        Set the margins of this plot. See `matplotlib's SubplotParams documentation <http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.SubplotParams>`_ for more details. It is recommended that you set :py:attr:`boomslang.Plot.Plot.tight` to True instead of setting these parameters.
        """
        self.plotParams = dict(kwdict)

        if "left" not in self.plotParams:
            self.plotParams["left"] = 0.12

        if "bottom" not in self.plotParams:
            self.plotParams["bottom"] = 0.10

        if "right" not in self.plotParams:
            self.plotParams["right"] = 0.90

        if "top" not in self.plotParams:
            self.plotParams["top"] = 0.90

        if "wspace" not in self.plotParams:
            self.plotParams["wspace"] = 0.20

        if "hspace" not in self.plotParams:
            self.plotParams["hspace"] = 0.20


    def save(self, filename, **kwargs):
        """
        Save this plot to a file.
        """
        layout = self.__setupLayout()
        layout.save(filename,**kwargs)

    def subplot(self, fig, row, column, position, projection):
        kwdict = {}

        if projection is not None:
            kwdict["projection"] = projection

        ax = fig.add_subplot(row, column, position, **kwdict)
        return self.drawPlot(fig, ax)

    def drawPlot(self, fig, ax):
        """
        Used by PlotLayout to plot the graph at a given location in the layout.
        """

        ax2 = None

        if self.tight:
            ax.autoscale_view(tight=True)

        for inset in self.insets:
            inset.draw(fig, ax)

        if self.hideTicks == True:
            for xtl in ax.get_xticklabels():
                xtl.set_visible(False)
            for xtick in ax.get_xticklines():
                xtick.set_visible(False)
            for ytl in ax.get_yticklabels():
                ytl.set_visible(False)
            for ytick in ax.get_yticklines():
                ytick.set_visible(False)

        if self.grid.visible == True:
            self.grid.draw(fig, ax)

        if self.loglog or self.logx:
            myBase = None

            if self.logbasex is not None:
                myBase = self.logbasex
            else:
                myBase = self.logbase

            ax.set_xscale('log', basex=myBase)
        if self.loglog or self.logy:
            myBase = None

            if self.logbasey is not None:
                myBase = self.logbasey
            else:
                myBase = self.logbase

            ax.set_yscale('log', basey=myBase)

        if self.twinxIndex > 0:
            ax2 = ax.twinx()
            ax2.set_ylabel(self.twinxLabel)
            if self.twinxLimits is not None:
                ax2.set_ylim(ymin=self.twinxLimits[0], ymax=self.twinxLimits[1])

        plotHandles = []
        plotLabels = []

        if self.xFormatter is not None:
            ax.xaxis.set_major_formatter(self.xFormatter)

        if self.yFormatter is not None:
            ax.yaxis.set_major_formatter(self.yFormatter)

        if self.title is not None:
            ax.set_title(self.title, **self.titleProperties)

        i = 0
        myAxis = ax

        hasLineStyles = self.lineStyles is not None
        hasColors = self.lineColors is not None
        hasMarkers = self.markers is not None

        numLineStyles = 1
        numColors = 1
        numMarkers = 1

        if hasLineStyles:
            numLineStyles = len(self.lineStyles)

        if hasColors:
            numColors = len(self.lineColors)

        if hasMarkers:
            numMarkers = len(self.markers)

        plotIndex = 0

        for plotInfo in self.plots:
            if self.twinxIndex >= 0 and i == self.twinxIndex:
                myAxis = ax2

            myLineStyle = None
            myColor = None
            myMarker = None

            # cycle through styles first, then markers, then colors
            colorIndex = (plotIndex / (numMarkers * numLineStyles)) % numColors
            markerIndex = int(plotIndex / numLineStyles) % numMarkers
            lineStyleIndex = plotIndex % numLineStyles

            if hasLineStyles:
                myLineStyle = self.lineStyles[lineStyleIndex].style

            if hasColors:
                myColor =  self.lineColors[colorIndex]

            if hasMarkers:
                myMarker = self.markers[markerIndex].marker


            plotIndex += 1

            if myLineStyle is not None:
                plotInfo.lineStyle = myLineStyle

            if myMarker is not None:
                plotInfo.marker = myMarker

            if myColor is not None:
                plotInfo.color = myColor

            plotInfo._preDraw()
            (currPlotHandles, currPlotLabels) = plotInfo.draw(fig, myAxis)

            labelIndices = [x for x in range(len(currPlotLabels)) \
                                if currPlotLabels[x] is not None]

            if len(labelIndices) > 0:
                plotHandles.extend([currPlotHandles[x] for x in labelIndices])
                plotLabels.extend([currPlotLabels[x] for x in labelIndices])

            if plotInfo.xLimits is not None:
                if self.xLimits is None:
                    self.xLimits = plotInfo.xLimits
                else:
                    (myXMin, myXMax) = plotInfo.xLimits
                    self.xLimits = (min(self.xLimits[0], myXMin),
                                 max(self.xLimits[1], myXMax))

            i += 1

        if self.xLimits is not None:
            ax.set_xlim(xmin=self.xLimits[0], xmax=self.xLimits[1])

        if self.yLimits is not None:
            ax.set_ylim(ymin=self.yLimits[0], ymax=self.yLimits[1])


        if self.xLabel is not None:
            ax.set_xlabel(self.xLabel, **self.xLabelProperties)

        if self.yLabel is not None:
            ax.set_ylabel(self.yLabel, **self.yLabelProperties)

        if self.legend is not None:
            if len(plotHandles) == 0:
                print >>sys.stderr, "ERROR: Plot wanted to draw a legend, " \
                    "but none of its elements have labels"
                sys.exit(1)

            if self.twinxIndex > 0:
                legendAxis = ax2
            else:
                legendAxis = ax

            self.legend.draw(fig, legendAxis, plotHandles, plotLabels)

        return (plotHandles, plotLabels)
