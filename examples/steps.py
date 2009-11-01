#!/usr/bin/env python
from boomslang import Line, Plot, PlotLayout

xVals = [1, 2, 3, 4, 5]
yVals = [1, 2, 3, 4, 5]

def generatePlot(stepType):
    line = Line()
    line.xValues = xVals
    line.yValues = yVals
    line.marker = 'o'
    line.stepFunction(stepType)
    
    plot = Plot()
    plot.add(line)
    plot.setTitle(r'"%s" Steps' % (stepType))
    plot.setXLimits(0, 6)
    plot.setYLimits(0, 6)
    
    return plot

prePlot = generatePlot("pre")
midPlot = generatePlot("mid")
postPlot = generatePlot("post")

layout = PlotLayout()
layout.width = 3
layout.addPlot(prePlot)
layout.addPlot(midPlot)
layout.addPlot(postPlot)
layout.setPlotParameters(right=0.96, left=0.04)
layout.save("steps.png")
