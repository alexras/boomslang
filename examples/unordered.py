#!/usr/bin/env python

from boomslang import Plot, Line

line = Line()
line.xValues = [2, 1, 3, 4, 0]
line.yValues = [2, 1, 3, 4, 0]

plot = Plot()
plot.add(line)

plot.save("unordered.png")

