plot = Plot()
line = Line()
plot.setDimensions(3, 4)

line.xValues = range(5)
line.yValues = range(5)

plot.add(line)
plot.save(self.imageName)

im = Image.open(self.imageName)
self.assertEqual(im.size, (300,400))

plot.setDimensions(3,4,dpi=250)

plot.save("exactsize.png")
