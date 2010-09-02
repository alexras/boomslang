#!/usr/bin/env python

from boomslang import Line, Plot

plot = Plot()

for i in xrange(24):
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
plot.addMarker('')
plot.addMarker('x')
plot.addMarker('o')
plot.hasLegend(columns=2)
plot.setLegendLabelSize(8)
plot.save("linestyles.png")
