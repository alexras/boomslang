class LineStyle(object):
    """
    This property controls the way that a line looks.
    """

    _STYLE_TRANSLATOR = {
            "-" : ["solid", None],
            "--" : ["dashed"],
            "-." : ["dash-dot", "dot-dash"],
            ":" : ["dotted"],
            }

    VALID_STYLES = {}

    for (glyph, equivalents) in _STYLE_TRANSLATOR.items():
        VALID_STYLES[glyph] = glyph

        for equiv in equivalents:
            VALID_STYLES[equiv] = glyph

    def __init__(self):
        self._style = "-"

    @property
    def style(self):
        """
        The style in which the line will be drawn.
        """
        return self._style

    @style.setter
    def style(self, value):
        assert value in LineStyle.VALID_STYLES, "'%s' is not a valid "\
            "line style" % (value)
        self._style = LineStyle.VALID_STYLES[value]

