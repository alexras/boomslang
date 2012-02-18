from matplotlib.font_manager import FontProperties
import os

_fonts_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "fonts"))

class FontFace:
    def __init__(self, regular_font = None, italic_font = None,
                 bold_font = None, bold_italic_font = None):

        if regular_font != None:
            self.regular = FontProperties(
                fname = os.path.join(_fonts_directory, regular_font),
                style = "normal",
                variant = "normal",
                weight = "normal",
                stretch = "normal")
        else:
            self.regular = None

        if italic_font != None:
            self.italic = FontProperties(
                fname = os.path.join(_fonts_directory, italic_font),
                style = "italic",
                variant = "normal",
                weight = "normal",
                stretch = "normal")
        else:
            self.italic = None

        if bold_font != None:
            self.bold = FontProperties(
                fname = os.path.join(_fonts_directory, bold_font),
                style = "normal",
                variant = "normal",
                weight = "bold",
                stretch = "normal")
        else:
            self.bold = None

        if bold_italic_font != None:
            self.bold_italic = FontProperties(
                fname = os.path.join(_fonts_directory, bold_italic_font),
                style = "italic",
                variant = "normal",
                weight = "bold",
                stretch = "normal")
        else:
            self.bold_italic = None

sans_serif = FontFace(regular_font = "Arimo-Regular-Latin.ttf",
                      italic_font = "Arimo-Italic-Latin.ttf",
                      bold_font = "Arimo-Bold-Latin.ttf",
                      bold_italic_font = "Arimo-BoldItalic-Latin.ttf")

serif = FontFace(regular_font = "Tinos-Regular.ttf",
                 italic_font = "Tinos-Italic.ttf",
                 bold_font = "Tinos-Bold.ttf",
                 bold_italic_font = "Tinos-BoldItalic.ttf")

monospace = FontFace(regular_font = "Lekton-Regular.ttf",
                     italic_font = "Lekton-Italic.ttf",
                     bold_font = "Lekton-Bold.ttf")
