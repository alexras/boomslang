class Marker(object):
    """
    This property controls the way that a plot element's markers look.
    """

    _MARK_TRANSLATOR = {
        "" : ["none", None],
        "." : ["point", "points"],
        "," : ["pixel", "pixels"],
        "o" : ["circle", "circles"],
        "v" : ["down triangle", "down triangles"],
        "^" : ["up triangle", "up triangles"],
        "<" : ["left triangle", "left triangles"],
        ">" : ["right triangle", "right triangles"],
        "s" : ["square", "squares"],
        "p" : ["pentagon", "pentagons"],
        "*" : ["star", "stars"],
        "h" : ["hexagon", "hexagons", "vertical hexagon", "vertical hexagons"],
        "H" : ["horizontal hexagon", "horizontal hexagons"],
        "+" : ["plus", "pluses", "plusses"],
        "x" : ["x", "cross", "crosses"],
        "D" : ["diamond", "diamonds"],
        "d" : ["thin diamond", "thin diamonds"],
        "|" : ["vline", "vlines", "vertical line", "vertical lines"],
        "_" : ["hline", "hlines", "horizontal line", "horizontal lines"]
        }

    """
    This dictionary (derived from _MARK_TRANSLATOR) maps valid marker types to
    their matplotlib equivalents.
    """
    VALID_MARKS = {}

    for (glyph, equivalents) in _MARK_TRANSLATOR.items():
        VALID_MARKS[glyph] = glyph

        for equiv in equivalents:
            VALID_MARKS[equiv] = glyph

    def __init__(self):
        self._marker = None

        self.size = 8.0
        """
        The size of the marker
        """

    @property
    def marker(self):
        """
        Defines the shape of the marker. Valid marker shapes are:

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
        """

        return self._marker

    @marker.setter
    def marker(self, value):
        if value not in Marker.VALID_MARKS:
            raise ValueError("'%s' is not a valid mark" % (value))

        self._marker = Marker.VALID_MARKS[value]

