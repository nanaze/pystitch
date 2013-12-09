import unittest
import os
from PIL import Image 
import image

def _GetTestDataDir():
  return os.path.join(os.path.dirname(__file__), 'testdata')


class ImageTest(unittest.TestCase):

  def testImageAsRGB(self):
    image_path = os.path.join(_GetTestDataDir(), 'sample.png')
    img = Image.open(image_path)
    img = img.convert('RGBA')

    pixel_arr = image.GetPixelArrayFromImage(img)

    self.assertEquals(10, pixel_arr.size[0])
    self.assertEquals(10, pixel_arr.size[1])    
    self.assertEquals((0, 0, 0), pixel_arr[0, 0])
    self.assertEquals((202, 0, 0), pixel_arr[9, 9])
    
if __name__ == '__main__':
    unittest.main()
