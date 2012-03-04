Getting Started
===============

Boomslang is designed to make creating common kinds of plots easier. In this section of the documentation, we'll look at how Boomslang tries to do that and how to start building plots with Boomslang.

Design Principles
-----------------

**Plotting code should be reusable and modular.** Traditional wisdom holds that a plot's axes and the things that are plotted on those axes (lines, points, bars) are inseparable. Boomslang chooses to separate the axes (which we call a *plot*) from the things that are drawn on those axes (which we call *plot elements*).


**Matplotlib is complicated. Boomslang should be easy.** Matplotlib is an extremely powerful library, but its power comes at a cost in terms of complexity. Boomslang aims to abstract most or all of that complexity away from the end user.


**Boomslang is not Matplotlib.** There are many kinds of graphs that Matplotlib can generate and Boomslang cannot. Boomslang's goal is not to be a general-purpose figure plotting engine, but to provide an easier alternative to Matplotlib for plots that people find themselves wanting to generate the majority of the time.


Writing your First Boomslang Script
-----------------------------------

Let's walk through a simple example of how to use Boomslang. Consider the code below:

.. literalinclude:: examples/simpleline.py
    :language: python
    :linenos:

On line 1, we create a plot element, in this case a ``Line``. Plot elements are
simply objects that know how to draw themselves. The values of their fields
determines what gets drawn. In this case, we're setting the line's x and y
values. We could also set things like the line's color, width, and whether it
is dashed or dotted. See the API documentation for more information on the
different kind of plot elements and their properties.

On line 4, we create a ``Plot``. You can think of plots as containers for plot
elements, but also as objects that know how to draw themselves. On line 5, we
add the line to the plot using the ``Plot.add()`` method.

The next few lines do things like setting the labels of the plot's X and Y
axes, and setting bounds on the Y axis.

The last line saves the plot to a file. This feature uses Matplotlib's
underlying save functionality, and can support a wide range of formats. If you
want an interactive view of the plot, you could call ``plot.plot()``.

