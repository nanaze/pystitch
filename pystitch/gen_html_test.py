import gen_html
import unittest
import color

class GenHtmlTest(unittest.TestCase):

  def tesGetTextColor(self):
    self.assertEquals(color.RGBColor(0,0,0), gen_html._GetTextColor((120, 120, 120)))
    self.assertEquals(color.RGBColor(255,255,255), gen_html._GetTextColor((130, 130, 130)))


        
if __name__ == '__main__':
    unittest.main()
