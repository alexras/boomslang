#!/usr/bin/env python
import random
from boomslang import Scatter, Plot, VLine

scatter = Scatter()
scatter.label="Hooray dots with vlines!"

for i in range(100):
    scatter.xValues.append(random.uniform(0, 10))
    scatter.yValues.append(random.uniform(0, 10))

vline1 = VLine()
vline1.xValues = [2,8]
vline1.color = 'CornflowerBlue'

vline2 = VLine()
vline2.xValues = [1,9]
vline2.color = 'GoldenRod'

plot = Plot()
plot.hasLegend()
plot.add(scatter)
plot.add(vline1)
plot.add(vline2)
plot.save("vline.png")
