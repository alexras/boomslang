from boomslang.LineStyle import LineStyle

class Grid(object):
    def __init__(self):
        self.color = None
        self.lineStyle = LineStyle()
        self.visible = False
    
    def draw(self, axes):
        if self.visible:
            axes.grid(color=self.color, linestyle=self.lineStyle.style)
            # Gridlines should be below plots
            axes.set_axisbelow(True)
