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
        """
        The color of points in the scatter plot. See :ref:`styling-colors` for
        valid colors.
        """

    @property
    def marker(self):
        """
        The marker type used to mark points in the scatter plot. See
        :ref:`styling-markers` for valid marker types.
        """
        return self._marker.marker

    @marker.setter
    def marker(self, value):
        self._marker.marker = value

    @property
    def markerSize(self):
        """
        The size of the scatter plot's markers.
        """
        return self._marker.size

    @markerSize.setter
    def markerSize(self, value):
        self._marker.size = value

    def draw(self, fig, axis, transform = None):
        super(Scatter, self).draw(fig, axis)

        kwdict = self.getAttributes()
        kwdict["marker"] = self.marker
        kwdict["label"] = self.label
        kwdict["color"] = self.color
        kwdict["s"] = self.markerSize


        return [[axis.scatter(self.xValues, self.yValues, **kwdict)],
                [self.label]]

