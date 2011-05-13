import pylab
import matplotlib.axes
import matplotlib.transforms
import matplotlib.ticker as mticker
from matplotlib import pyplot
from boomslang import Plot
import numpy as np

class BrokenAxesPiece(matplotlib.axes.Axes):
    def __init__(self, fig, rect, axisbg=None, frameon=True,
            sharex=None, sharey=None, label='', xscale=None,
            yscale=None,
            xform=None,
            **kwargs):

        if xform is None: self.xform = lambda x: x
        else: self.xform = xform

        super(BrokenAxesPiece,self).__init__(fig, rect, axisbg, frameon,
                sharex, sharey, label, xscale, yscale, **kwargs)


    def set_position(self, pos, which='both'):
        if which == 'both' or which == 'original':
            super(BrokenAxesPiece, self).set_position(pos, 'both')
        elif which == 'active':
            l,b,w,h = pos.get_points().flatten().tolist()
            l,b,w,h = self.xform(l,b,w,h)
            new_pos = matplotlib.transforms.Bbox([[l,b],[w,h]])

            super(BrokenAxesPiece, self).set_position(new_pos, 'active')

class BrokenAxisPlot(Plot):
    """
    Represents a single broken-axis plot.  Not embeddable into nested
    PlotLayouts at the moment.
    """

    def __init__(self,
                 break_points,
                 break_line_size = 0.015,
                 break_hspace = 0.05,
                 break_ratio = 0.5):

        super(BrokenAxisPlot,self).__init__()

        self.break_points = break_points
        self.break_line_size = break_line_size
        self.break_hspace = break_hspace
        self.break_ratio = break_ratio

    def subplot(self, row, column, position):
        # Step 0, plot in normal space to build up base fig and stats
        orig_ax = pylab.subplot(row, column, position)

        orig = (self.legend, self.legendCols)
        (self.legend, self.legendCols) = False, 0
        handles = self.drawPlot(orig_ax)

        nticks = len(orig_ax.get_yticks())

        print orig_ax.yaxis.get_label(), orig_ax.yaxis.labelpad

        if True:
            for side in ['top','bottom','left','right']:
                orig_ax.spines[side].set_visible(False)

            orig_ax.grid(False)
            orig_ax.cla()

            orig_ax.xaxis.set_visible(False)
            orig_ax.set_yticks([0])
            orig_ax.set_yticklabels(["    "])

        f = pylab.gcf()

        hs = self.break_hspace * 1

        def top_xform(l,b,w,h):
            return (l,b + (h-b+hs) * self.break_ratio,w,h)

        def bot_xform(l,b,w,h):
            return (l,b,w,h-(h-b+hs) * (1-self.break_ratio))

        # Hork
        r = orig_ax.transAxes._boxout._bbox


        ax2 = BrokenAxesPiece(f, r, sharex=orig_ax, xform=bot_xform)
        f.add_axes(ax2)

        handles = self.drawPlot(ax2)

        # Re-enable the legend
        (self.legend, self.legendCols) = orig

        ax = BrokenAxesPiece(f, r, sharex=orig_ax, xform=top_xform)
        f.add_axes(ax)

        handles = self.drawPlot(ax)

        print orig_ax.get_legend(), ax.get_legend(), ax2.get_legend()

        # Set Limits
        (y_bot, y_top) = ax.get_ylim()

        ax2.set_ylim(y_bot, self.break_points[0])
        ax.set_ylim(self.break_points[1], y_top)

        # Re-tick things
        numticks2 = (self.break_ratio * nticks * (1 / (1+hs))) - 1
        numticks = ((1 - self.break_ratio) * nticks * (1/(1+hs)))

        numticks2 = max(numticks2, 2)
        numticks = max(numticks, 2)

        print orig_ax.get_yticks(), nticks, numticks, numticks2

        ax2.yaxis.set_major_locator(mticker.LinearLocator(numticks=numticks2))
        ax.yaxis.set_major_locator(mticker.LinearLocator(numticks=numticks))

        ax2.set_xticks(orig_ax.get_xticks())
        ax2.set_xticklabels([t.get_text() for t in orig_ax.get_xticklabels()])
        #print ax2.get_xticks()
        #print ax2.get_xticklabels()[0]

        ax.spines['bottom'].set_visible(False)
        ax2.spines['top'].set_visible(False)

        ax.xaxis.tick_top()
        ax.tick_params(labeltop='off')
        ax2.xaxis.tick_bottom()

        orig_ax.set_ylabel(ax.get_ylabel())
        ax.set_ylabel("")
        ax2.set_ylabel("")


        kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)

        ax.plot((-self.break_line_size,
                 +self.break_line_size),
                (-self.break_line_size/(1-self.break_ratio),
                 +self.break_line_size/(1-self.break_ratio)),
                **kwargs) # top-left

        ax.plot((1-self.break_line_size,
                 1+self.break_line_size),
                (-self.break_line_size/(1-self.break_ratio),
                 +self.break_line_size/(1-self.break_ratio)),
                **kwargs) # top-right

        kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False)

        ax2.plot((-self.break_line_size,
                  +self.break_line_size),
                (1-self.break_line_size/(self.break_ratio),
                 1+self.break_line_size/(self.break_ratio)),
                **kwargs) # bottom-left

        ax2.plot((1-self.break_line_size,
                  1+self.break_line_size),
                (1-self.break_line_size/(self.break_ratio),
                 1+self.break_line_size/(self.break_ratio)),
                **kwargs) # bottom-right

        return handles
