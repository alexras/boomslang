from PIL import Image
from PIL import ImageChops
from abc import ABCMeta,abstractmethod
import os
import unittest

from matplotlib import rc

from boomslang import Fonts

Fonts.useBoomslangFonts()

class ImageComparisonTestCase():
    __metaclass__ = ABCMeta

    scriptPath = os.path.abspath(os.path.dirname(__file__))

    TEST_CASE_NAME = "testImageComparison"

    def setUp(self):
        if os.path.exists(self.imageName):
            os.unlink(self.imageName)

    @abstractmethod
    def constructImage(self):
        pass

    def testImageComparison(self):
        self.constructImage()

        referenceImage = os.path.abspath(os.path.join(
                self.scriptPath, "reference", self.imageName))

        ourImage = Image.open(self.imageName)
        refImage = Image.open(referenceImage)

        diff = ImageChops.difference(refImage, ourImage).getbbox()

        self.assertTrue(diff == None, "Image differs from reference; "
                        "bounding box of difference is %s" % (diff,))

        if os.path.exists(self.imageName):
            os.unlink(self.imageName)
