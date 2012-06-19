import matplotlib.axes
import matplotlib.transforms
import matplotlib.ticker as mticker
from boomslang import Plot
import numpy as np

class BrokenAxesPiece(matplotlib.axes.Axes):
    def __init__(self, fig, rect, axisbg=None, frameon=True,
            sharex=None, sharey=None, label='', xscale=None,
            yscale=None,
            xform=None,
            **kwargs):

        if xform is None:
            self.xform = lambda x: x
        else:
            self.xform = xform

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
        """
        A 2-tuple that defines the start and end points of the gap on the y-axis
        """

        self.break_line_size = break_line_size
        """
        The size of the broken axis lines
        """

        self.break_hspace = break_hspace
        """
        The amount of horizontal space to put between the break points
        """

        self.break_ratio = break_ratio
        """
        Defines how to divvy up space between the two broken parts of the plot
        """

    def subplot(self, fig, row, column, position, projection):
        # Step 0, plot in normal space to build up base fig and stats
        orig_ax = fig.add_subplot(row, column, position)

        # Save legend and set it to None
        orig_legend = self.legend
        self.legend = None

        handles = self.drawPlot(fig, orig_ax)

        nticks = len(orig_ax.get_yticks())

        if True:
            for side in ['top','bottom','left','right']:
                orig_ax.spines[side].set_visible(False)

            orig_ax.grid(False)
            orig_ax.cla()

            orig_ax.xaxis.set_visible(False)
            orig_ax.set_yticks([0])
            orig_ax.set_yticklabels(["    "])

        hs = self.break_hspace * 1

        def top_xform(l,b,w,h):
            return (l,b + (h-b+hs) * self.break_ratio,w,h)

        def bot_xform(l,b,w,h):
            return (l,b,w,h-(h-b+hs) * (1-self.break_ratio))

        # Hork
        r = orig_ax.transAxes._boxout._bbox


        ax2 = BrokenAxesPiece(fig, r, sharex=orig_ax, xform=bot_xform)
        fig.add_axes(ax2)

        handles = self.drawPlot(fig, ax2)

        # Re-enable the legend
        self.legend = orig_legend

        ax = BrokenAxesPiece(fig, r, sharex=orig_ax, xform=top_xform)
        fig.add_axes(ax)

        handles = self.drawPlot(fig, ax)

        # Set Limits
        (y_bot, y_top) = ax.get_ylim()

        ax2.set_ylim(y_bot, self.break_points[0])
        ax.set_ylim(self.break_points[1], y_top)

        # Re-tick things
        numticks2 = (self.break_ratio * nticks * (1 / (1+hs))) - 1
        numticks = ((1 - self.break_ratio) * nticks * (1/(1+hs)))

        numticks2 = max(numticks2, 2)
        numticks = max(numticks, 2)

        ax2.yaxis.set_major_locator(mticker.LinearLocator(numticks=numticks2))
        ax.yaxis.set_major_locator(mticker.LinearLocator(numticks=numticks))

        ax2.set_xticks(orig_ax.get_xticks())
        ax2.set_xticklabels([t.get_text() for t in orig_ax.get_xticklabels()])

        ax.spines['bottom'].set_visible(False)
        ax2.spines['top'].set_visible(False)

        ax.xaxis.tick_top()
        ax.tick_params(labeltop='off')
        ax2.xaxis.tick_bottom()

        orig_ax.set_ylabel(ax.get_ylabel())
        ax.set_ylabel("")
        ax2.set_ylabel("")

        ax.set_xlabel("")

        kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)

        ax.plot((-self.break_line_size,
                 self.break_line_size),
                (-self.break_line_size/(1-self.break_ratio),
                 self.break_line_size/(1-self.break_ratio)),
                **kwargs) # top-left

        ax.plot((1-self.break_line_size,
                 1+self.break_line_size),
                (-self.break_line_size/(1-self.break_ratio),
                 self.break_line_size/(1-self.break_ratio)),
                **kwargs) # top-right

        kwargs = dict(transform=ax2.transAxes, color='k', clip_on=False)

        ax2.plot((-self.break_line_size,
                  self.break_line_size),
                (1-self.break_line_size/(self.break_ratio),
                 1+self.break_line_size/(self.break_ratio)),
                **kwargs) # bottom-left

        ax2.plot((1-self.break_line_size,
                  1+self.break_line_size),
                (1-self.break_line_size/(self.break_ratio),
                 1+self.break_line_size/(self.break_ratio)),
                **kwargs) # bottom-right

        return handles
