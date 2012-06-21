from matplotlib import pyplot
from PlotInfo import PlotInfo
from StepType import StepType
import warnings
from Marker import Marker
from LineStyle import LineStyle

class Line(PlotInfo):
    """
    A plot element that represents a line in two-dimensional space
    """

    _steps = StepType("steps")

    def __init__(self,
                 color='black',
                 width=1,
                 lineStyle='-',
                 marker=None,
                 markerSize=8.0,
                 dates=False,
                 loglog=False,
                 steps=None,
                 alpha=None,
                 antialiased=False,
                 **kwargs
                ):
        super(Line,self).__init__("line", **kwargs)

        self._marker = Marker()
        self._marker.marker = marker
        self._marker.size = markerSize

        # TODO Change to width
        self.lineWidth = width
        """
        The line's width
        """

        self.color = color
        """
        The line's color. see :ref:`styling-colors` for valid colors.
        """

        self._lineStyle = LineStyle()
        self._lineStyle.style = lineStyle

        self.dates = dates
        """
        If True, the x-axis values of this line will be interpreted as dates
        """

        self.loglog = loglog

        self.steps = steps

        self.alpha = alpha

        self.antialiased = antialiased
        """
        If True, the line will be anti-aliased, removing jagged edges in some
        output formats
        """

    @property
    def steps(self):
        """
        If not None, the line will be plotted as a step function. If "pre",
        each point comes before a step. If "mid", each point is in the middle
        of a step. If "post", each point comes after a step.
        """
        return self._steps

    @steps.setter
    def steps(self, val):
        self._steps = val

    @property
    def lineStyle(self):
        """
        The line's style. See :ref:`styling-lines` for more information about
        available line styles.
        """
        return self._lineStyle.style

    @lineStyle.setter
    def lineStyle(self, value):
        self._lineStyle.style = value

    @property
    def marker(self):
        """
        The marker used to mark points on the line. See :ref:`styling-markers`
        for more information on avialable marker types.
        """

        return self._marker.marker

    @marker.setter
    def marker(self, value):
        self._marker.marker = value

    @property
    def markerSize(self):
        """
        The size of the markers used to mark points on the line.
        """

        return self._marker.size

    @markerSize.setter
    def markerSize(self, value):
        self._marker.size = value

    def stepFunction(self, stepType="pre"):
        self.steps = stepType

    def draw(self, fig, axis, transform=None):
        super(Line, self).draw(fig, axis)

        if self.dates:
            plotFunc = axis.plot_date
        elif self.loglog:
            warnings.warn("Setting loglog in Lines will be deprecated soon. "
                          "Set this in Plot instead.",
                          PendingDeprecationWarning)
            plotFunc = axis.loglog
        else:
            plotFunc = axis.plot

        kwdict = self.getAttributes()
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.lineWidth

        if self.steps is not None:
            kwdict["drawstyle"] = "steps-%s" % (self.steps)

        if self.marker is not None:
            kwdict["marker"] = self.marker
            kwdict["markersize"] = self.markerSize
        else:
            kwdict["marker"] = "None"

        if self.antialiased:
            kwdict["antialiased"] = self.antialiased
        if self.alpha is not None:
            kwdict["alpha"] = self.alpha

        handle = plotFunc(self.xValues, self.yValues, **kwdict)

        if type(handle) == list:
            handle = handle[0]

        return [[handle], [self.label]]
