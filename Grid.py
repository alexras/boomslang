from boomslang.LineStyle import LineStyle

class Grid(object):
    def __init__(self, color="#dddddd", style="-", visible=True):
        self.color = color
        self._lineStyle = LineStyle()
        self._lineStyle.style = style
        self.visible = visible
        self.which = 'major'

    @property
    def style(self):
        return self._lineStyle.style

    @style.setter
    def style(self, value):
        self._lineStyle.style = value

    @style.getter
    def style(self):
        return self._lineStyle.style

    def draw(self, fig, axes):
        if self.visible:
            axes.grid(color=self.color, linestyle=self.style,
                      which=self.which)
            # Gridlines should be below plots
            axes.set_axisbelow(True)
