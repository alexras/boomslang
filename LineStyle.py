class LineStyle(object):
    """
    This dictionary maps matplotlib representations of marker types to English
    descriptions. Either can be used when specifying marker type.
    """
    _STYLE_TRANSLATOR = {
            "-" : ["solid", None],
            "--" : ["dashed"],
            "-." : ["dash-dot", "dot-dash"],
            ":" : ["dotted"],
            }

    """
    This dictionary (derived from _STYLE_TRANSLATOR) maps valid marker types to
    their matplotlib equivalents.
    """
    VALID_STYLES = {}

    for (glyph, equivalents) in _STYLE_TRANSLATOR.items():
        VALID_STYLES[glyph] = glyph

        for equiv in equivalents:
            VALID_STYLES[equiv] = glyph

    def __init__(self):
        self._style = "-"

    @property
    def style(self):
        """ The style in which the line will be drawn """
        return self._style

    @style.setter
    def style(self, value):
        assert value in LineStyle.VALID_STYLES, "'%s' is not a valid "\
            "line style" % (value)
        self._style = LineStyle.VALID_STYLES[value]

    @style.getter
    def style(self):
        return self._style
