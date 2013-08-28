from Location import Location
import warnings, itertools
from Utils import _check_min_matplotlib_version

# Adapted from http://stackoverflow.com/a/10101532
def _flip(items, ncol):
    """The items in `items` are listed in column order and displayed across
    `ncol` columns. Re-order the list so that the items will be displayed
    across rows rather than down columns."""

    return list(itertools.chain(*[items[i::ncol] for i in range(ncol)]))

class Legend(object):
    location = Location("location")

    def __init__(self, columns = 1, scatterPoints = 3, drawFrame = True,
                 location = "best", figLegend = False, labelSize = None,
                 bboxToAnchor = None, title = None, leftToRight = False,
                 labelOrdering = None):
        self.location = location
        self.labelSize = labelSize
        self.columns = columns
        self.scatterPoints = scatterPoints
        self.drawFrame = drawFrame
        self.figLegend = figLegend
        self.bboxToAnchor = bboxToAnchor
        self.title = title
        self.labelOrdering = labelOrdering
        self.leftToRight = leftToRight

    def _genLegendKeywords(self):
        legendKeywords = {}

        if self.columns > 1:
            if not _check_min_matplotlib_version(0, 98, 0):
                warnings.warn("Number of columns support not available "
                              "in versions of matplotlib prior to 0.98")
            else:
                legendKeywords["ncol"] = self.columns
                legendKeywords["scatterpoints"] = self.scatterPoints

        if self.labelSize is not None:
            legendKeywords["prop"] = {"size" : self.labelSize}

        if self.bboxToAnchor is not None:
            legendKeywords["bbox_to_anchor"] = self.bboxToAnchor

        if self.title is not None:
            legendKeywords["title"] = self.title

        return legendKeywords

    def draw(self, figure, axes, handles, labels):
        legendKeywords = self._genLegendKeywords()

        legend = None

        if self.labelOrdering is not None:
            label_handle_pairs = zip(labels, handles)

            def label_sorter(x):
                try:
                    return self.labelOrdering.index(x[0])
                except ValueError, e:
                    return None

            label_handle_pairs.sort(key=label_sorter)

            labels, handles = zip(*label_handle_pairs)

        if self.leftToRight and self.columns > 1:
            handles = _flip(handles, self.columns)
            labels = _flip(labels, self.columns)

        if self.figLegend:
            legend = figure.legend(handles, labels, loc=self.location,
                                   **legendKeywords)
        else:
            legend = axes.legend(handles, labels, loc=self.location,
                                 **legendKeywords)

        if legend is not None:
            legend.draw_frame(self.drawFrame)
