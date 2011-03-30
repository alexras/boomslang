class Location(object):
    _LOCATION_TRANSLATOR = {
        "best" : ["best"],
        "upper right" : ["top right"],
        "upper left" : ["top left"],
        "lower left" : ["bottom left"],
        "lower right" : ["bottom right"],
        "right" : [],
        "center left" : ["middle left", "left"],
        "center right" : ["middle right", "right"],
        "lower center" : ["bottom middle", "bottom center"],
        "upper center" : ["top middle", "upper middle"],
        "center" : ["middle"]
     }
    
    VALID_LOCATIONS = {}

    for (glyph, equivalents) in _LOCATION_TRANSLATOR.items():
        VALID_LOCATIONS[glyph] = glyph

        for equiv in equivalents:
            VALID_LOCATIONS[equiv] = glyph

    def __init__(self):
        self._location = "best"

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        assert value in VALID_LOCATIONS, "'%s' is not a valid legend location"
        self._location = VALID_LOCATIONS[value]
