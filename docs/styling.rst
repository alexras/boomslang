Styling Plot Elements
=====================

This page describes the various ways that Boomslang's plot elements can be
styled. Classes described below are typically used as Python properties,
allowing them to be treated like normal fields with the benefits of aliasing
and argument checking.

.. _styling-markers:

Markers
-------

Markers are used to annotate or distinguish particular points on the Cartesian
plane. There are a large number of options for configuring markers in
matplotlib; Boomslang exports a subset of them in a way that's a little easier
to deal with.

Valid marker styles are as follows:

=========================================     ====================================================================
Description                                   Valid Values of boomslang.Marker.Marker.marker
=========================================     ====================================================================
No marker                                      ``""``, "none", None
Points                                         ``.``, "point", "points"
Pixels                                         ``,``, "pixel", "pixels"
Circles                                        ``o``, "circle", "circles"
Triangles Pointing Down                        ``v``, "down triangle", "down triangles"
Triangles Pointing Up                          ``^``, "up triangle", "up triangles"
Triangles Pointing Left                        ``<``, "left triangle", "left triangles"
Triangles Pointing Right                       ``>``, "right triangle", "right triangles"
Squares                                        ``s``, "square", "squares"
Pentagons                                      ``p``, "pentagon", "pentagons"
Stars                                          ``*``, "star", "stars"
Hexagons with Parallel Sides Vertical          ``h``, "hexagon", "hexagons", "vertical hexagon", "vertical hexagons"
Hexagons with Parallel Sides Horizontal        ``H``, "horizontal hexagon", "horizontal hexagons"
Pluses                                         ``+``, "plus", "pluses", "plusses"
Crosses (Xs)                                   ``x``, "cross", "crosses"
Thick Diamonds                                 ``D``, "diamond", "diamonds"
Thin Diamonds                                  ``d``, "thin diamond", "thin diamonds"
Vertical Lines                                 ``|``, "vline", "vlines", "vertical line", "vertical lines"
Horizontal Lines                               ``_``, "hline", "hlines", "horizontal line", "horizontal lines"
=========================================     ====================================================================

Labels
------

Labels include things like tick labels (the numbers on the axes themselves),
axis labels (labels that apply to an entire axis), and the
:ref:`boomslang.Label.Label` plot element. They can also be styled in a number
of different ways.

Valid label style properties are as follows:

========================  =================================================================================================================================================================================================
Property                  Description
========================  =================================================================================================================================================================================================
``alpha``                 Transparency of the label in [0.0, 1.0]
``backgroundColor``       The label's background color
``color``                 The label's text color
``fontsize``              The size of the label's font
``horizontalalignment``   The horizontal alignment of the label's text ('left', 'center', or 'right')
``linespacing``           The spacing between label lines (multiple of font size)
``multialignment``        Alignment for multiple lines of text ('left', 'center', or 'right')
``rotation``              Angle of the label's rotation in degrees
``rotation_mode``         Text rotation mode ("anchor" to align before rotating, None (default) to rotate before aligning)
``stretch``               Label's font stretch (horizontal condensation or expansion)
``style``                 The font's style ('normal', 'italic', or 'oblique')
``verticalalignment``     The vertical alignment of the label's text ('top', 'center', 'bottom', or 'baseline')
``weight``                The font's weight (a number in [0, 1000] or one of 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black')
========================  =================================================================================================================================================================================================

.. _styling-lines:

Line Styles
-----------

Boomslang has a standard level of control over how lines are rendered. At the
moment, they can be solid, dashed, dotted, or alternate between dashes and
dots. Boomslang includes some aliases for these line styles so that you don't
have to remember the specific Matplotlib glyphs for each style.

Valid line styles are as follows:

=========================  ==============================================
Description                Valid line style values
=========================  ==============================================
Solid                      ``-``, "solid", None
Dashed                     ``--``, "dashed"
Alternating Dash and Dot   ``-.``, "dash-dot", "dot-dash"
Dotted                     ``:``, "dotted"
=========================  ==============================================

.. _styling-colors:

Colors
------

Colors in Boomslang can be specified by name ("black", "blue"), a
floating-point shade of gray ("0.75"), or an HTML hex string
("#ab45bc"). Certain common colors can also be specified by one-letter
abbreviations. Supported colors are red (r), green (g), blue (b), cyan (c),
yellow (y), magenta (m), black (k), and white (w).
