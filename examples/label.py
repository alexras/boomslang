#!/usr/bin/env python

from boomslang import Label, Line, Plot
import numpy

line = Line()
line.xValues = numpy.arange(0.0, 5.0, 0.01)
line.yValues = numpy.cos(2 * numpy.pi * line.xValues)

maxLabel = Label(2, 1, "Maximum!")
maxLabel.setTextOffset(0.5, 0.5)
maxLabel.hasArrow()

minLabel = Label(1.5, -1, "Minimum!")
minLabel.setTextPosition(1, -2)
minLabel.hasArrow()

randomLabel = Label(2, -1.7, "A Point!")
randomLabel.setTextOffset(0, 0.2)
randomLabel.marker = 'o'

plot = Plot()
plot.add(line)
plot.add(minLabel)
plot.add(maxLabel)
plot.add(randomLabel)
plot.setYLimits(-3, 3)
plot.setXLabel("X")
plot.setYLabel("cos(x)")
plot.save("label.png")
