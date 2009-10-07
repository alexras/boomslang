#!/usr/bin/env python

from boomslang import Bar, Plot

bar = Bar()

bar.xValues = range(5)
bar.yValues = [2, 4, 6, 8, 10]
# Valid values include all marker types, /, //, \, \\
bar.hatch = r"\\"
bar.color="red"
bar.edgeColor="black"

plot = Plot()
plot.add(bar)
plot.save("hatchedbars.png")
