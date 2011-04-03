from boomslang.LineStyle import LineStyle
from LineStyle import LineStyle

class Grid(object):
    def __init__(self, color=None, style=None, visible=False):
        self.color = color
        self._lineStyle = LineStyle()
        self._lineStyle.style = style
        self.visible = visible

    @property
    def style(self):
        return self._lineStyle.style

    @style.setter
    def style(self, value):
        self._lineStyle.style = value

    @style.getter
    def style(self):
        return self._lineStyle.style

    def draw(self, axes):
        if self.visible:
            axes.grid(color=self.color, linestyle=self.lineStyle.style)
            # Gridlines should be below plots
            axes.set_axisbelow(True)
