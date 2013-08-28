Examples: examples/label.py
===========================


.. image:: examples/label.png

Back to :ref:`examples-gallery`

.. code-block:: python
    :linenos:


    line = Line()
    line.xValues = numpy.arange(0.0, 5.0, 0.01)
    line.yValues = numpy.cos(2 * numpy.pi * line.xValues)
    
    maxLabel = Label(2, 1, "Maximum!")
    maxLabel.textOffset = (0.5, 0.5)
    maxLabel.hasArrow()
    
    minLabel = Label(1.5, -1, "Minimum!")
    minLabel.textPosition = (1, -2)
    minLabel.hasArrow()
    
    randomLabel = Label(2, -1.7, "A Point!")
    randomLabel.textOffset = (0, 0.2)
    randomLabel.marker = 'o'
    
    styledLabel = Label(1.25, 1.2, "A FancyPoint!",
    bbox={'edgecolor':'red',
    'facecolor':'white',
    'ls':'dashed',
    'lw':'2'})
    styledLabel.textOffset = (0, 0.2)
    styledLabel.marker = 'o'
    
    plot = Plot()
    plot.add(line)
    plot.add(minLabel)
    plot.add(maxLabel)
    plot.add(randomLabel)
    plot.add(styledLabel)
    plot.yLimits = (-3, 3)
    plot.xLabel = "X"
    plot.yLabel = "cos(x)"
    plot.save("label.png")
