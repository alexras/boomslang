#!/usr/bin/env python

from boomslang import Plot, Line, PlotLayout
import numpy

line = Line()
line.xValues = numpy.arange(0, 150, 0.01)
line.yValues = numpy.cos(.02 * numpy.pi * line.xValues)

plot = Plot()
plot.add(line)
plot.setXLimits(0, 150)
plot.setYLimits(-1, 1)
plot.setXLabel("X")
plot.setYLabel("cos(X)")
splitPlots = plot.split(2)

layout = PlotLayout()
layout.width = 2
layout.addPlot(plot, grouping="unsplit")

for s in splitPlots:
    layout.addPlot(s, grouping="splits")

layout.save("split.png")