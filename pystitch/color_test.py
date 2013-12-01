import color 
import unittest

class TestColor(unittest.TestCase):

  def testColor(self):
    c = color.RGBColor(1,2,3)
    self.assertEquals(1, c.red)
    self.assertEquals(2, c.green)
    self.assertEquals(3, c.blue)

    self.assertEqual(color.RGBColor(1,2,3), c)

  def testValue(self):
    self.assertRaises(ValueError, lambda: color.RGBColor(-1, 0, 0))
    self.assertRaises(ValueError, lambda: color.RGBColor(0, -1, 0))
    self.assertRaises(ValueError, lambda: color.RGBColor(0, 0, -1))

    self.assertRaises(ValueError, lambda: color.RGBColor(256, 255, 255))
    self.assertRaises(ValueError, lambda: color.RGBColor(255, 256, 255))
    self.assertRaises(ValueError, lambda: color.RGBColor(255, 255, 256))
      
    # Check OK values
    color.RGBColor(0,0,0)
    color.RGBColor(255, 255, 255)

  def testDistance(self):
    a = color.RGBColor(0,0,0)
    b = color.RGBColor(0,0,0)
    c = color.RGBColor(255,0,0)
    d = color.RGBColor(255,255,255)

    self.assertEquals(0, color.RGBColor.distance(a, b))
    self.assertEquals(255, color.RGBColor.distance(a, c))
    self.assertAlmostEqual(441.67, 
        color.RGBColor.distance(a, d), places=2)

  def testRGBColorFromHexString(self):
    self.assertEquals(color.RGBColor(255, 0, 166),
                      color.RGBColorFromHexString('#ff00a6'))
    self.assertEquals(color.RGBColor(255, 0, 166),
                      color.RGBColorFromHexString('ff00a6'))
    self.assertRaises(lambda: color.RGBColorFromHexString('#ffgghh'))

if __name__ == '__main__':
    unittest.main()
