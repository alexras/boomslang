#!/usr/bin/env python
from boomslang import Bar, ClusteredBars, Plot

bar1 = Bar()
bar1.xValues = range(5)
bar1.yValues = [2, 4, 6, 8, 10]
bar1.color = "red"
bar1.label = "Red Cluster"

bar2 = Bar()
bar2.xValues = range(5)
bar2.yValues = [3, 12, 4, 8, 14]
bar2.color = "blue"
bar2.label = "Blue Cluster"

bar3 = Bar()
bar3.xValues = range(5)
bar3.yValues = [1, 6, 9, 13, 20]
bar3.color = "green"
bar3.label = "Green Cluster"

clusteredBars = ClusteredBars()

clusteredBars.add(bar1)
clusteredBars.add(bar2)
clusteredBars.add(bar3)
clusteredBars.spacing = 0.5

clusteredBars.xTickLabels = ["A", "B", "C", "D", "E"]

plot = Plot()
plot.add(clusteredBars)
plot.hasLegend()

plot.save("clusteredbars.png")
