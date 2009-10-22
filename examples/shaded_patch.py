#!/usr/bin/env python
from boomslang import Plot, ShadedRegion, Line

line = Line()
line.xValues = [1, 5]
line.yValues = [2, 9]

region = ShadedRegion()
region.xValues = [1, 9, 9, 1]
region.yValues = [1, 1, 9, 9]
region.color = "red"

plot = Plot()
plot.add(region)
plot.add(line)

plot.plot()
