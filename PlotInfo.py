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
                 errorBarColor = None,
                 errorBarLineWidth = None,
                 errorBarCapsize = None,
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

        if yMins is None:
            yMins = []

        if yMaxes is None:
            yMaxes = []

        if yErrors is None:
            yErrors = []

        self.plotType = plotType
        """
        Names the type of plot element
        """

        self.xValues = xValues
        """
        An array of x-axis values for the plot element
        """

        self.yValues = yValues
        """
        An array of y-axis values for the plot elements
        """

        self.xTickLabels = xTickLabels
        """
        A list of labels that should be drawn on the x-axis
        """

        self.yTickLabels = yTickLabels
        """
        A list of labels that should be drawn on the y-axis
        """

        self.xTickLabelPoints = xTickLabelPoints
        """
        The locations on the x-axis where the labels in :attr:`xTickLabels`
        should be drawn
        """

        self.yTickLabelPoints = yTickLabelPoints
        """
        The locations on the x-axis where the labels in :attr:`xTickLabels`
        should be drawn
        """

        self._xTickLabelProperties = LabelProperties()

        self._yTickLabelProperties = LabelProperties()

        if xTickLabelProperties is not None:
            self.xTickLabelProperties = xTickLabelProperties

        if yTickLabelProperties is not None:
            self.yTickLabelProperties = yTickLabelProperties

        self.label = label
        """
        A string used to label this plot element in a legend
        """

        self.yMins = yMins
        """
        For asymmetric error bars, a list of locations for the bottoms of this
        plot element's error bars
        """

        self.yMaxes = yMaxes
        """
        For asymmetric error bars, a list of locations for the tops of this
        plot element's error bars
        """

        self.yErrors = yErrors
        """
        For symmetric error bars, a list of error bar widths for this plot
        element's error bars
        """

        self.autosort = autosort
        """
        If true, x/y pairs in :py:attr:`xValues` and :py:attr:`yValues` are
        sorted by x value before the plot is rendered
        """

        self.xLimits = xLimits

        self.errorBarColor = errorBarColor
        self.errorBarLineWidth = errorBarLineWidth
        self.errorBarCapsize = errorBarCapsize

        self.picker = picker

    @property
    def xTickLabelProperties(self):
        """
        A dictionary of properties that control the appearance of the X axis'
        tick labels. See :ref:`styling-labels` for more information on which
        properties can be set.
        """

        return self._xTickLabelProperties

    @xTickLabelProperties.setter
    def xTickLabelProperties(self, **props):
        self._xTickLabelProperties.update(props)

    @xTickLabelProperties.setter
    def xTickLabelProperties(self, propsobj):
        self._xTickLabelProperties.update(propsobj)


    @property
    def yTickLabelProperties(self):
        """
        A dictionary of properties that control the appearance of the Y axis'
        tick labels. See :ref:`styling-labels` for more information on which
        properties can be set.
        """

        return self._yTickLabelProperties

    @yTickLabelProperties.setter
    def yTickLabelProperties(self, props):
        self._yTickLabelProperties.update(props)

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
        # Deprecated: use xTickLabelProperties field instead
        self._xTickLabelProperties.update(propList)

    def setYTickLabelProperties(self, **propList):
        # Deprecated: use yTickLabelProperties field instead
        self._yTickLabelProperties.update(propList)

    def split(self, pieces):
        """
        Split this plot element into `pieces` separate plot elements, each of
        which is responsible for a disjoint range of the original plot
        element's x-axis. This is useful for situations where a plot element
        cannot fit comfortably in a single plot.
        """
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
        """
        Get the attributes dictionary used to style the plot element. Extending
        this method allows plot elements to inherit attributes.
        """

        kwdict = {}

        if self.picker is not None:
            kwdict['picker'] = self.picker

        return kwdict


    def draw(self, fig, axis, transform=None):
        """
        The base method for drawing a plot element on the axis `axis` within
        the figure `fig`. Other plot elements should override this method, but
        should also be sure to call this method before doing any
        element-specific processing.
        """

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
        """
        Draw error bars for the plot element using the plot element's
        `yMins`/`yMaxes` or `yErrors`. If `yMins` or `yMaxes` have non-zero
        length, they are used to draw error bars that can be
        asymmetric. Otherwise, `yErrors` are used to draw symmetric error bars.

        If some transform should be applied to the error bars, it is provided
        by the caller with the `transform` parameter.
        """

        errorBarKeywords = {}
        if  self.errorBarColor is not None:
            errorBarKeywords["ecolor"] = self.errorBarColor
        elif hasattr(self, "color"):
            errorBarKeywords["ecolor"] = self.color

        if self.errorBarCapsize is not None:
            errorBarKeywords["capsize"] = self.errorBarCapsize

        if self.errorBarLineWidth is not None:
            errorBarKeywords["linewidth"] = self.errorBarLineWidth

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

