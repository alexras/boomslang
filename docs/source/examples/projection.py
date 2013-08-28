plot = Plot()
plot.projection = 'polar'

r = arange(0,1,0.001)
theta = 2*2*pi*r

line = Line()
line.xValues = theta
line.yValues = r
plot.add(line)
plot.save("projection.png")

