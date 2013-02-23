import color 
import unittest

class TestColor(unittest.TestCase):

  def testColor(self):
    c = color.RGBColor(1,2,3)
    self.assertEquals(1, c.red)
    self.assertEquals(2, c.green)
    self.assertEquals(3, c.blue)

    self.assertTupleEqual((1,2,3), c)

if __name__ == '__main__':
    unittest.main()
