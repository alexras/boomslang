import pylab
from matplotlib import pyplot
from PlotInfo import *

class Scatter(PlotInfo):
    def __init__(self):
        PlotInfo.__init__(self, "scatter")
        self.marker = 'o'
        self.color = "black"
            
    def draw(self, axis):
        kwdict = {}
        kwdict["marker"] = self.marker
        kwdict["label"] = self.label
        kwdict["color"] = self.color

        return [[axis.scatter(self.xValues, self.yValues, **kwdict)], 
                [self.label]]
    
