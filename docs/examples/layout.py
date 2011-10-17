line = Line()
line.xValues = range(5)
line.yValues = [2, 4, 6, 8, 10]

linePlot = Plot()
linePlot.add(line)
linePlot.setXLabel("X Data")
linePlot.setYLabel("Y Data")
linePlot.setTitle("Data as Line")

bar = Bar()
bar.xValues = range(5)
bar.yValues = [2, 4, 6, 8, 10]

barPlot = Plot()

barPlot.add(bar)
barPlot.setXLabel("X Data")
barPlot.setYLabel("Y Data")
barPlot.setTitle("Data as Bars")

scatter = Scatter()
scatter.xValues = range(5)
scatter.yValues = [2, 4, 6, 8, 10]

scatterPlot = Plot()
scatterPlot.add(scatter)
scatterPlot.setXLabel("X Data")
scatterPlot.setYLabel("Y Data")
scatterPlot.setTitle("Data as Points")

layout = PlotLayout()

layout.addPlot(linePlot, grouping="topRow")
layout.addPlot(barPlot, grouping="topRow")

layout.addPlot(scatterPlot)

# Set values similar to those given in the
# "Configure subplots" sliders in the
# interactive figure
layout.setPlotParameters(hspace=0.48)
layout.save("layout.png")
