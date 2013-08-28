Plots
=====

Plots in Boomslang are constructed by adding plot elements to Plot objects. The
Plot object's API is defined below.

.. autoclass:: boomslang.Plot.Plot
   :members:


.. _plots-grid-lines:

Grid Lines
----------

:py:attr:`boomslang.Plot.Plot.grid` is a :class:`boomslang.Grid.Grid` object that
defines the appearance of the plot's grid lines. By default, there are no grid
lines.

.. autoclass:: boomslang.Grid.Grid
   :members:

.. _plots-locations:

Locations
---------

Parts of a plot like legends and insets allow the user to explicitly specify
their location (by default, matplotlib tries do to place the legend/inset where
it is least obtrusive). Boomslang defines the standard matplotlib location
strings along with a number of aliases that some find more intuitive than the
defaults.

Valid location strings (clockwise from top middle, plus centered) are as
follows:

* "upper center", "top middle" "upper middle"
* "upper right", "top right"
* "center right", "middle right", "right"
* "lower right", "bottom right"
* "lower center", "bottom middle", "bottom center"
* "lower left", "bottom left"
* "center left", "middle left", "left",
* "upper left", "top left"
* "center", "middle"

