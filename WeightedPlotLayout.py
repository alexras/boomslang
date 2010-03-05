import pylab
import matplotlib
from matplotlib import pyplot
import sys
import os
from boomslang import PlotLayout

from Utils import getGoldenRatioDimensions

class WeightedPlotLayout(PlotLayout):
    def __init__(self):
        super(WeightedPlotLayout,self).__init__()
        self.groupedWeights = {}
        self.weights = []

    def addPlot(self, plot, grouping=None, weight=1):
        super(WeightedPlotLayout,self).addPlot(plot, grouping=grouping)

        if grouping == None:
            self.weights.append(weight)
        else:
            if grouping not in self.groupedWeights:
                self.groupedWeights[grouping] = []
            self.groupedWeights[grouping].append(weight)

    def _doPlot(self):
        if len(self.groupedPlots) + len(self.plots) == 0:
            print "WeightedPlotLayout.plot(): No data to plot!"
            return

        if self.rcParams is not None:
            pylab.rcParams.update(self.rcParams)

        numRows = len(self.groupedPlots.keys()) + len(self.plots)
        maxRowLength = max([len(self.groupedPlots[f])
                                for f in self.groupedPlots.keys()])

        if self.groupOrder is not None:
            keyList = self.groupOrder
        else:
            keyList = self.groupedPlots.keys()

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
            # figWidth = fig.get_figwidth()
            # print figWidth
            # print fig.get_figheight()
            # (goldenWidth, goldenHeight) = getGoldenRatioDimensions(figWidth)
            # fig.set_figheight(goldenHeight)
            # print fig.get_figheight()

        plotHandles = []
        plotLabels = []

        # Force a call to plotParams since we need them here
        if self.plotParams is None:
            self.setPlotParameters(**dict())

        figTop = self.plotParams["top"]
        figLeft = self.plotParams["left"]

        wspace = self.plotParams["wspace"]
        hspace = self.plotParams["hspace"]

        height = figTop - self.plotParams["bottom"]
        rowHeight = height / (numRows + (numRows - 1) * hspace)
        hgap = self.plotParams["hspace"] * rowHeight

        rowWidth = self.plotParams["right"] - figLeft

        # To contain a list of plots and rects, so we can do the
        # information collection in one pass
        plotInfo = []

        # Generate rects for grouped plots
        currentRow = 0
        for grouping in keyList:
            plots = self.groupedPlots[grouping]
            weights = self.groupedWeights[grouping]

            totalWeight = 1.0 * sum(weights)
            numPlots = len(plots)

            # hspace, wspace behavior defined in matplotlib/axes.py
            # in the class SubplotBase
            unitWidth = rowWidth / (numPlots + (numPlots-1) * wspace)
            availableWidth = unitWidth * numPlots
            wgap = unitWidth * wspace

            bottom = figTop - rowHeight - (rowHeight + hgap) * currentRow
            left = figLeft

            for i in range(0, len(plots)):
                plot = plots[i]
                weight = weights[i]
                myWidth = availableWidth * weights[i] / totalWeight

                plotInfo.append((plot, [left, bottom, myWidth, rowHeight]))

                left += myWidth + wgap

            currentRow += 1

        # Generate rects for ungrouped plots
        for plot in self.plots:
            bottom = figTop - rowHeight - (rowHeight + hgap) * currentRow
            left = figLeft
            plotInfo.append((plot, [left, bottom, rowWidth, rowHeight]))

            currentRow += 1

        # Plot everything
        for (plot, rect) in plotInfo:
            ax = fig.add_axes(rect)
            (currPlotHandles, currPlotLabels) = plot.drawPlot(ax)

            for i in xrange(len(currPlotHandles)):
                if currPlotLabels[i] in plotLabels:
                    continue

                if isinstance(currPlotHandles[i], list):
                    plotHandles.append(currPlotHandles[i][0])
                else:
                    plotHandles.append(currPlotHandles[i])

                plotLabels.append(currPlotLabels[i])


        if self.figLegendLoc is not None:
            figLegendKeywords = {}

            if self.figLegendCols is not None:
                versionPieces = [int(x) for x in matplotlib.__version__.split('.')]

                (superMajor, major, minor) = versionPieces[0:3]

                if superMajor == 0 and major < 98:
                    print >>sys.stderr, "Number of columns support not available in versions of matplotlib prior to 0.98"
                else:
                    figLegendKeywords["ncol"] = self.figLegendCols

            pylab.figlegend(plotHandles, plotLabels,
                            self.figLegendLoc,
                            **figLegendKeywords)
