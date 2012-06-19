import collections

class LabelProperties(collections.MutableMapping):
    """
    A dictionary of properties that define how labels look.
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
