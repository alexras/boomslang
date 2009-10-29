#!/usr/bin/env python

from boomslang import Line, Plot

plot = Plot()

for i in xrange(6):
    line = Line()
    line.xValues = xrange(5)
    line.yValues = [(i+1) * x for x in line.xValues]
    line.label = "Line %d" % (i + 1)
    plot.add(line)

plot.addLineColor("red")
plot.addLineColor("blue")
plot.addLineStyle("-")
plot.addLineStyle("--")
plot.addLineStyle(":")
plot.hasLegend(columns=2)
plot.save("linestyles.png")
