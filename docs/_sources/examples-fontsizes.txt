Examples: examples/fontsizes.py
===============================


.. image:: examples/fontsizes.png

Back to :ref:`examples-gallery`

.. code-block:: python
    :linenos:


    plot = Plot()
    
    line = Line()
    line.yValues = [25, 40, 30, 23, 10, 50]
    line.xValues = range(len(line.yValues))
    
    plot.add(line)
    plot.xLabel = "X Label"
    plot.yLabel = "Y Label"
    plot.yLimits = (0, 60)
    
    plot.xTickLabelSize = 24
    plot.yTickLabelSize = 36
    plot.axesLabelSize = 18
    plot.tight = True
    
    plot.save(self.imageName)
