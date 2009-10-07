import pylab
from matplotlib import pyplot
from PlotInfo import PlotInfo

class Line(PlotInfo):
    def __init__(self):
        PlotInfo.__init__(self, "line")
        
        self.marker = None
        self.markerSize = 8.0
        self.lineWidth = 1
        self.color = 'black'
        self.lineStyle = '-'
        self.dates = False

    def draw(self, axis):
        PlotInfo.draw(self, axis)
        
        if self.dates:
            plotFunc = axis.plot_date
        else:
            plotFunc = axis.plot

        kwdict = {}
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.lineWidth

        if self.marker is not None:
            kwdict["marker"] = self.marker
            kwdict["markersize"] = self.markerSize

        return [[plotFunc(self.xValues, self.yValues, **kwdict)], [self.label]]
