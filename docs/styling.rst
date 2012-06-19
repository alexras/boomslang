Styling Plot Elements
=====================

This page describes the various ways that Boomslang's plot elements can be
styled. Classes described below are typically used as Python properties,
allowing them to be treated like normal fields with the benefits of aliasing
and argument checking.

Markers
-------

Markers are used to annotate or distinguish particular points on the Cartesian
plane. There are a large number of options for configuring markers in
matplotlib; Boomslang exports a subset of them in a way that's a little easier
to deal with.

.. autoclass:: boomslang.Marker.Marker
    :members:

Labels
------

Labels include things like tick labels (the numbers on the axes themselves),
axis labels (labels that apply to an entire axis), and the
:ref:`boomslang.Label.Label` plot element. They can also be styled in a number
of different ways.

.. autoclass:: boomslang.LabelProperties.LabelProperties
    :members:

Colors
------

Colors in Boomslang can be specified by name ("black", "blue"), a
floating-point shade of gray ("0.75"), or an HTML hex string
("#ab45bc"). Certain common colors can also be specified by one-letter
abbreviations. Supported colors are red (r), green (g), blue (b), cyan (c),
yellow (y), magenta (m), black (k), and white (w).
