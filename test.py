import unittest
import os
from PIL import Image
from PIL import ImageChops

class TestExamples(unittest.TestCase):        
    def assert_images_same(self, im1_path, im2_path):
        im1 = Image.open(im1_path)
        im2 = Image.open(im2_path)

        diff = ImageChops.difference(im2,im1).getbbox()
        
        self.assertTrue(diff == None, "Images differ; bounding box of "
                        "difference is %s" % (diff,))

    def test_vs_reference(self):
        for example in filter(lambda x: x.endswith('py'), 
                              os.listdir('examples')):
            example_no_py = example[:-3]
            full_path = os.path.join('examples', example)
            result_path = example_no_py + ".png"
            reference_path = os.path.join('examples', 'reference', 
                                          result_path)
            
            res = os.system("python %s" % (full_path))
            self.assertTrue(res == 0)
            self.assert_images_same(result_path, reference_path)
            os.unlink(result_path)

if __name__ == '__main__':
    unittest.main()
