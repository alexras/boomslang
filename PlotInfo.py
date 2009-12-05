import os
import sys
import copy

class PlotInfo:
    def __init__(self, plotType):
        self.plotType = plotType

        self.xValues = []
        self.yValues = []

        self.xTickLabels = None
        self.yTickLabels = None
        self.xTickLabelPoints = None
        self.yTickLabelPoints = None
        self.xTickLabelProperties = {}
        self.yTickLabelProperties = {}
        
        self.label = None

        self.yMins = None
        self.yMaxes = None
        self.yErrors = None
    
    def setXTickLabelProperties(self, **propList):
        self._setTickLabelProperties(self.xTickLabelProperties, propList)
        
    def setYTickLabelProperties(self, **propList):
        self._setTickLabelProperties(self.yTickLabelProperties, propList)
    
    def _setTickLabelProperties(self, tickPropsDict, propList):
        # Going to restrict the set of properties that can be modified so they
        # don't mess with the rest of the system
        
        validProperties = ["alpha", "backgroundColor", "color", \
            "horizontalalignment", "linespacing", "multialignment", \
            "rotation", "stretch", "style", 
            "verticalalignment", "weight"]
        
        for (key, val) in propList.items():
            if key not in validProperties:
                print >>sys.stderr, "Tick label property '%s' is not currently supported" % (key)
            else:
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
        
    def draw(self, axis):
        if len(self.xValues) > 0:
            zipped = zip(self.xValues, self.yValues)
            zipped.sort()
            self.xValues, self.yValues = zip(*zipped)
        
        if self.xTickLabels is not None:
            if self.xTickLabelPoints is None:
                axis.set_xticks(range(len(self.xTickLabels)))
            else:
                axis.set_xticks(self.xTickLabelPoints)
            
            axis.set_xticklabels(self.xTickLabels, **self.xTickLabelProperties)
        
        if self.yTickLabels is not None:
            if self.yTickLabelPoints is None:
                axis.set_yticks(range(len(self.yTickLabels)))
            else:
                axis.set_yticks(self.yTickLabelPoints)
            
            axis.set_yticklabels(self.yTickLabels, **self.yTickLabelProperties)

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
