import os
import sys

class PlotInfo:
    def __init__(self, plotType):
        self.plotType = plotType

        self.xValues = []
        self.yValues = []

        self.xTickLabels = None
        self.yTickLabels = None
        self.xTickLabelPoints = None
        self.yTickLabelPoints = None
        self.label = None
        self.plotType = None

        self.yMins = None
        self.yMaxes = None
        self.yErrors = None

    def draw(self, axis):
        if self.xTickLabels is not None:
            if self.xTickLabelPoints is None:
                axis.set_xticks(range(len(self.xTickLabels)))
            else:
                axis.set_xticks(self.xTickLabelPoints)
            axis.set_xticklabels(self.xTickLabels)
        
        if self.yTickLabels is not None:
            if self.yTickLabelPoints is None:
                axis.set_yticks(range(len(self.yTickLabels)))
            else:
                axis.set_yticks(self.yTickLabelPoints)
            axis.set_yticklabels(self.yTickLabels)

        errorBarKeywords = {}
        if hasattr(self, "color"):
            errorBarKeywords["ecolor"] = self.color

        if hasattr(self, "lineWidth"):
            errorBarKeywords["linewidth"] = self.lineWidth

        if hasattr(self, "lineStyle"):
            errorBarKeywords["linestyle"] = self.lineStyle

        errorBarKeywords["fmt"] = None

        if self.yMins is not None and self.yMaxes is not None:
            numYVals = len(self.yValues)
            yMin = [self.yValues[i] - self.yMins[i] for i in xrange(numYVals)]
            yMax = [self.yMaxes[i] - self.yValues[i] for i in xrange(numYVals)]


            errorBarKeywords["yerr"] = [yMin, yMax]

            axis.errorbar(self.xValues, self.yValues, **errorBarKeywords) 
        elif self.yErrors is not None:
            errorBarKeywords["yerr"] = self.yErrors
            axis.errorbar(self.xValues, self.yValues, **errorBarKeywords)
