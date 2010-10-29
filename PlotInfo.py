import os
import sys
import copy

class PlotInfo(object):
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
        
        self.yMins = []
        self.yMaxes = []
        self.yErrors = []
        
        self.autosort = True

        self.xLimits = None
        
    def __str__(self):
        return str(self.__dict__)
    
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
        if len(self.xValues) > 0 and self.autosort:
            # This is a total kludge --AR
            
            sortAsymmetricErrorBars = len(self.yMins) > 0 or \
                len(self.yMaxes) > 0
            sortSymmetricErrorBars = len(self.yErrors) > 0

            if sortAsymmetricErrorBars:
                if len(self.yMins) != len(self.yValues):
                    print >>sys.stderr, "You don't have an error bar for every point, some points will be truncated"

                zipped = zip(self.xValues, self.yValues, self.yMins, 
                             self.yMaxes)
                zipped.sort()
                self.xValues, self.yValues, self.yMins, self.yMaxes \
                    = zip(*zipped)
            elif sortSymmetricErrorBars:
                if len(self.yErrors) != len(self.yValues):
                    print >>sys.stderr, "You don't have an error bar for every point, some points will be truncated"

                zipped = zip(self.xValues, self.yValues, self.yErrors)
                zipped.sort()
                self.xValues, self.yValues, self.yErrors = zip(*zipped)
            else:
                zipped = zip(self.xValues, self.yValues)
                zipped.sort()
                self.xValues, self.yValues = zip(*zipped)
        
        if self.xTickLabels is not None:
            if self.xTickLabelPoints is None:
                axis.set_xticks(self.xValues[0:len(self.xTickLabels)])
            else:
                axis.set_xticks(self.xTickLabelPoints)
            
            axis.set_xticklabels(self.xTickLabels, **self.xTickLabelProperties)
        
        if self.yTickLabels is not None:
            if self.yTickLabelPoints is None:
                axis.set_yticks(self.yValues[0:len(self.yTickLabels)])
            else:
                axis.set_yticks(self.yTickLabelPoints)

            axis.set_yticklabels(self.yTickLabels, **self.yTickLabelProperties)

        self.drawErrorBars(axis)

    def drawErrorBars(self, axis, transform=None):
        errorBarKeywords = {}
        if hasattr(self, "ecolor"):
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
