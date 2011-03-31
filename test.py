import unittest

# FIXME: once Python 2.7 becomes more widely adopted, use unittest's test
# discovery feature

from examples.boxandwhisker import BoxAndWhiskerTest
from examples.bar import BarTest
from examples.clusteredbars import ClusteredBarsTest
from examples.errorbars import ErrorBarsTest
from examples.hatchedbars import HatchedBarsTest
from examples.inset import InsetTest
from examples.latex import LatexTest
from examples.layout import LayoutTest

testSuite = unittest.TestSuite()
testSuite.addTest(BoxAndWhiskerTest())
testSuite.addTest(BarTest())
testSuite.addTest(ClusteredBarsTest())
testSuite.addTest(ErrorBarsTest())
testSuite.addTest(HatchedBarsTest())
testSuite.addTest(InsetTest())
testSuite.addTest(LatexTest())
testSuite.addTest(LayoutTest())

runner = unittest.TextTestRunner()
runner.run(testSuite)
