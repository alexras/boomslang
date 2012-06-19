import itertools
from matplotlib import pyplot
from PlotInfo import PlotInfo
from Marker import Marker
from LineStyle import LineStyle

class HLine(PlotInfo):
    """
    A plot element that represents a horizontal line that passes through a
    given point on the y-axis.
    """

    def __init__(self,
                 marker = None,
                 markerSize = 8.0,
                 width = 1.0,
                 color = 'black',
                 lineStyle = '-',
                 dates = False,
                 **kwargs):
        super(HLine,self).__init__("hline", **kwargs)

        self._marker = Marker()
        self._marker.marker = marker
        self._marker.size = markerSize

        self.width = width
        """
        The line's width
        """

        self.color = color
        """
        The line's color. See :ref:`styling-colors` for valid colors.
        """

        self._lineStyle = LineStyle()
        self._lineStyle.style = lineStyle

        self.dates = dates

    @property
    def lineStyle(self):
        """
        The line style for this line; see :ref:`styling-lines` for more
        information about available line styles.
        """

        return self._lineStyle.style

    @lineStyle.setter
    def lineStyle(self, value):
        self._lineStyle.style = value

    @property
    def marker(self):
        """
        The marker used to mark points on the line. See :ref:`styling-markers`
        for more information about available markers.
        """
        return self._marker.marker

    @marker.setter
    def marker(self, value):
        self._marker.marker = value

    @property
    def markerSize(self):
        """
        The size of this line's markers.
        """
        return self._marker.size

    @markerSize.setter
    def markerSize(self, value):
        self._marker.size = value

    def draw(self, fig, axis, transform=None):
        # Present to keep the PlotInfo sorting from failing
        self.xValues = list(itertools.repeat(0, len(self.yValues)))

        PlotInfo.draw(self, fig, axis, transform)

        kwdict = self.getAttributes()
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.width

        return [[axis.axhline(y=yValue, **kwdict)
                    for yValue in self.yValues],
                [self.label for yValue in self.yValues]]
