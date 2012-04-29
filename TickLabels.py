from LabelProperties import LabelProperties

class TickLabels(object):
    def __init__(self):
        self._formatter = None
        self.labels = None
        self.labelPoints = None
        self._properties = LabelProperties()
        self.size = None

    @property
    def properties(self):
        return self._properties

    @property
    def formatter(self):
        return self._formatter

    @formatter.setter
    def formatter(self, func):
        self._formatter = pylab.FuncFormatter(func)

    def draw(self, axes, axis):
        if self.labelPoints is not None:
            axis.set_ticks(self.labelPoints)

        if self.labels is not None:
            axis.set_ticklabels(self.labels, **self.properties)

        if self.formatter is not None:
            axis.set_major_formatter(self.formatter)

        if self.size is not None:
            for tick in axis.get_majorticklabels():
                tick.set_fontsize(self.size)
