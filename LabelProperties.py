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
        assert key in VALID_PROPERTIES, ("Label property '%s' is not "
                                         "currently supported") % (key)
        self._props[key] = value
            
    def __delitem__(self, key):
        del self._props[key]
    
