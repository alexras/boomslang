from boomslang.LineStyle import LineStyle

class Grid(object):
    """
    The Grid plot element defines a set of gridlines that are displayed behind
    all other plot elements
    """

    def __init__(self, color="#dddddd", style="-", visible=True):
        self.color = color
        """
        The color of the gridlines; see :ref:`styling-colors` for more
        information on available colors.
        """

        self._lineStyle = LineStyle()
        self._lineStyle.style = style

        self.visible = visible
        """
        If True, the grid's lines are visible. If False, they are invisible.
        """

        self.which = 'major'
        """
        If "major", the plot's major ticks have grid lines. If "minor", the
        plot's minor ticks have grid lines. If "both", both major and minor
        ticks have grid lines.
        """

    @property
    def style(self):
        """
        The style of the grid's lines; see :ref:`styling-lines` for more
        information about available line styles.
        """
        return self._lineStyle.style

    @style.setter
    def style(self, value):
        self._lineStyle.style = value

    def draw(self, fig, axes):
        if self.visible:
            axes.grid(color=self.color, linestyle=self.style,
                      which=self.which)
            # Gridlines should be below plots
            axes.set_axisbelow(True)
