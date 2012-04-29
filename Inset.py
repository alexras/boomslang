from Location import Location
import sys
from boomslang_exceptions import BoomslangPlotRenderingException,\
    BoomslangPlotConfigurationException
from BoundedFloat import BoundedFloat

try:
    import mpl_toolkits.axes_grid.inset_locator
    BOOMSLANG_INSET_LOCATOR_LOADED = True
except ImportError:
    BOOMSLANG_INSET_LOCATOR_LOADED = False


class Inset(object):
    width = BoundedFloat("width", minimum = 0.0, maximum = 1.0)
    height = BoundedFloat("height", minimum = 0.0, maximum = 1.0)
    location = Location("location")

    def __init__(self, plot, width=0.3, height=0.3, location="best",
                 padding=0.05):
        self.plot = plot

        self.width = width
        self.height = height
        self.location = location
        self.padding = padding

    def draw(self, fig, axes):
        if not BOOMSLANG_INSET_LOCATOR_LOADED:
            print >>sys.stderr, "Plotting insets requires " \
                "mpl_toolkits.axes_grid.inset_locator, which " \
                "your version of matplotlib doesn't appear to " \
                "have."
            sys.exit(1)

        insetAxes = mpl_toolkits.axes_grid.inset_locator.inset_axes(
            axes,
            width="%.2f%%" % (self.width * 100.0),
            height="%.2f%%" % (self.height * 100.0),
            loc=self.location)

        self.plot.drawPlot(fig, insetAxes)

        return insetAxes
