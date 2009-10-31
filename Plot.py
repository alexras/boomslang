import pylab
from matplotlib import pyplot
import sys
from PlotInfo import PlotInfo
from PlotLayout import *
import copy

try:
    import mpl_toolkits.axes_grid.inset_locator
    insetLocatorLoaded = True
except ImportError:
    insetLocatorLoaded = False

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
        
        self.insets = []
        
        self.hideTicks = False
        
        self.latex = False
    
    def split(self, pieces):
       splitPlots = [copy.deepcopy(self) for i in xrange(pieces)]
       
       for plot in splitPlots:
           plot.plots = []
       
       for plot in self.plots:
           elements = plot.split(pieces)
           for i in xrange(pieces):
               splitPlots[i].add(elements[i])
               splitPlots[i].setXLimits(min(elements[i].xValues), max(elements[i].xValues))
       return splitPlots
       
    def getDimensions(self):
        if self.width is None:
            (self.width, self.height) = getGoldenRatioDimensions(8.0)
        elif self.height is None:
            (goldWidth, goldHeight) = getGoldenRatioDimensions(self.width)
            self.height = goldHeight
        return (self.width, self.height)

    def hideTickLabels(self):
        self.hideTicks = True

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

    def addInset(self, inset, width=0.3, height=0.3, location="upper right", 
                 padding=0.05):
        if not isinstance(inset, Plot):
            print >>sys.stderr, "Can only add Plots as insets"
            sys.exit(1)

        if not isinstance(width, float) or not isinstance(height, float):
            print >>sys.stderr, \
                "Width and height of inset must be numbers in range [0.0, 1.0)"
            sys.exit(1)
        
        self.insets.append((inset, width, height, location, padding))

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

        if self.latex == True:
            layout.useLatexLabels()

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

    def plotInset(self, parentAxes, width, height, location, padding):
        if not insetLocatorLoaded:
            print sys.stderr, "Plotting insets requires mpl_toolkits.axes_grid.inset_locatoor, which your version of matplotlib doesn't appear to have."
            sys.exit(1)

        locationMap = {"best" : 0, 
                       "upper right" : 1,
                       "upper left" : 2, 
                       "lower left" : 3,
                       "lower right" : 4, 
                       "right" : 5, 
                       "center left" : 6, 
                       "center right" : 7,
                       "lower center" : 8, 
                       "upper center" : 9, 
                       "center" : 10}

        if location not in locationMap:
            print >>sys.stderr, "Location '%s' isn't valid. Valid locations are: %s" % (location, ', '.join(locationMap))

        ax = mpl_toolkits.axes_grid.inset_locator.inset_axes(parentAxes, width="%.2f%%" % (width * 100.0), height="%.2f%%" % (height * 100.0), loc=locationMap[location])
        return self.drawPlot(ax)

    # def plotInset(self, parentAxes, width, height, hPos, vPos, padding):
    #     print parentAxes
    #     insetWidth = width
    #     insetHeight = height
        
    #     parentBBox = parentAxes.get_position().get_points()

    #     (parentLeft, parentBottom) = parentBBox[0]
    #     (parentWidth, parentHeight) = parentBBox[1]

    #     insetLeft = parentLeft
    #     insetBottom = parentBottom
    #     width = width * parentWidth
    #     height = height * parentHeight

    #     if vPos == "lower":
    #         insetBottom += padding
    #     elif vPos == "upper":
    #         insetBottom += parentHeight - (padding + height)

    #     if hPos == "left":
    #         insetLeft += padding
    #     elif hPos == "center":
    #         insetLeft += parentWidth - (width / 2.0)
    #     elif hPos == "right":
    #         insetLeft += parentWidth - (padding + width)
        
    #     print insetLeft, insetBottom, width, height
        
    #     ax = pylab.axes([insetLeft, insetBottom, width, height])
    #     return self.drawPlot(ax)

    def subplot(self, row, column, position):
        ax = pylab.subplot(row, column, position)
        return self.drawPlot(ax)
        
    def drawPlot(self, ax):
        """
        Used by PlotLayout to plot the graph at a given location in the layout.
        """
        for insetInfo in self.insets:
            insetInfo[0].plotInset(ax, *(insetInfo[1:]))
        
        if self.hideTicks == True:
            for xtl in ax.get_xticklabels():
                xtl.set_visible(False)
            for xtick in ax.get_xticklines():
                xtick.set_visible(False)
            for ytl in ax.get_yticklabels():
                ytl.set_visible(False)
            for ytick in ax.get_yticklines():
                ytick.set_visible(False)

        
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

        legendKeywords = {}
        
        if self.legendCols > 0:
            versionParts = [int(x) for x in matplotlib.__version__.split('.')]
            
            (superMajor, major, minor) = versionParts[0:3]

            if superMajor == 0 and major < 98:
                print >>sys.stderr, "Number of columns support not available in versions of matplotlib prior to 0.98"
            else:
                legendKeywords["ncol"] = self.legendCols

        
        if self.legend:
            pylab.legend(plotHandles, plotLabels, loc=self.legendLoc, 
                         **legendKeywords)
        if self.figLegend:
            pylab.figlegend(plotHandles, plotLabels, loc=self.legendLoc, 
                            **legendKeywords)
                
        return (plotHandles, plotLabels)
