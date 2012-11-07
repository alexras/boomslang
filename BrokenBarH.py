from matplotlib import pyplot
from PlotInfo import PlotInfo

class BrokenBarH(PlotInfo):
    """
    A plot element that represents a collection of horizontal bars spanning a
    sequence of [xMin, xMax] ranges at a given y.
    """

    def __init__(self,
                 y=None,
                 xMins = [],
                 xWidths = [],
                 yWidth=0.6,
                 linewidth=1.0,
                 color="black",
                 edgeColor=None,
                 **kwargs):
        super(BrokenBarH,self).__init__("broken barh", **kwargs)

        self.y = y
        """
        The y coordinate for this collection of horizontal bars
        """

        self.xMins = xMins
        """
        A list of locations for the start xValues of the horizontal bars
        """

        self.xWidths = xWidths
        """
        A list of widths of the horizontal bars
        """

        self.yWidth = yWidth
        """
        The bar's width along the y axis
        """

        self.linewidth = linewidth
        """
        The width of the line that borders the bars
        """

        self.color = color
        """
        The bar's color. See :ref:`styling-colors` for valid colors.
        """

        self.edgeColor = edgeColor
        """
        The color of the line that borders the bars
        """

    def draw(self, fig, axis, transform=None):
        # Draw only if we have a valid y value for the horizontal bars
        if self.y is None:
            return [[], []]

        xranges = [(self.xMins[i], self.xWidths[i]) for i in xrange(len(self.xMins))]
        yrange = (self.y - 0.5 * self.yWidth, self.yWidth)

        kwdict = self.getAttributes()
        kwdict["linewidth"] = self.linewidth
        kwdict["edgecolor"] = self.edgeColor
        kwdict["facecolors"] = self.color
        kwdict["label"] = self.label

        return [[axis.broken_barh(xranges, yrange, **kwdict)], [self.label]]
