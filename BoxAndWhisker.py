from matplotlib import pyplot
from PlotInfo import *
from Marker import Marker

class BoxAndWhisker(PlotInfo):
    """
    A modified box-and-whisker plot.
    """

    def __init__(self):
        super(BoxAndWhisker,self).__init__("boxplot")

        self.width=None
        """
        The width of each of the element's "boxes".
        """

        self.color="black"

        self.label = None

        self.xSequence = []
        """
        A list of lists defining the values to be plotted. Each list gives a
        set of y-axis values. The first list gives the values for x=0, the
        second for x=1, and so on.
        """

        #TODO Document
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
