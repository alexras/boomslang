class BoundedFloat(object):
    """
    BoundedFloats behave like floats, but are required to be within
    `minimum` (inclusive) and `maximum` (exclusive)
    """

    def __init__(self, name, minimum, maximum, default=None):
        self.name = name
        self.min = float(minimum)
        self.max = float(maximum)

        if default != None:
            if default < self.min or default >= self.max:
                raise ValueError("Default value %.2f out-of-bounds [%.2f,%.2f)",
                                 default, self.min, self.max)

        self.default = default

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Value %s not a float", value)

        if value >= self.max or value < self.min:
            raise ValueError("Value %f out-of-bounds [%.2f, %.2f)", value,
                             self.min, self.max)

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if self.name not in instance.__dict__:
            if self.default == None:
                instance.__dict__[self.name] = self.min
            else:
                instance.__dict__[self.name] = self.default

        return instance.__dict__[self.name]

