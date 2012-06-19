Plot Elements
=============

Plot elements in Boomslang are represented by objects that encapsulate all the
state that a plot element needs to draw itself. The one required method that
all plot elements must implement is `draw(self, fig, axes)`, which the element
uses to draw itself within the figure `fig` on the axes `axes`.

PlotInfo: The Common Plot Element Base Class
--------------------------------------------

Many of Boomslang's plot elements inherit from PlotInfo. PlotInfo contains
several useful fields (x-axis and y-axis values, error bars, etc.)

.. autoclass:: boomslang.PlotInfo.PlotInfo
    :members:

Simple Plot Elements
--------------------

Boomslang comes equipped with the standard plot elements for making lines, bar
graphs, scatter plots, and box-and-whisker plots.

.. autoclass:: boomslang.Line.Line
    :members:

.. autoclass:: boomslang.HLine.HLine
    :members:

.. autoclass:: boomslang.VLine.VLine
    :members:

.. autoclass:: boomslang.Scatter.Scatter
    :members:

.. autoclass:: boomslang.Bar.Bar
    :members:

.. autoclass:: boomslang.BoxAndWhisker.BoxAndWhisker
    :members:


Compound Plot Elements
----------------------

Boomslang can combine certain plot elements together to easily create stacks
and clusters of plot elements while maintaining the individual elements
themselves, making it easy to re-compose them by changing a couple of lines of
code.

.. autoclass:: boomslang.ClusteredBars.ClusteredBars
    :members:

.. autoclass:: boomslang.StackedBars.StackedBars
    :members:

.. autoclass:: boomslang.StackedLines.StackedLines
    :members:

Miscellaneous Plot Elements
---------------------------

.. autoclass:: boomslang.Label.Label
    :members:

.. autoclass:: boomslang.Grid.Grid
    :members:
