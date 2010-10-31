#!/usr/bin/env python
import random
from boomslang import BoxAndWhisker, Plot

bnw = BoxAndWhisker()
bnw.label="Whiskers"

xSequence = []

for i in range(10):
    xSequence.append([random.uniform(1,i*10) for x in range(100)])

bnw.xSequence = xSequence

plot = Plot()
plot.hasLegend()
plot.add(bnw)
plot.save("boxandwhisker.png")
