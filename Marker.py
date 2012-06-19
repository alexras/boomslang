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
        Defines the shape of the marker.
        """

        return self._marker

    @marker.setter
    def marker(self, value):
        if value not in Marker.VALID_MARKS:
            raise ValueError("'%s' is not a valid mark" % (value))

        self._marker = Marker.VALID_MARKS[value]

