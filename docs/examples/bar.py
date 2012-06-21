plot = Plot()

bar = Bar()
bar.xValues = range(5)
bar.yValues = [2, 8, 4, 6, 5]

plot.add(bar)
plot.xLabel = "Widget ID"
plot.yLabel = "# Widgets Sold"

plot.save("bar.png")
