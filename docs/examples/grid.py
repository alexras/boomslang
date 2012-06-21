plot = Plot()

line = Line()
line.yValues = [25, 40, 30, 23, 10, 50]
line.xValues = range(len(line.yValues))

plot.add(line)
plot.xLabel = "X Label"
plot.yLabel = "Y Label"
plot.yLimits = (0, 60)

plot.grid = True

plot.save("grid.png")
