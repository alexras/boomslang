import pylab
from matplotlib import pyplot
from PlotInfo import PlotInfo

class Line(PlotInfo):
    def __init__(self):
        PlotInfo.__init__(self, "line")
        
        self.marker = None
        self.markerSize = 8.0
        # TODO Change to width
        self.lineWidth = 1
        self.color = 'black'
        self.lineStyle = '-'
        self.dates = False
        self.loglog = False
        self.steps = None

    def stepFunction(self, stepType="pre"):
        validStepTypes = ["pre", "mid", "post"]
        
        if stepType not in validStepTypes:
            print >>sys.stderr, "%s is not a valid step type. Valid step types are %s" % (stepType, ", ".join(validStepTypes))
            sys.exit(1)
        
        self.steps = stepType

    def draw(self, axis):
        PlotInfo.draw(self, axis)
        
        if self.dates:
            plotFunc = axis.plot_date
        elif self.loglog:
            plotFunc = axis.loglog
        else:
            plotFunc = axis.plot

        kwdict = {}
        kwdict["linestyle"] = self.lineStyle
        kwdict["color"] = self.color
        kwdict["label"] = self.label
        kwdict["linewidth"] = self.lineWidth
        
        if self.steps is not None:
            kwdict["drawstyle"] = "steps-%s" % (self.steps)
        
        if self.marker is not None:
            kwdict["marker"] = self.marker
            kwdict["markersize"] = self.markerSize
        else:
            kwdict["marker"] = "None"
        
        return [[plotFunc(self.xValues, self.yValues, **kwdict)], [self.label]]
