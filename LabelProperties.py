import collections

class LabelProperties(collections.MutableMapping):
    """
    A dictionary of properties that define how labels look. Valid properties
    are:

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

    """
    VALID_PROPERTIES = ["alpha",
                        "backgroundColor",
                        "color",
                        "fontsize",
                        "horizontalalignment",
                        "linespacing",
                        "multialignment",
                        "rotation",
                        "rotation_mode",
                        "stretch",
                        "style",
                        "verticalalignment",
                        "weight"]

    def __init__(self):
        self._props = {}

    def __getitem__(self, key):
        return self._props[key]

    def __setitem__(self, key, value):
        if key not in LabelProperties.VALID_PROPERTIES:
            raise ValueError("Label property '%s' is not currently supported"\
                                 % (key))
        self._props[key] = value

    def __delitem__(self, key):
        del self._props[key]


    def __iter__(self):
        return self._props.__iter__()

    def __len__(self):
        return len(self._props)

    def update(self, props):
        if type(props) == dict:
            for key, value in props.items():
                self.__setitem__(key, value)
        elif type(props) == LabelProperties:
            self.update(props._props)
        else:
            raise TypeError("Incorrect argument type %s passed to "
                            "LabelProperties.update" % (type(props)))

    def clear(self):
        self._props.clear()
