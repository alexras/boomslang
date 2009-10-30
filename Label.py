import pylab
from matplotlib import pyplot
from PlotInfo import PlotInfo

class Label(PlotInfo):
    def __init__(self, x, y, text=None):
        PlotInfo.__init__(self, "label")
        
        self.x = x
        self.y = y
        self.text = text
        self.textX = x
        self.textY = y
        self.arrow = None
        self.marker = None

    def setTextOffset(self, x, y):
        self.textX = self.x + x
        self.textY = self.y + y

    def setTextPosition(self, x, y):
        self.textX = x
        self.textY = y

    def hasArrow(self, style="->", color="black"):
        self.arrow = dict(facecolor=color, arrowstyle=style)
    
    def draw(self, axis):
        kwdict = {}
        kwdict["xytext"] = (self.textX, self.textY)
        kwdict["xycoords"] = "data"
        kwdict["textcoords"] = "data"
        kwdict["arrowprops"] = self.arrow
        kwdict["horizontalalignment"] = "center"

        handles = []
        labels = []

        handles.append(axis.annotate(self.text, (self.x, self.y), **kwdict))
        labels.append(None)

        if self.marker is not None:
            handles.append(axis.scatter([self.x],[self.y],marker=self.marker, 
                                        color="black"))
            labels.append(None)

        return [handles, labels]
