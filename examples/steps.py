#!/usr/bin/env python
from boomslang import Line, Plot, PlotLayout

xVals = [1, 2, 3, 4, 5]
yVals = [1, 2, 3, 4, 5]

preStep = Line()
preStep.xValues = xVals
preStep.yValues = yVals
preStep.stepFunction("pre")
preStep.marker = 'x'

prePlot = Plot()
prePlot.add(preStep)
prePlot.setTitle(r'"pre" Steps')
prePlot.setXLimits(0, 6)
prePlot.setYLimits(0, 6)

midStep = Line()
midStep.xValues = xVals
midStep.yValues = yVals
midStep.stepFunction("mid")
midStep.marker = 'x'

midPlot = Plot()
midPlot.add(midStep)
midPlot.setTitle(r'"mid" Steps')
midPlot.setXLimits(0, 6)
midPlot.setYLimits(0, 6)


postStep = Line()
postStep.xValues = xVals
postStep.yValues = yVals
postStep.stepFunction("post")
postStep.marker = 'x'

postPlot = Plot()
postPlot.add(postStep)
postPlot.setTitle(r'"post" Steps')
postPlot.setXLimits(0, 6)
postPlot.setYLimits(0, 6)

layout = PlotLayout()
layout.width = 1
layout.addPlot(prePlot)
layout.addPlot(midPlot)
layout.addPlot(postPlot)
layout.setPlotParameters(top=0.96, bottom=0.04)
layout.save("steps.png")
