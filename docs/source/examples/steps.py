xVals = [1, 2, 3, 4, 5]
yVals = [1, 2, 3, 4, 5]

def generatePlot(stepType):
    line = Line()
    line.xValues = xVals
    line.yValues = yVals
    line.marker = 'o'
    line.stepFunction(stepType)

    plot = Plot()
    plot.add(line)
    plot.title = r'"%s" Steps' % (stepType)
    plot.xLimits = (0, 6)
    plot.yLimits = (0, 6)

    return plot

prePlot = generatePlot("pre")
midPlot = generatePlot("mid")
postPlot = generatePlot("post")

layout = PlotLayout()
layout.width = 1
layout.addPlot(prePlot)
layout.addPlot(midPlot)
layout.addPlot(postPlot)

layout.save("steps.png")
