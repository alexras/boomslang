import pylab
from matplotlib import pyplot
from PlotInfo import *

class Scatter(PlotInfo):
    def __init__(self,
                 marker='o',
                 markerSize=20,
                 color="black", **kwargs):
        super(Scatter,self).__init__("scatter", **kwargs)
        self.marker = marker
        self.markerSize = markerSize
        self.color = color

    def draw(self, axis):
        kwdict = {}
        kwdict["marker"] = self.marker
        kwdict["label"] = self.label
        kwdict["color"] = self.color
        kwdict["s"] = self.markerSize

        return [[axis.scatter(self.xValues, self.yValues, **kwdict)],
                [self.label]]

