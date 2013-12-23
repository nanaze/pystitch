import color_map
import color
import unittest

class ColorMapTest(unittest.TestCase):

  def testColorMap(self):
    cmap = color_map.ColorMap()

    a = color.RGBColor(0,0,0)
    self.assertEquals('A', cmap.get(a))

    a2 = color.RGBColor(0,0,0)
    self.assertEquals('A', cmap.get(a2))

    b = color.RGBColor(0,0,1)
    self.assertEquals('B', cmap.get(b))  

    self.assertEquals([(0, 0, 0), (0, 0, 1)], list(cmap))
    self.assertEquals(['A', 'B'], map(lambda c: cmap.get(c), cmap))
        
if __name__ == '__main__':
    unittest.main()
