
Examples
========

.. htmlonly::

+------------------------------------------+---------------------------------------------------------------+
|Image                                     |Source Code                                                    |
+==========================================+===============================================================+
|.. image:: examples/simpleline.png        |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.yValues = [25, 40, 30, 23, 10, 50]                    |
|                                          |    line.xValues = range(len(line.yValues))                    |
|                                          |                                                               |
|                                          |    plot.add(line)                                             |
|                                          |    plot.setXLabel("X Label")                                  |
|                                          |    plot.setYLabel("Y Label")                                  |
|                                          |    plot.setYLimits(0, 60)                                     |
|                                          |    plot.save("simpleline.png")                                |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/logscale.png          |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |                                                               |
|                                          |    plotBase10 = Plot()                                        |
|                                          |    plotBase10.loglog = True                                   |
|                                          |                                                               |
|                                          |    lineBase10 = Line()                                        |
|                                          |    lineBase10.marker = 'x'                                    |
|                                          |    lineBase10.xValues = [1, 10, 100, 1000, 10000]             |
|                                          |    lineBase10.yValues = [1, 25, 140, 1024, 10342]             |
|                                          |                                                               |
|                                          |    plotBase10.add(lineBase10)                                 |
|                                          |                                                               |
|                                          |    plotBase2 = Plot()                                         |
|                                          |    plotBase2.logx = True                                      |
|                                          |    plotBase2.logbase = 2                                      |
|                                          |                                                               |
|                                          |    lineBase2 = Line()                                         |
|                                          |    lineBase2.marker = 'x'                                     |
|                                          |    lineBase2.xValues = [1, 2, 4, 8, 16, 32, 64]               |
|                                          |    lineBase2.yValues = [1, 2, 3, 4, 5, 6, 7]                  |
|                                          |                                                               |
|                                          |    plotBase2.add(lineBase2)                                   |
|                                          |                                                               |
|                                          |                                                               |
|                                          |    layout.addPlot(plotBase10)                                 |
|                                          |    layout.addPlot(plotBase2)                                  |
|                                          |                                                               |
|                                          |    layout.width = 2                                           |
|                                          |    layout.save("logscale.png")                                |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/linestyles.png        |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    for i in xrange(6):                                        |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = xrange(5)                                   |
|                                          |    line.yValues = [(i+1) * x for x in line.xValues]           |
|                                          |    line.label = "Line %d" % (i + 1)                           |
|                                          |    plot.add(line)                                             |
|                                          |                                                               |
|                                          |    plot.addLineColor("red")                                   |
|                                          |    plot.addLineColor("blue")                                  |
|                                          |    plot.addLineStyle("-")                                     |
|                                          |    plot.addLineStyle("--")                                    |
|                                          |    plot.addLineStyle(":")                                     |
|                                          |    plot.hasLegend(columns=2)                                  |
|                                          |    plot.save("linestyles.png")                                |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/errorbars.png         |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    # Uneven error bars                                        |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = range(6)                                    |
|                                          |    line.yValues = [25, 21, 30, 23, 10, 30]                    |
|                                          |    line.yMins = [10, 18, 10, 10, 5, 20]                       |
|                                          |    line.yMaxes = [30, 50, 40, 30, 20, 45]                     |
|                                          |    line.label = "Asymmetric Errors"                           |
|                                          |    line.color = "red"                                         |
|                                          |                                                               |
|                                          |    line.xValues = range(len(line.yValues))                    |
|                                          |                                                               |
|                                          |    # Even error bars                                          |
|                                          |    line2 = Line()                                             |
|                                          |    line2.xValues = range(6)                                   |
|                                          |    line2.yValues = [35, 40, 45, 40, 55, 50]                   |
|                                          |    line2.color = "blue"                                       |
|                                          |    line2.label = "Symmetric Errors"                           |
|                                          |    line2.yErrors = [3, 6, 5, 3, 5, 4]                         |
|                                          |                                                               |
|                                          |    plot.add(line)                                             |
|                                          |    plot.add(line2)                                            |
|                                          |    plot.setXLabel("X Label")                                  |
|                                          |    plot.setYLabel("Y Label")                                  |
|                                          |    plot.hasLegend()                                           |
|                                          |    plot.save("errorbars.png")                                 |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/twinx.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line1 = Line()                                             |
|                                          |    line1.xValues = range(7)                                   |
|                                          |    line1.yValues = [1, 2, 4, 8, 16, 32, 64]                   |
|                                          |    line1.label = "First Plot"                                 |
|                                          |    line1.lineStyle = "-"                                      |
|                                          |    line1.color = "red"                                        |
|                                          |                                                               |
|                                          |    line2 = Line()                                             |
|                                          |    line2.xValues = range(7)                                   |
|                                          |    line2.yValues = [100, 90, 80, 70, 60, 50, 40]              |
|                                          |    line2.label = "Second Plot"                                |
|                                          |    line2.lineStyle = "--"                                     |
|                                          |    line2.color = "blue"                                       |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(line1)                                            |
|                                          |    plot.add(line2)                                            |
|                                          |    plot.setXLabel("Shared X Axis")                            |
|                                          |    plot.setYLabel("First Plot's Y Axis")                      |
|                                          |    plot.setTwinX("Second Plot's Y Axis", 1)                   |
|                                          |    plot.hasLegend()                                           |
|                                          |                                                               |
|                                          |    plot.save("twinx.png")                                     |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/hatchedbars.png       |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    bar = Bar()                                                |
|                                          |                                                               |
|                                          |    bar.xValues = range(5)                                     |
|                                          |    bar.yValues = [2, 4, 6, 8, 10]                             |
|                                          |    # Valid values include all marker types,                   |
|                                          |    # /, //, \, \\                                             |
|                                          |    bar.hatch = r"\\"                                          |
|                                          |    bar.color="red"                                            |
|                                          |    bar.edgeColor="black"                                      |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(bar)                                              |
|                                          |    plot.save("hatchedbars.png")                               |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/stackedbar.png        |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    bar1 = Bar()                                               |
|                                          |    bar1.xValues = range(5)                                    |
|                                          |    bar1.yValues = [1, 2, 1, 2, 3]                             |
|                                          |    bar1.color = "red"                                         |
|                                          |    bar1.label = "Red Cluster"                                 |
|                                          |                                                               |
|                                          |    bar2 = Bar()                                               |
|                                          |    bar2.xValues = range(5)                                    |
|                                          |    bar2.yValues = [2, 2, 3, 3, 4]                             |
|                                          |    bar2.color = "blue"                                        |
|                                          |    bar2.label = "Blue Cluster"                                |
|                                          |                                                               |
|                                          |    bar3 = Bar()                                               |
|                                          |    bar3.xValues = range(5)                                    |
|                                          |    bar3.yValues = [3, 5, 4, 5, 3]                             |
|                                          |    bar3.color = "green"                                       |
|                                          |    bar3.label = "Green Cluster"                               |
|                                          |                                                               |
|                                          |    stackedBars = StackedBars()                                |
|                                          |    stackedBars.add(bar1)                                      |
|                                          |    stackedBars.add(bar2)                                      |
|                                          |    stackedBars.add(bar3)                                      |
|                                          |                                                               |
|                                          |    stackedBars.xTickLabels = ["A", "B", "C", "D", "E"]        |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(stackedBars)                                      |
|                                          |    plot.setYLimits(0, 15)                                     |
|                                          |    plot.hasLegend()                                           |
|                                          |    plot.save("stackedbar.png")                                |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/label.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = numpy.arange(0.0, 5.0, 0.01)                |
|                                          |    line.yValues = numpy.cos(2 * numpy.pi * line.xValues)      |
|                                          |                                                               |
|                                          |    maxLabel = Label(2, 1, "Maximum!")                         |
|                                          |    maxLabel.setTextOffset(0.5, 0.5)                           |
|                                          |    maxLabel.hasArrow()                                        |
|                                          |                                                               |
|                                          |    minLabel = Label(1.5, -1, "Minimum!")                      |
|                                          |    minLabel.setTextPosition(1, -2)                            |
|                                          |    minLabel.hasArrow()                                        |
|                                          |                                                               |
|                                          |    randomLabel = Label(2, -1.7, "A Point!")                   |
|                                          |    randomLabel.setTextOffset(0, 0.2)                          |
|                                          |    randomLabel.marker = 'o'                                   |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(line)                                             |
|                                          |    plot.add(minLabel)                                         |
|                                          |    plot.add(maxLabel)                                         |
|                                          |    plot.add(randomLabel)                                      |
|                                          |    plot.setYLimits(-3, 3)                                     |
|                                          |    plot.setXLabel("X")                                        |
|                                          |    plot.setYLabel("cos(x)")                                   |
|                                          |    plot.save("label.png")                                     |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/steps.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    xVals = [1, 2, 3, 4, 5]                                    |
|                                          |    yVals = [1, 2, 3, 4, 5]                                    |
|                                          |                                                               |
|                                          |    def generatePlot(stepType):                                |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = xVals                                       |
|                                          |    line.yValues = yVals                                       |
|                                          |    line.marker = 'o'                                          |
|                                          |    line.stepFunction(stepType)                                |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(line)                                             |
|                                          |    plot.setTitle(r'"%s" Steps' % (stepType))                  |
|                                          |    plot.setXLimits(0, 6)                                      |
|                                          |    plot.setYLimits(0, 6)                                      |
|                                          |                                                               |
|                                          |    return plot                                                |
|                                          |                                                               |
|                                          |    prePlot = generatePlot("pre")                              |
|                                          |    midPlot = generatePlot("mid")                              |
|                                          |    postPlot = generatePlot("post")                            |
|                                          |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |    layout.width = 1                                           |
|                                          |    layout.addPlot(prePlot)                                    |
|                                          |    layout.addPlot(midPlot)                                    |
|                                          |    layout.addPlot(postPlot)                                   |
|                                          |    layout.setPlotParameters(top=0.96, bottom=0.04)            |
|                                          |    layout.save("steps.png")                                   |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/split.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    import numpy                                               |
|                                          |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = numpy.arange(0, 150, 0.01)                  |
|                                          |    line.yValues = numpy.cos(.02 * numpy.pi * line.xValues)    |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(line)                                             |
|                                          |    plot.setXLimits(0, 150)                                    |
|                                          |    plot.setYLimits(-1, 1)                                     |
|                                          |    plot.setXLabel("X")                                        |
|                                          |    plot.setYLabel("cos(X)")                                   |
|                                          |    splitPlots = plot.split(2)                                 |
|                                          |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |    layout.width = 2                                           |
|                                          |    layout.addPlot(plot, grouping="unsplit")                   |
|                                          |                                                               |
|                                          |    for s in splitPlots:                                       |
|                                          |    layout.addPlot(s, grouping="splits")                       |
|                                          |                                                               |
|                                          |    layout.save("split.png")                                   |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/unordered.png         |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = [2, 1, 3, 4, 0]                             |
|                                          |    line.yValues = [2, 1, 3, 4, 0]                             |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(line)                                             |
|                                          |                                                               |
|                                          |    plot.save("unordered.png")                                 |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/scatter.png           |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    scatter = Scatter()                                        |
|                                          |    scatter.label="Hooray dots!"                               |
|                                          |                                                               |
|                                          |    for i in range(100):                                       |
|                                          |    scatter.xValues.append(random.uniform(0, 10))              |
|                                          |    scatter.yValues.append(random.uniform(0, 10))              |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.hasLegend()                                           |
|                                          |    plot.add(scatter)                                          |
|                                          |    plot.save("scatter.png")                                   |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/clusteredbars.png     |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    bar1 = Bar()                                               |
|                                          |    bar1.xValues = range(5)                                    |
|                                          |    bar1.yValues = [2, 4, 6, 8, 10]                            |
|                                          |    bar1.color = "red"                                         |
|                                          |    bar1.label = "Red Cluster"                                 |
|                                          |                                                               |
|                                          |    bar2 = Bar()                                               |
|                                          |    bar2.xValues = range(5)                                    |
|                                          |    bar2.yValues = [3, 12, 4, 8, 14]                           |
|                                          |    bar2.color = "blue"                                        |
|                                          |    bar2.label = "Blue Cluster"                                |
|                                          |                                                               |
|                                          |    bar3 = Bar()                                               |
|                                          |    bar3.xValues = range(5)                                    |
|                                          |    bar3.yValues = [1, 6, 9, 13, 20]                           |
|                                          |    bar3.color = "green"                                       |
|                                          |    bar3.label = "Green Cluster"                               |
|                                          |                                                               |
|                                          |    clusteredBars = ClusteredBars()                            |
|                                          |                                                               |
|                                          |    clusteredBars.add(bar1)                                    |
|                                          |    clusteredBars.add(bar2)                                    |
|                                          |    clusteredBars.add(bar3)                                    |
|                                          |    clusteredBars.spacing = 0.5                                |
|                                          |                                                               |
|                                          |    clusteredBars.xTickLabels = ["A", "B", "C", "D", "E"]      |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(clusteredBars)                                    |
|                                          |    plot.hasLegend()                                           |
|                                          |                                                               |
|                                          |    plot.save("clusteredbars.png")                             |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/tickstyles.png        |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.yValues = [25, 40, 30, 23, 10, 50]                    |
|                                          |    line.xValues = range(len(line.yValues))                    |
|                                          |    line.xTickLabels = [                                       |
|                                          |    "X 1", "X 2", "X 3", "X 4", "X 5"]                         |
|                                          |    line.yTickLabels = [                                       |
|                                          |    "Y Ten", "Y Twenty", "Y Thirty", "Y Forty",                |
|                                          |    "Y Fifty", "Y Sixty"]                                      |
|                                          |                                                               |
|                                          |    line.yTickLabelPoints = [10, 20, 30, 40, 50, 60]           |
|                                          |    line.setXTickLabelProperties(color="blue",                 |
|                                          |    weight="bold",                                             |
|                                          |    rotation="45")                                             |
|                                          |    line.setYTickLabelProperties(style="italic",               |
|                                          |    alpha=0.5,                                                 |
|                                          |    color="red")                                               |
|                                          |    plot.add(line)                                             |
|                                          |    plot.setXLabel("X Label")                                  |
|                                          |    plot.setYLabel("Y Label")                                  |
|                                          |    plot.setYLimits(0, 60)                                     |
|                                          |                                                               |
|                                          |    plot.setPlotParameters(bottom=.15, left=0.15)              |
|                                          |                                                               |
|                                          |    plot.save("tickstyles.png")                                |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/legendLabelSizes.png  |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = range(5)                                    |
|                                          |    line.yValues = [2,3,5,7,9]                                 |
|                                          |    line.label = "A Line"                                      |
|                                          |                                                               |
|                                          |    linePlot1 = Plot()                                         |
|                                          |    linePlot1.setTitle("Small Legend")                         |
|                                          |    linePlot1.add(line)                                        |
|                                          |    linePlot1.hasLegend()                                      |
|                                          |    linePlot1.setLegendLabelSize(10)                           |
|                                          |                                                               |
|                                          |    linePlot2 = Plot()                                         |
|                                          |    linePlot2.setTitle("Large Legend")                         |
|                                          |    linePlot2.add(line)                                        |
|                                          |    linePlot2.hasLegend()                                      |
|                                          |    linePlot2.setLegendLabelSize(30)                           |
|                                          |                                                               |
|                                          |    linePlot3 = Plot()                                         |
|                                          |    linePlot3.setTitle("Inherited from Layout")                |
|                                          |    linePlot3.add(line)                                        |
|                                          |    linePlot3.hasLegend()                                      |
|                                          |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |    layout.setWidth(2)                                         |
|                                          |    layout.addPlot(linePlot1)                                  |
|                                          |    layout.addPlot(linePlot2)                                  |
|                                          |    layout.addPlot(linePlot3)                                  |
|                                          |    layout.setLegendLabelSize(15)                              |
|                                          |    layout.setPlotParameters(left=0.03, bottom=0.03,           |
|                                          |    right=0.98, top=0.94)                                      |
|                                          |    layout.plot()                                              |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/bar.png               |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    bar = Bar()                                                |
|                                          |    bar.xValues = range(5)                                     |
|                                          |    bar.yValues = [2, 8, 4, 6, 5]                              |
|                                          |                                                               |
|                                          |    plot.add(bar)                                              |
|                                          |    plot.setXLabel("Widget ID")                                |
|                                          |    plot.setYLabel("# Widgets Sold")                           |
|                                          |                                                               |
|                                          |    plot.save("bar.png")                                       |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/latex.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = [0, 1, 2, 3, 4, 5,                          |
|                                          |    6, 7, 8, 9, 10]                                            |
|                                          |    line.yValues = [0, 1, 4, 9, 16, 25,                        |
|                                          |    36, 49, 64, 81, 100]                                       |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.useLatexLabels()                                      |
|                                          |    plot.setXLabel(r"$x$")                                     |
|                                          |    plot.setYLabel(r"$f(x) = x^2$")                            |
|                                          |    plot.setTitle(                                             |
|                                          |    r"LaTeX is Number $\sum_{n=1}^{\infty}"                    |
|                                          |    "\frac{-e^{i\pi}}{2^n}$")                                  |
|                                          |    plot.add(line)                                             |
|                                          |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |    layout.addPlot(plot)                                       |
|                                          |                                                               |
|                                          |    layout.setAxesLabelSize(18)                                |
|                                          |    layout.setPlotParameters(top=0.84)                         |
|                                          |    layout.save("latex.png")                                   |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/layout.png            |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = range(5)                                    |
|                                          |    line.yValues = [2, 4, 6, 8, 10]                            |
|                                          |                                                               |
|                                          |    linePlot = Plot()                                          |
|                                          |    linePlot.add(line)                                         |
|                                          |    linePlot.setXLabel("X Data")                               |
|                                          |    linePlot.setYLabel("Y Data")                               |
|                                          |    linePlot.setTitle("Data as Line")                          |
|                                          |                                                               |
|                                          |    bar = Bar()                                                |
|                                          |    bar.xValues = range(5)                                     |
|                                          |    bar.yValues = [2, 4, 6, 8, 10]                             |
|                                          |                                                               |
|                                          |    barPlot = Plot()                                           |
|                                          |                                                               |
|                                          |    barPlot.add(bar)                                           |
|                                          |    barPlot.setXLabel("X Data")                                |
|                                          |    barPlot.setYLabel("Y Data")                                |
|                                          |    barPlot.setTitle("Data as Bars")                           |
|                                          |                                                               |
|                                          |    scatter = Scatter()                                        |
|                                          |    scatter.xValues = range(5)                                 |
|                                          |    scatter.yValues = [2, 4, 6, 8, 10]                         |
|                                          |                                                               |
|                                          |    scatterPlot = Plot()                                       |
|                                          |    scatterPlot.add(scatter)                                   |
|                                          |    scatterPlot.setXLabel("X Data")                            |
|                                          |    scatterPlot.setYLabel("Y Data")                            |
|                                          |    scatterPlot.setTitle("Data as Points")                     |
|                                          |                                                               |
|                                          |    layout = PlotLayout()                                      |
|                                          |                                                               |
|                                          |    layout.addPlot(linePlot, grouping="topRow")                |
|                                          |    layout.addPlot(barPlot, grouping="topRow")                 |
|                                          |                                                               |
|                                          |    layout.addPlot(scatterPlot)                                |
|                                          |                                                               |
|                                          |    # Set values similar to those given in the                 |
|                                          |    # "Configure subplots" sliders in the                      |
|                                          |    # interactive figure                                       |
|                                          |    layout.setPlotParameters(hspace=0.48)                      |
|                                          |    layout.save("layout.png")                                  |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/inset.png             |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    lines = []                                                 |
|                                          |                                                               |
|                                          |    for i in xrange(3):                                        |
|                                          |    line = Line()                                              |
|                                          |    line.xValues = xrange(5)                                   |
|                                          |    line.yValues = [(i+1 / 2.0) *  pow(x, i+1)                 |
|                                          |    for x in line.xValues]                                     |
|                                          |    line.label = "Line %d" % (i + 1)                           |
|                                          |    lines.append(line)                                         |
|                                          |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |    plot.add(lines[0])                                         |
|                                          |                                                               |
|                                          |    inset = Plot()                                             |
|                                          |    inset.add(lines[1])                                        |
|                                          |    inset.hideTickLabels()                                     |
|                                          |    inset.setTitle("Inset in Yo Inset\n"                       |
|                                          |    "So You Can Inset\n"                                       |
|                                          |    "While You Inset")                                         |
|                                          |                                                               |
|                                          |    insideInset = Plot()                                       |
|                                          |    insideInset.hideTickLabels()                               |
|                                          |    insideInset.add(lines[2])                                  |
|                                          |                                                               |
|                                          |    inset.addInset(insideInset, width=0.4,                     |
|                                          |    height=0.3, location="upper left")                         |
|                                          |                                                               |
|                                          |    plot.addInset(inset, width=0.4, height=0.4,                |
|                                          |    location="lower right")                                    |
|                                          |                                                               |
|                                          |    plot.save("inset.png")                                     |
+------------------------------------------+---------------------------------------------------------------+
|.. image:: examples/fontsizes.png         |::                                                             |
|    :width: 100 %                         |                                                               |
|                                          |    plot = Plot()                                              |
|                                          |                                                               |
|                                          |    line = Line()                                              |
|                                          |    line.yValues = [25, 40, 30, 23, 10, 50]                    |
|                                          |    line.xValues = range(len(line.yValues))                    |
|                                          |                                                               |
|                                          |    plot.add(line)                                             |
|                                          |    plot.setXLabel("X Label")                                  |
|                                          |    plot.setYLabel("Y Label")                                  |
|                                          |    plot.setYLimits(0, 60)                                     |
|                                          |                                                               |
|                                          |    plot.setXTickLabelSize(24)                                 |
|                                          |    plot.setYTickLabelSize(36)                                 |
|                                          |    plot.setAxesLabelSize(18)                                  |
|                                          |                                                               |
|                                          |    plot.setPlotParameters(bottom=0.14)                        |
|                                          |                                                               |
|                                          |    plot.save("fontsizes.png")                                 |
+------------------------------------------+---------------------------------------------------------------+
