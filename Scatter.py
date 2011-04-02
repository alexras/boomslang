import pylab
from matplotlib import pyplot
from PlotInfo import *
from Marker import Marker

class Scatter(PlotInfo):
    def __init__(self,
                 marker='o',
                 markerSize=20,
                 color="black", **kwargs):
        super(Scatter,self).__init__("scatter", **kwargs)
        self._marker = Marker()
        self._marker.marker = marker
        self._marker.size = markerSize
        self.color = color

    @property
    def marker(self):
        return self._marker.marker

    @marker.setter
    def marker(self, value):
        self._marker.marker = value

    @marker.getter
    def marker(self):
        return self._marker.marker

    @property
    def markerSize(self):
        return self._marker.size

    @markerSize.setter
    def markerSize(self, value):
        self._marker.size = value

    @markerSize.getter
    def markerSize(self):
        return self._marker.size

    def draw(self, axis):
        kwdict = {}
        kwdict["marker"] = self.marker
        kwdict["label"] = self.label
        kwdict["color"] = self.color
        kwdict["s"] = self.markerSize

        return [[axis.scatter(self.xValues, self.yValues, **kwdict)],
                [self.label]]

