import pylab
from matplotlib import pyplot
import sys
from PlotInfo import PlotInfo
from PlotLayout import *

from Utils import getGoldenRatioDimensions

class Plot:
    """
    Represents a single plot, usually consisting of a single X and Y axis.
    """

    def __init__(self):
        self.plots = []
        self.title = None
        self.xFormatter = None
        self.yFormatter = None
        self.yLabel = None
        self.xLabel = None
        self.legend = False

        self.xlim = None
        self.ylim = None

        self.legendCols = 0
        self.legendLoc = None

        self.twinxLabel = None
        self.twinxIndex = -1
        self.twinxLimits = None

        self.lineStyles = None
        self.lineColors = None

        self.title = None

        self.width = None
        self.height = None
        
        self.plotParams = None
        self.logx = False
        self.logy = False
        self.loglog = False
        self.grid = False

        self.figLegend = False


    def getDimensions(self):
        if self.width is None:
            (self.width, self.height) = getGoldenRatioDimensions(8.0)
        elif self.height is None:
            (goldWidth, goldHeight) = getGoldenRatioDimensions(self.width)
            self.height = goldHeight
        return (self.width, self.height)

    def setDimensions(self, width=None, height=None):
        self.width = width
        self.height = height

    def add(self, plottableObject):
        """
        Add a plottable object (a Line, Bar, etc.) to this plot, causing it to
        be drawn when the plot is drawn.
        """

        if not issubclass(plottableObject.__class__, PlotInfo):
            print >>sys.stderr, "All objects added to a Plot must be a subclass of PlotInfo"
            sys.exit(1)
        self.plots.append(plottableObject)

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
        self.lineStyles.append(style)

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

    def getNumPlots(self):
        """
        Get the number of plottable objects currently registered for this plot.
        """
        return len(self.plots)
    
    def setTwinX(self, label, index, yMin=None, yMax=None):
        """
        Make the plot use a secondary y-axis with the provided label. All
        registered plottable objects at or after the given index will use this
        second axis.
        """
        self.twinxLabel = label
        self.twinxIndex = index

        if yMin == None and yMax == None:
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
        self.xFormatter = formatter

    def setXLabel(self, xLabel):
        """
        Set the x-axis label.
        """
        self.xLabel = xLabel

    def setYLabel(self, yLabel):
        """
        Set the y-axis label.
        """
        self.yLabel = yLabel

    def setXLimits(self, minX, maxX):
        """
        Set the minimum and maximum values for the x-axis.
        """
        self.xlim = (minX, maxX)

    def setYLimits(self, minY, maxY):
        """
        Set the minimum and maximum values for the y-axis.
        """
        self.ylim = (minY, maxY)

    def hasFigLegend(self, columns=1, location="best"):
        self.figLegend = True
        self.legendCols = columns
        self.legendLoc = location

    def hasLegend(self, columns=1, location="best"):
        """
        Declare that the plot has a legend with a given number of columns and
        location.
        """
        self.legend = True
        self.legendCols = columns
        self.legendLoc = location

    def setTitle(self, title):
        self.title = title

    def __cmp__(self, other):
        assert(isinstance(other, Plot))

        return cmp(self.title, other.title)

    def __setupLayout(self):
        layout = PlotLayout()
        (width, height) = self.getDimensions()
        
        layout.setPlotDimensions(width, height)

        if self.plotParams is not None:
            layout.setPlotParameters(**self.plotParams)

        layout.addPlot(self)
        return layout

    def plot(self):
        """
        Draw this plot to a matplotlib canvas.
        """
        layout = self.__setupLayout()
        layout.plot()

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


    def save(self, filename):
        """
        Save this plot to a file.
        """
        layout = self.__setupLayout()
        layout.save(filename)

    def subplot(self, row, column, position):
        """
        Used by PlotLayout to plot the graph at a given location in the layout.
        """
        ax = pylab.subplot(row, column, position)

        if self.grid:
            ax.grid()

        if self.loglog or self.logx:
            ax.set_xscale('log')
        if self.loglog or self.logy:
            ax.set_yscale('log')

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
            ax.set_title(self.title)

        i = 0
        myAxis = ax
        for plotInfo in self.plots:
            if self.twinxIndex >= 0 and i == self.twinxIndex:
                myAxis = ax2

            if self.lineStyles is not None:
                numLineStyles = len(self.lineStyles)

                myLineStyle = self.lineStyles[i % numLineStyles]
                myColor = "black"

                if self.lineColors is not None:
                    numColors = len(self.lineColors)
                    myColor = self.lineColors[(i / numLineStyles) % numColors]
                
                plotInfo.color = myColor
                plotInfo.lineStyle = myLineStyle

            (currPlotHandles, currPlotLabels) = plotInfo.draw(myAxis)
            plotHandles.extend(currPlotHandles)
            plotLabels.extend(currPlotLabels)

            i += 1

        if self.xlim is not None:
            pylab.xlim(xmin=self.xlim[0], xmax=self.xlim[1])

        if self.ylim is not None:
            pylab.ylim(ymin=self.ylim[0], ymax=self.ylim[1])


        if self.xLabel is not None:
            ax.set_xlabel(self.xLabel)

        if self.yLabel is not None:
            ax.set_ylabel(self.yLabel)

        if self.legend:
            pylab.legend(plotHandles, plotLabels, loc=self.legendLoc, 
                         ncol=self.legendCols)
        if self.figLegend:
            pylab.figlegend(plotHandles, plotLabels, loc=self.legendLoc, 
                            ncol=self.legendCols)

        return (plotHandles, plotLabels)
