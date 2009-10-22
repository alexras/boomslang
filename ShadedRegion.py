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
        argsDict["color"] = self.color
        
        poly = matplotlib.patches.Polygon(zip(self.xValues, self.yValues), 
                                          **argsDict)
        
        return [[axis.add_patch(poly)], [self.label]]
