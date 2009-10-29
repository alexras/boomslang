#!/usr/bin/env python

from boomslang import Line, Plot

plot = Plot()

line = Line()
line.yValues = [25, 40, 30, 23, 10, 50]
line.xValues = range(len(line.yValues))

plot.add(line)
plot.setXLabel("X Label")
plot.setYLabel("Y Label")
plot.setYLimits(0, 60)

plot.save("simpleline.png")
