from matplotlib import pyplot
from PlotInfo import PlotInfo
from Marker import Marker

class Label(PlotInfo):
    """
    Labels a point on the plot with text and/or arrows
    """

    def __init__(self, x, y, text=None, bbox=None):
        PlotInfo.__init__(self, "label")

        self.x = x
        """
        The label's x coordinate
        """

        self.y = y
        """
        The label's y coordinate
        """

        self.text = text
        """
        The text that should be displayed with the label
        """

        self.textX = x
        """
        The x coordinate at which the text for the label should be drawn
        """

        self.textY = y
        """
        The y coordinate at which the text for the label should be drawn
        """

        self.arrow = None

        self._marker = Marker()

        self.rotation = None

        if bbox:
            self.bbox = dict(bbox)
        else:
            self.bbox = None

    @property
    def marker(self):
        """
        The marker type that should be used to mark the labeled point
        """
        return self._marker.marker

    @marker.setter
    def marker(self, value):
        self._marker.marker = value

    def setTextOffset(self, x, y):
        self.textX = self.x + x
        self.textY = self.y + y

    def setTextPosition(self, x, y):
        self.textX = x
        self.textY = y

    def hasArrow(self, style="->", color="black"):
        """
        Defines an arrow between the label's text and its point. Valid arrow
        styles are given in `Matplotlib's documentation <http://matplotlib.github.com/users/annotations_guide.html?highlight=arrowprops#annotating-with-arrow>`_.
        """

        self.arrow = dict(facecolor=color, arrowstyle=style)

    def draw(self, fig, axis, transform=None):
        kwdict = {}
        kwdict["xytext"] = (self.textX, self.textY)
        kwdict["xycoords"] = "data"
        kwdict["textcoords"] = "data"
        kwdict["arrowprops"] = self.arrow
        kwdict["horizontalalignment"] = "center"
        kwdict["rotation"] = self.rotation

        # For props, see
        # http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.patches.Rectangle
        if self.bbox: kwdict["bbox"] = self.bbox

        handles = []
        labels = []

        handles.append(axis.annotate(self.text, (self.x, self.y), **kwdict))
        labels.append(None)

        if self.marker is not None:
            handles.append(axis.scatter([self.x],[self.y],marker=self.marker,
                                        color="black"))
            labels.append(None)

        return [handles, labels]
