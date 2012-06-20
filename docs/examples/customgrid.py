plot = Plot()

line = Line()
line.yValues = [25, 40, 30, 23, 10, 50]
line.xValues = range(len(line.yValues))

plot.add(line)
plot.setXLabel("X Label")
plot.setYLabel("Y Label")
plot.setYLimits(0, 60)

plot.grid.color = "#ff0000"
plot.grid.style = "dotted"
plot.grid.visible = True

plot.save("customgri")
