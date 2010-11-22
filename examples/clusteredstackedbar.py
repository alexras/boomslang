#!/usr/bin/env python
from boomslang import ClusteredBars, StackedBars, Bar, Plot
from random import uniform

cluster = ClusteredBars()

colors = ['red','green','blue','CornflowerBlue','LightSalmon']
for i in xrange(5):
    stack = StackedBars()

    for j in xrange(5):
        bar = Bar()
        bar.xValues = range(5)
        bar.yValues = [uniform(1,3*x) for x in bar.xValues]
        bar.color = colors[j]
        bar.label = "Subject %d" % (j+1,)

        stack.add(bar)
    cluster.add(stack)

cluster.spacing = 0.5
cluster.xTickLabels = ["1", "2", "3", "4", "5"]

plot = Plot()
plot.add(cluster)
plot.hasLegend()
plot.setXLabel('Nested Cars')
plot.setYLabel('Party (lampshades)')
plot.save("clusteredstackedbar.png")
