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

class Plot(object):
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
        self.scatterPoints=3
        self.legendLoc = None

        self.twinxLabel = None
        self.twinxIndex = -1
        self.twinxLimits = None

        self.lineStyles = None
        self.lineColors = None
        self.markers = None

        self.width = None
        self.height = None
        
        self.plotParams = None
        self.logx = False
        self.logy = False
        self.loglog = False
        self.logbase = 10
        self.logbasex = None
        self.logbasey = None
        
        self.grid = False

        self.figLegend = False
        
        self.insets = []
        
        self.hideTicks = False
        
        self.latex = False
        
        self.axesLabelSize = None
        self.xTickLabelSize = None
        self.yTickLabelSize = None
        self.legendLabelSize = None
        
        self.titleProperties = {}

        self.tight = False
        
    def setTitleProperties(self, **propList):
        self.__setProperties(self.titleProperties, propList)

    def __setProperties(self, propsDict, propList):
        # Going to restrict the set of properties that can be modified so they
        # don't mess with the rest of the system
        
        validProperties = ["alpha", "backgroundColor", "color", 
                           "horizontalalignment", "linespacing", 
                           "multialignment", "rotation", "stretch", "style", 
                           "verticalalignment", "weight"]
        
        for (key, val) in propList.items():
            if key not in validProperties:
                print >>sys.stderr, "Property '%s' is not currently supported" % (key)
            else:
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
        self.legendLabelSize = size
    
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

    def addMarker(self, marker):
        if self.markers is None:
            self.markers = []
        self.markers.append(marker)

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
        self.xFormatter = pylab.FuncFormatter(formatter)

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

    def hasFigLegend(self, columns=1, location="best", scatterPoints=3, 
                     draw_frame=True):
        self.figLegend = True
        self.legendCols = columns
        self.legendLoc = location
        self.scatterPoints = scatterPoints
        self.legendDrawFrame = draw_frame

    def hasLegend(self, columns=1, location="best", scatterPoints=3,
                  draw_frame=True):
        """
        Declare that the plot has a legend with a given number of columns and
        location.
        """
        self.legend = True
        self.legendCols = columns
        self.legendLoc = location
        self.scatterPoints = scatterPoints
        self.legendDrawFrame = draw_frame

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


    def save(self, filename, **kwargs):
        """
        Save this plot to a file.
        """
        layout = self.__setupLayout()
        layout.save(filename,**kwargs)

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

        if self.tight:
            ax.autoscale_view(tight=True)
            
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
            #TODO: color and linestyle for gridlines should be configurable
            ax.grid(color="#dddddd", linestyle="-")
            # Gridlines should be below plots
            ax.set_axisbelow(True)

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
            markerIndex = (plotIndex / numLineStyles) % numMarkers
            lineStyleIndex = plotIndex % numLineStyles

            if hasLineStyles:
                myLineStyle = self.lineStyles[lineStyleIndex]
            
            if hasColors:
                myColor =  self.lineColors[colorIndex]
            
            if hasMarkers:
                myMarker = self.markers[markerIndex]

                                
            plotIndex += 1
                
            if myLineStyle is not None:
                plotInfo.lineStyle = myLineStyle

            if myMarker is not None:
                plotInfo.marker = myMarker
            
            if myColor is not None:
                plotInfo.color = myColor
            
            (currPlotHandles, currPlotLabels) = plotInfo.draw(myAxis)
            
            labelIndices = [x for x in range(len(currPlotLabels)) \
                                if currPlotLabels[x] is not None]
            
            if len(labelIndices) > 0:
                plotHandles.extend([currPlotHandles[x] for x in labelIndices])
                plotLabels.extend([currPlotLabels[x] for x in labelIndices])
            
            if plotInfo.xLimits is not None:
                if self.xlim is None:
                    self.xlim = plotInfo.xLimits
                else:
                    (myXMin, myXMax) = plotInfo.xLimits
                    self.xlim = (min(self.xlim[0], myXMin), 
                                 max(self.xlim[1], myXMax))
            
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
                legendKeywords["scatterpoints"] = self.scatterPoints
                
                if self.legendLabelSize is not None:
                    legendKeywords["prop"] = {"size" : self.legendLabelSize}

        legend = None # So we can disable the box if we want

        if self.legend:
            if len(plotHandles) == 0:
                print >>sys.stderr, "ERROR: Plot wanted to draw a legend, but none of its elements have labels"
                sys.exit(1)
            legend = pylab.legend(plotHandles, plotLabels,
                                  loc=self.legendLoc, **legendKeywords)
        if self.figLegend:
            legend = pylab.figlegend(plotHandles, plotLabels,
                                     loc=self.legendLoc, **legendKeywords)

        if legend:
            legend.draw_frame(self.legendDrawFrame)
 
        return (plotHandles, plotLabels)
