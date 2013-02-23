import color 
import unittest

class TestColor(unittest.TestCase):

  def testColor(self):
    c = color.RGBColor(1,2,3)
    self.assertEquals(1, c.red)
    self.assertEquals(2, c.green)
    self.assertEquals(3, c.blue)

    self.assertTupleEqual((1,2,3), c)

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
  
    

if __name__ == '__main__':
    unittest.main()
