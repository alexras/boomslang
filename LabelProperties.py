import collections
import sys

class LabelProperties(collections.MutableMapping):
    VALID_PROPERTIES = ["alpha",
                        "backgroundColor",
                        "color",
                        "horizontalalignment",
                        "linespacing",
                        "multialignment",
                        "rotation",
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
