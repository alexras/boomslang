import pylab
from matplotlib import pyplot
from PlotInfo import PlotInfo

class VLine(PlotInfo):
    def __init__(self):
        super(VLine,self).__init__("vline")
        
        self.marker = None
        self.markerSize = 8.0
        # TODO Change to width
        self.lineWidth = 1
        self.color = 'black'
        self.lineStyle = '-'
        self.dates = False

    def draw(self, axis):
        # Present to keep the PlotInfo sorting from failing
        self.yValues = [0 for x in self.xValues]

        PlotInfo.draw(self, axis)

        kwdict = {}
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.lineWidth

        return [[axis.axvline(x=xValue, **kwdict)
                    for xValue in self.xValues],
                [self.label for xValue in self.xValues]]
