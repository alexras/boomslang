import pylab
from matplotlib import pyplot
import os
import warnings
from boomslang_exceptions import BoomslangPlotRenderingException

from Utils import getGoldenRatioDimensions, _check_min_matplotlib_version

class PlotLayout(object):
    """
    Displays multiple :class:`boomslang.Plot.Plot` objects in one canvas in a
    grid, allowing the user to group related Plots in the same row.
    """

    def __init__(self):
        self.groupedPlots = {}
        self.plots = []

        self.groupOrder = None
        """
        If not None, a list of groups in order by the order in which they
        should be displayed
        """

        self._width = 1
        self.plotParams = None

        self.dimensions = None
        self.figdimensions = None
        self.dpi = None

        self.figLegendLoc = None
        self.figLegendCols = None

        self.rcParams = None

    def __setRCParam(self, param, value):
        if self.rcParams is None:
            self.rcParams = {}

        self.rcParams[param] = value

    def useLatexLabels(self):
        warnings.warn("WARNING: Using LaTeX labels requires dvipng and "
                      "ghostscript")
        self.__setRCParam("text.usetex", True)

    def setAxesLabelSize(self, size):
        self.__setRCParam("axes.labelsize", size)

    def setXTickLabelSize(self, size):
        self.__setRCParam("xtick.labelsize", size)

    def setYTickLabelSize(self, size):
        self.__setRCParam("ytick.labelsize", size)

    def setLegendLabelSize(self, size):
        self.__setRCParam("legend.fontsize", size)

    def setWidth(self, width):
        self.width = int(width)

    @property
    def width(self):
        """
        The width, in number of plots, of the layout.
        """
        return self._width

    @width.setter
    def width(self, width):
        self._width = int(width)

    def hasFigLegend(self, loc="best", columns=1, numcols=None):
        if numcols is not None:
            # hasLegend uses columns, rather than numcols.
            # trying to make this consistent.
            # this should catch named parameter usage
            columns = numcols
            warnings.warn("numcols deprecated for hasFigLegend", Warning)

        self.figLegendLoc = loc
        self.figLegendCols = columns

    def addPlot(self, plot, grouping=None):
        """
        Add `plot` (a :class:`boomslang.Plot.Plot`) to the layout. Optionally,
        specify a group name with `grouping`. Plots grouped in the same
        grouping are drawn on the same row of the grid.
        """
        if grouping == None:
            self.plots.append(plot)
        else:
            if grouping not in self.groupedPlots:
                self.groupedPlots[grouping] = []

            self.groupedPlots[grouping].append(plot)

    def setGroupOrder(self, groupOrder):
        self.groupOrder = groupOrder

    def setPlotDimensions(self, x, y, dpi=100):
        """
        Set the dimensions of each plot in the layout to be `x` by `y`.
        """
        self.dimensions = (x,y)
        self.dpi = dpi

    def setFigureDimensions(self, x, y, dpi=100):
        """
        Set the dimensions of the layout to be `x` by `y`. This overrides any
        values set with
        :py:func:`boomslang.PlotLayout.PlotLayout.setPlotDimensions`.
        """
        self.figdimensions = (x,y)
        self.dpi = dpi

    def setPlotParameters(self, **kwdict):
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


    def _doPlot(self):
        if len(self.groupedPlots) + len(self.plots) == 0:
            raise BoomslangPlotRenderingException("No data to plot!")

        oldRCParams = {}

        if self.rcParams is not None:

            for (param, value) in self.rcParams.items():
                oldRCParams[param] = pylab.rcParams[param]
                pylab.rcParams[param] = value

        groupedPlotLengths = [len(plots) for plots in self.groupedPlots.values()]

        if len(groupedPlotLengths) == 0:
            maxRowLength = self.width
        else:
            maxRowLength = max(groupedPlotLengths)

        numPlots = len(self.plots)

        if numPlots == 0:
            numExcessRows = 0
        elif numPlots <= maxRowLength:
            numExcessRows = 1
        elif numPlots % maxRowLength == 0:
            numExcessRows = numPlots / maxRowLength
        else:
            numExcessRows = (numPlots / maxRowLength) + 1

        numRows = len(self.groupedPlots.keys()) + numExcessRows

        if self.groupOrder is not None:
            keyList = self.groupOrder
        else:
            keyList = self.groupedPlots.keys()

        currentRow = 0

        if self.figdimensions is not None:
            fig = pyplot.figure(figsize=(self.figdimensions[0],
                                         self.figdimensions[1]))
        elif self.dimensions is not None:
            fig = pyplot.figure(figsize=(self.dimensions[0] * maxRowLength,
                                         self.dimensions[1] * numRows))
        else:
            (figWidth, figHeight) = getGoldenRatioDimensions(8.0)
            figWidth *= maxRowLength
            figHeight *= numRows
            fig = pyplot.figure(figsize=(figWidth, figHeight))

        plotHandles = []
        plotLabels = []

        for grouping in keyList:
            currentColumn = 1
            plots = self.groupedPlots[grouping]

            numPlots = len(plots)

            for plot in plots:
                myRows = numRows
                myCols = numPlots
                myPos = (currentRow * numPlots) + currentColumn

                (currPlotHandles, currPlotLabels) = self._plot_subplot(
                    plot = plot, fig = fig, rows = myRows, cols = myCols,
                    pos = myPos, projection=plot.projection)

                for i in xrange(len(currPlotHandles)):
                    if currPlotLabels[i] in plotLabels:
                        continue

                    if isinstance(currPlotHandles[i], list):
                        plotHandles.append(currPlotHandles[i][0])
                    else:
                        plotHandles.append(currPlotHandles[i])

                    plotLabels.append(currPlotLabels[i])

                currentColumn += 1
            currentRow += 1

        ungroupedPlotsRemaining = len(self.plots)
        if ungroupedPlotsRemaining > 0:
            currentColumn = 1

            for plot in self.plots:
                if currentColumn == 1:
                    numColumns = min(maxRowLength, ungroupedPlotsRemaining)

                myRows = numRows
                myCols = numColumns
                myPos = (currentRow * numColumns) + currentColumn

                (currPlotHandles, currPlotLabels) = self._plot_subplot(
                    plot = plot, fig = fig, rows = myRows, cols = myCols,
                    pos = myPos, projection=plot.projection)

                for i in xrange(len(currPlotHandles)):
                    if currPlotLabels[i] in plotLabels:
                        continue

                    if isinstance(currPlotHandles[i], list):
                        plotHandles.append(currPlotHandles[i][0])
                    else:
                        plotHandles.append(currPlotHandles[i])

                    plotLabels.append(currPlotLabels[i])

                currentColumn += 1

                if currentColumn > numColumns:
                    currentRow += 1
                    currentColumn = 1

                ungroupedPlotsRemaining -= 1

        if self.figLegendLoc is not None:
            figLegendKeywords = {}

            if self.figLegendCols is not None:
                if not _check_min_matplotlib_version(0, 98, 0):
                    warnings.warn("Number of columns support not available in "
                                  "versions of matplotlib prior to 0.98")
                else:
                    figLegendKeywords["ncol"] = self.figLegendCols

            fig.legend(plotHandles, plotLabels,
                       self.figLegendLoc,
                       **figLegendKeywords)

        if self.plotParams is not None:
            fig.subplots_adjust(left=self.plotParams["left"],
                                bottom=self.plotParams["bottom"],
                                right=self.plotParams["right"],
                                top=self.plotParams["top"],
                                wspace=self.plotParams["wspace"],
                                hspace=self.plotParams["hspace"])
        # Restore old RC params
        for (key,value) in oldRCParams.items():
            pylab.rcParams[key] = value

        if _check_min_matplotlib_version(1, 1, 0):
            fig.tight_layout()
        return fig

    def _plot_subplot(self, plot, fig, rows, cols, pos, projection):
        return plot.subplot(fig, rows, cols, pos, projection)

    def plot(self):
        """
        Draw this layout to a matplotlib canvas.
        """
        fig = self._doPlot()
        if not pylab.isinteractive():
            pylab.show()
        else:
            pylab.draw()
        pylab.close(fig)

    def save(self, filename, **kwargs):
        """
        Save this layout to a file.
        """
        tempDisplayHack = False

        if "DISPLAY" not in os.environ:
            tempDisplayHack = True
            os.environ["DISPLAY"] = ":0.0"
        fig = self._doPlot()
        fig.savefig(filename, dpi = self.dpi, **kwargs)
        # pylab holds on to all figures unless you explicitly close them
        pylab.close(fig)

        if tempDisplayHack == True:
            del os.environ["DISPLAY"]
