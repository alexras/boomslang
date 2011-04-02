import pylab
from matplotlib import pyplot
from PlotInfo import PlotInfo
from StepType import StepType
import warnings

class Line(PlotInfo):
    steps = StepType("steps")

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

        self.marker = marker
        self.markerSize = markerSize
        # TODO Change to width
        self.lineWidth = width
        self.color = color
        self.lineStyle = lineStyle
        self.dates = dates
        self.loglog = loglog
        self.steps = steps

        self.alpha = alpha
        self.antialiased = antialiased

    def stepFunction(self, stepType="pre"):
        self.steps = stepType

    def draw(self, axis):
        super(Line, self).draw(axis)

        if self.dates:
            plotFunc = axis.plot_date
        elif self.loglog:
            warnings.warn("Setting loglog in Lines will be deprecated soon. "
                          "Set this in Plot instead.",
                          warnings.PendingDeprecationWarning)
            plotFunc = axis.loglog
        else:
            plotFunc = axis.plot

        kwdict = {}
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

        return [[plotFunc(self.xValues, self.yValues, **kwdict)], [self.label]]
