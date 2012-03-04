import os
import sys
import copy
import warnings

from LabelProperties import LabelProperties

class PlotInfo(object):
    def __init__(self,
                 plotType,
                 xValues = None,
                 yValues = None,
                 xTickLabels = None,
                 yTickLabels = None,
                 xTickLabelPoints = None,
                 yTickLabelPoints = None,
                 xTickLabelProperties = None,
                 yTickLabelProperties = None,
                 label = None,
                 yMins = None,
                 yMaxes = None,
                 yErrors = None,
                 autosort = True,
                 xLimits = None,
                 picker=None):

        if xValues is None:
            xValues = []

        if yValues is None:
            yValues = []

        if xTickLabels is None:
            xTickLabels = []

        if yTickLabels is None:
            yTickLabels = []

        if xTickLabelPoints is None:
            xTickLabelPoints = []

        if yTickLabelPoints is None:
            yTickLabelPoints = []

        if xTickLabelProperties is None:
            xTickLabelProperties = LabelProperties()

        if yTickLabelProperties is None:
            yTickLabelProperties = LabelProperties()

        if yMins is None:
            yMins = []

        if yMaxes is None:
            yMaxes = []

        if yErrors is None:
            yErrors = []

        self.plotType = plotType

        self.xValues = xValues
        self.yValues = yValues

        self.xTickLabels = xTickLabels
        self.yTickLabels = yTickLabels
        self.xTickLabelPoints = xTickLabelPoints
        self.yTickLabelPoints = yTickLabelPoints
        self.xTickLabelProperties = xTickLabelProperties
        self.yTickLabelProperties = yTickLabelProperties

        self.label = label

        self.yMins = yMins
        self.yMaxes = yMaxes
        self.yErrors = yErrors

        self.autosort = autosort

        self.xLimits = xLimits

        self.picker = picker

    def __str__(self):
        return str(self.__dict__)

    def _preDraw(self):
        """
        The _preDraw function is called on all plot elements before drawing
        occurs. This allows various fields to be set in a structured way
        prior to actual drawing.
        """
        pass

    def setXTickLabelProperties(self, **propList):
        self._setTickLabelProperties(self.xTickLabelProperties, propList)

    def setYTickLabelProperties(self, **propList):
        self._setTickLabelProperties(self.yTickLabelProperties, propList)

    def _setTickLabelProperties(self, tickPropsDict, propList):
        for (key, val) in propList.items():
            tickPropsDict[key] = val

    def split(self, pieces):
        elements = []

        numXVals = len(self.xValues)

        valChunkSize = numXVals / pieces
        valChunkRemainder = numXVals % pieces

        for i in xrange(pieces):
            element = copy.deepcopy(self)

            if i < pieces - 1 or valChunkRemainder == 0:
                element.xValues = self.xValues[i * valChunkSize:(i+1) * valChunkSize]
                element.yValues = self.yValues[i * valChunkSize:(i+1) * valChunkSize]
            else:
                element.xValues = self.xValues[i * valChunkSize:]
                element.yValues = self.yValues[i * valChunkSize:]
            elements.append(element)
        return elements

    def getAttributes(self):
        kwdict = {}

        if self.picker is not None:
            kwdict['picker'] = self.picker

        return kwdict


    def draw(self, fig, axis):
        if len(self.xValues) > 0 and self.autosort:
            # This is a total kludge --AR

            sortAsymmetricErrorBars = len(self.yMins) > 0 or \
                len(self.yMaxes) > 0
            sortSymmetricErrorBars = len(self.yErrors) > 0

            if sortAsymmetricErrorBars:
                if len(self.yMins) != len(self.yValues):
                    warnings.warn("You don't have an error bar for every "
                                  "point, some points will be truncated")

                zipped = zip(self.xValues, self.yValues, self.yMins,
                             self.yMaxes)
                zipped.sort()
                self.xValues, self.yValues, self.yMins, self.yMaxes \
                    = zip(*zipped)
            elif sortSymmetricErrorBars:
                if len(self.yErrors) != len(self.yValues):
                    warnings.warn("You don't have an error bar for every "
                                  "point, some points will be truncated")

                zipped = zip(self.xValues, self.yValues, self.yErrors)
                zipped.sort()
                self.xValues, self.yValues, self.yErrors = zip(*zipped)
            else:
                zipped = zip(self.xValues, self.yValues)
                zipped.sort()
                self.xValues, self.yValues = zip(*zipped)

        if len(self.xTickLabels) > 0:
            if len(self.xTickLabelPoints) == 0:
                axis.set_xticks(self.xValues[0:len(self.xTickLabels)])
            else:
                axis.set_xticks(self.xTickLabelPoints)

            axis.set_xticklabels(self.xTickLabels, **self.xTickLabelProperties)

        if len(self.yTickLabels) > 0:
            if len(self.yTickLabelPoints) == 0:
                axis.set_yticks(self.yValues[0:len(self.yTickLabels)])
            else:
                axis.set_yticks(self.yTickLabelPoints)

            axis.set_yticklabels(self.yTickLabels, **self.yTickLabelProperties)

        self.drawErrorBars(axis)

    def drawErrorBars(self, axis, transform=None):
        errorBarKeywords = {}
        if hasattr(self, "ecolor") and self.ecolor is not None:
            errorBarKeywords["ecolor"] = self.ecolor
        elif hasattr(self, "color"):
            errorBarKeywords["ecolor"] = self.color

        if hasattr(self, "lineWidth"):
            errorBarKeywords["linewidth"] = self.lineWidth

        if hasattr(self, "lineStyle"):
            errorBarKeywords["linestyle"] = self.lineStyle

        if transform:
            errorBarKeywords['transform'] = transform + axis.transData

        errorBarKeywords["fmt"] = None

        if len(self.yMins) > 0 and len(self.yMaxes) > 0:
            numYVals = len(self.yValues)
            yMin = [self.yValues[i] - self.yMins[i] for i in xrange(numYVals)]
            yMax = [self.yMaxes[i] - self.yValues[i] for i in xrange(numYVals)]


            errorBarKeywords["yerr"] = [yMin, yMax]

            axis.errorbar(self.xValues, self.yValues, **errorBarKeywords)
        elif len(self.yErrors) > 0:
            errorBarKeywords["yerr"] = self.yErrors
            axis.errorbar(self.xValues, self.yValues, **errorBarKeywords)

# EOF
