#!/usr/bin/env python

from boomslang import Line, Plot, PlotLayout

lines = []

for i in xrange(3):
    line = Line()
    line.xValues = xrange(5)
    line.yValues = [(i+1 / 2.0) *  pow(x, i+1) for x in line.xValues]
    line.label = "Line %d" % (i + 1)
    lines.append(line)

plot = Plot()
plot.add(lines[0])

inset = Plot()
inset.add(lines[1])
inset.hideTickLabels()
inset.setTitle("Inset in Yo Inset\nSo You Can Inset\nWhile You Inset")

insideInset = Plot()
insideInset.hideTickLabels()
insideInset.add(lines[2])

inset.addInset(insideInset, width=0.4, height=0.3, location="upper left")

plot.addInset(inset, width=0.4, height=0.4, location="lower right")

plot.save("inset.png")
