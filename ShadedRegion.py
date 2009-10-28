import pylab
import matplotlib
from PlotInfo import PlotInfo

class ShadedRegion(PlotInfo):
    def __init__(self):
        PlotInfo.__init__(self, "shaded region")
        
        self.color = "gray"
        self.label = None
    def draw(self, axis):
        PlotInfo.draw(self, axis)

        argsDict = {}
        argsDict["facecolor"] = self.color
        argsDict["edgecolor"] = self.color
        argsDict["alpha"] = 0.5
        
        lowerLeft = (min(self.xValues), min(self.yValues))
        height = max(self.yValues) - min(self.yValues)
        width = max(self.xValues) - min(self.xValues)
        
        poly = matplotlib.patches.Rectangle(lowerLeft, width, height,
                                          **argsDict)
        
        return [[axis.add_patch(poly)], [self.label]]
