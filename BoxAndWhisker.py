from matplotlib import pyplot
from PlotInfo import *
from Marker import Marker

class BoxAndWhisker(PlotInfo):
    """
    Box and whisker plots
    """

    def __init__(self):
        super(BoxAndWhisker,self).__init__("boxplot")
        self.width=None
        self.color="black"
        self.label = None
        self.xSequence = []
        self.flierMarker = Marker()
        self.flierMarker.marker = '+'
        self.flierMarker.color = 'b'

    def draw(self, fig, axis, transform=None):
        # To be compatible with PlotInfo assumptions
        self.xValues = range(1,len(self.xSequence)+1)
        self.yValues = [0 for x in self.xValues]

        super(BoxAndWhisker,self).draw(fig, axis)

        kwdict = {}

        if self.flierMarker.marker is not None:
            kwdict["sym"] = self.flierMarker.marker
        else:
            kwdict["sym"] = ''

        plotHandles = axis.boxplot(self.xSequence, **kwdict)

        # Picking which part of the plot to use in the legend may
        # require more thought as there are multiple lines in the
        # boxplot, as well as the possibility for outliers.
        # Options are ['medians', 'fliers', 'whiskers', 'boxes', 'caps']
        return [plotHandles['medians'], [self.label]]
