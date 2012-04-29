import pylab
from matplotlib import pyplot
import os
from boomslang import PlotLayout

from Utils import getGoldenRatioDimensions, _check_min_matplotlib_version

class WeightedPlotLayout(PlotLayout):
    def __init__(self):
        super(WeightedPlotLayout,self).__init__()
        self.groupedWeights = {}
        self.weights = []
        self.figTitle = None
        self.usePlotParams = False # Include plot's parameters in
                                   # computing layout.

    def addPlot(self, plot, grouping=None, weight=1):
        super(WeightedPlotLayout,self).addPlot(plot, grouping=grouping)

        if grouping not in self.groupedWeights:
            self.groupedWeights[grouping] = []
        self.groupedWeights[grouping].append(weight)

    def setFigTitle(self, title=None):
        self.figTitle = title

    def _doPlot(self):
        if len(self.groupedPlots) + len(self.plots) == 0:
            print "WeightedPlotLayout.plot(): No data to plot!"
            return

        oldRCParams = {}

        if self.rcParams is not None:
            for (key,val) in self.rcParams.items():
                oldRCParams[key] = pylab.rcParams[key]
                pylab.rcParams[key] = val

        numRows = len(self.groupedPlots.keys()) + len(self.plots)
        maxRowLength = max([len(self.groupedPlots[f])
                                for f in self.groupedPlots.keys()])

        if self.groupOrder is not None:
            keyList = self.groupOrder
        else:
            keyList = sorted(self.groupedPlots.keys())

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

        def applyParams(r, pp):
            if pp is None: return r

            left, bottom, width, height = r

            return [
                    left + width * pp.get('left',0),
                    bottom + height * pp.get('bottom',0),
                    width * (pp.get('right',1) - pp.get('left',0)),
                    height * (pp.get('top',1) - pp.get('bottom',0))
                   ]

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
                myWidth = availableWidth * weights[i] / totalWeight

                rect = [left, bottom, myWidth, rowHeight]

                if self.usePlotParams and hasattr(plot,'plotParams'):
                    rect = applyParams(rect, plot.plotParams)

                plotInfo.append((plot, rect))

                left += myWidth + wgap

            currentRow += 1

        # Generate rects for ungrouped plots
        for plot in self.plots:
            bottom = figTop - rowHeight - (rowHeight + hgap) * currentRow
            left = figLeft

            rect = [left, bottom, rowWidth, rowHeight]

            if self.usePlotParams and hasattr(plot,'plotParams'):
                rect = applyParams(rect, plot.plotParams)

            plotInfo.append((plot, rect))

            currentRow += 1

        # Plot everything
        for (plot, rect) in plotInfo:
            ax = fig.add_axes(rect)
            (currPlotHandles, currPlotLabels) = plot.drawPlot(fig, ax)

            for i in xrange(len(currPlotHandles)):
                if currPlotLabels[i] in plotLabels:
                    continue

                if isinstance(currPlotHandles[i], list):
                    plotHandles.append(currPlotHandles[i][0])
                else:
                    plotHandles.append(currPlotHandles[i])

                plotLabels.append(currPlotLabels[i])

        if self.figTitle is not None:
            fig.suptitle(self.figTitle)

        for (key,val) in oldRCParams.items():
            pylab.rcParams[key] = val

        return fig
