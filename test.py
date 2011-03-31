import unittest

# FIXME: once Python 2.7 becomes more widely adopted, use unittest's test
# discovery feature

from examples.bar import BarTest
from examples.boxandwhisker import BoxAndWhiskerTest
from examples.clusteredbars import ClusteredBarsTest
from examples.errorbars import ErrorBarsTest
from examples.fontsizes import FontSizesTest
from examples.hatchedbars import HatchedBarsTest
from examples.inset import InsetTest
from examples.label import LabelTest
from examples.latex import LatexTest
from examples.layout import LayoutTest
from examples.legendLabelSizes import LegendLabelSizesTest
from examples.linestyles import LineStylesTest
from examples.linestyles2 import LineStyles2Test
from examples.logscale import LogScaleTest
from examples.scatter import ScatterTest
from examples.simpleline import SimpleLineTest
from examples.split import SplitTest
from examples.stackedbar import StackedBarTest
from examples.stackedlines import StackedLinesTest
from examples.steps import StepsTest
from examples.tickstyles import TickStylesTest
from examples.twinx import TwinXTest
from examples.unordered import UnorderedTest
from examples.vline import VLineTest
from examples.weightedlayout import WeightedLayoutTest

testSuite = unittest.TestSuite()
testSuite.addTest(BoxAndWhiskerTest())
testSuite.addTest(BarTest())
testSuite.addTest(ClusteredBarsTest())
testSuite.addTest(ErrorBarsTest())
testSuite.addTest(FontSizesTest())
testSuite.addTest(HatchedBarsTest())
testSuite.addTest(InsetTest())
testSuite.addTest(LabelTest())
testSuite.addTest(LatexTest())
testSuite.addTest(LayoutTest())
testSuite.addTest(LegendLabelSizesTest())
testSuite.addTest(LineStylesTest())
testSuite.addTest(LineStyles2Test())
testSuite.addTest(LogScaleTest())
testSuite.addTest(ScatterTest())
testSuite.addTest(SimpleLineTest())
testSuite.addTest(SplitTest())
testSuite.addTest(StackedBarTest())
testSuite.addTest(StackedLinesTest())
testSuite.addTest(StepsTest())
testSuite.addTest(TickStylesTest())
testSuite.addTest(TwinXTest())
testSuite.addTest(UnorderedTest())
testSuite.addTest(VLineTest())
testSuite.addTest(WeightedLayoutTest())

runner = unittest.TextTestRunner()
runner.run(testSuite)
