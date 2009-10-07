import pylab
from matplotlib import pyplot
import sys

from Utils import getGoldenRatioDimensions

class PlotLayout:
    def __init__(self):
        self.groupedPlots = {}
        self.plots = []
        self.groupOrder = None

        self.width = 1
        self.plotParams = None

        self.dimensions = None
        self.figdimensions = None
        self.figTitle = None

        self.figLegendLoc = None
        self.figLegendCols = None
        self.figLegendNumPlots = -1

        self.rcParams = None

    def __setRCParam(self, param, value):
        if self.rcParams is None:
            self.rcParams = {}

        self.rcParams[param] = value

    def useStandardFont(self):
        self.__setRCParam("font.family", "serif")
        self.__setRCParam("font.style", "normal")
        self.__setRCParam("font.variant", "normal")
        self.__setRCParam("font.weight", "normal")
        self.__setRCParam("font.stretch", "normal")

    def setAxesLabelSize(self, size):
        self.__setRCParam("axes.labelsize", size)

    def setXTickLabelSize(self, size):
        self.__setRCParam("xtick.labelsize", size)

    def setYTickLabelSize(self, size):
        self.__setRCParam("ytick.labelsize", size)

    def setLegendLabelSize(self, size):
        self.__setRCParam("legend.fontsize", size)

    def setFigureTitle(self, title):
        self.figTitle = title

    def setWidth(self, width):
        self.width = int(width)

    def hasFigLegend(self, loc="best", numcols=1, firstPlots=-1):
        self.figLegendLoc = loc
        self.figLegendCols = numcols

        if firstPlots >= 0:
            self.figLegendNumPlots = firstPlots

    def addPlot(self, plot, grouping=None):
        if grouping == None:
            self.plots.append(plot)
        else:
            if grouping not in self.groupedPlots:
                self.groupedPlots[grouping] = []

            self.groupedPlots[grouping].append(plot)

    def setGroupOrder(self, groupOrder):
        self.groupOrder = groupOrder

    def setPlotDimensions(self, x, y):
        self.dimensions = (x,y)

    def setFigureDimensions(self, x, y):
        self.figdimensions = (x,y)

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
            

    def __doPlot(self):
        if len(self.groupedPlots) + len(self.plots) == 0:
            print "PlotLayout.plot(): No data to plot!"
            return

        if self.rcParams is not None:
            pylab.rcParams.update(self.rcParams)

        groupedPlotLengths = [len(plots) for plots in self.groupedPlots.values()]

        self.plots.sort()

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
            fig = pyplot.figure(figsize=getGoldenRatioDimensions(8.0))
            # figWidth = fig.get_figwidth()
            # print figWidth
            # print fig.get_figheight()
            # (goldenWidth, goldenHeight) = getGoldenRatioDimensions(figWidth)
            # fig.set_figheight(goldenHeight)
            # print fig.get_figheight()

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

                (currPlotHandles, currPlotLabels) = plot.subplot(
                    myRows, myCols, myPos)

                for i in xrange(len(currPlotHandles)):
                    if currPlotLabels[i] in plotLabels:
                        continue

                    if isinstance(currPlotHandles[i], list):
                        plotHandles.append(currPlotHandles[i][0])
                    else:
                        plotHandles.append(currPlotHandles[i])

                    plotLabels.append(currPlotLabels[i])

#                plotHandles.extend(currPlotHandles)
#                plotLabels.extend(currPlotLabels)

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
                (currPlotHandles, currPlotLabels) = plot.subplot(
                    myRows, myCols, myPos)
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
            pylab.figlegend(plotHandles, plotLabels, 
                            self.figLegendLoc, 
                            ncol=self.figLegendCols)

        if self.plotParams is not None:
            pylab.subplots_adjust(left=self.plotParams["left"],
                                  bottom=self.plotParams["bottom"],
                                  right=self.plotParams["right"],
                                  top=self.plotParams["top"],
                                  wspace=self.plotParams["wspace"],
                                  hspace=self.plotParams["hspace"])

    def plot(self):
        self.__doPlot()
        pylab.show()

    def save(self, filename):
        print "Saving %s ..." % filename
        self.__doPlot()
        pylab.savefig(filename)
        pylab.clf()
