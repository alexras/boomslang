#!/usr/bin/env python
import random
from boomslang import Scatter, Plot

scatter = Scatter()
scatter.label="Hooray dots!"

for i in range(100):
    scatter.xValues.append(random.uniform(0, 10))
    scatter.yValues.append(random.uniform(0, 10))

plot = Plot()
plot.hasLegend()
plot.add(scatter)
plot.save("scatter.png")
