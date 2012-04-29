import itertools
from matplotlib import pyplot
from PlotInfo import PlotInfo
from Marker import Marker
from LineStyle import LineStyle

class VLine(PlotInfo):
    def __init__(self,
                 marker = None,
                 markerSize = 8.0,
                 width = 1.0,
                 color = 'black',
                 lineStyle = '-',
                 dates = False,
                 **kwargs):
        super(VLine,self).__init__("vline", **kwargs)

        self._marker = Marker()
        self._marker.marker = marker
        self._marker.size = markerSize
        self.width = width
        self.color = color
        self._lineStyle = LineStyle()
        self._lineStyle.style = lineStyle
        self.dates = dates

    @property
    def lineStyle(self):
        return self._lineStyle.style

    @lineStyle.setter
    def lineStyle(self, value):
        self._lineStyle.style = value

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

    def draw(self, fig, axis, transform=None):
        # Present to keep the PlotInfo sorting from failing
        self.yValues = list(itertools.repeat(0, len(self.xValues)))

        PlotInfo.draw(self, fig, axis)

        kwdict = self.getAttributes()
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.width

        return [[axis.axvline(x=xValue, **kwdict)
                    for xValue in self.xValues],
                [self.label for xValue in self.xValues]]
