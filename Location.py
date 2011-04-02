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


    # Translates location strings into the integers that Matplotlib expects
    LOCATION_TO_INT = {"best" : 0,
                       "upper right" : 1,
                       "upper left" : 2,
                       "lower left" : 3,
                       "lower right" : 4,
                       "right" : 5,
                       "center left" : 6,
                       "center right" : 7,
                       "lower center" : 8,
                       "upper center" : 9,
                       "center" : 10}

    VALID_LOCATIONS = {}

    for (glyph, equivalents) in _LOCATION_TRANSLATOR.items():
        VALID_LOCATIONS[glyph] = glyph

        for equiv in equivalents:
            VALID_LOCATIONS[equiv] = glyph

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value not in Location.VALID_LOCATIONS:
            raise TypeError("'%s' is not a valid legend location" % value)

        instance.__dict__[self.name] = Location.VALID_LOCATIONS[value]

    def __get__(self, instance, owner):
        if self.name not in instance.__dict__:
            raise AttributeError, self.name

        return Location.LOCATION_TO_INT[instance.__dict__[self.name]]
